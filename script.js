/**
 * script.js — StudyBuddy AI
 * ==========================
 * Handles all frontend chat logic:
 *  - Sending messages to Flask API
 *  - Rendering bot & user bubbles
 *  - Typing animation
 *  - Markdown-like text formatting
 *  - Auto-scroll, clear chat, mobile sidebar
 *  - Quick action buttons & welcome chips
 */

"use strict";

/* ─────────────────────────────────────────────
   CONFIG
───────────────────────────────────────────── */
const API_URL       = "http://localhost:5000/chat";
const BOT_DELAY_MIN = 600;   // ms — minimum "thinking" time
const BOT_DELAY_MAX = 1400;  // ms — maximum "thinking" time

/* ─────────────────────────────────────────────
   DOM REFS
───────────────────────────────────────────── */
const messagesEl      = document.getElementById("messages");
const userInputEl     = document.getElementById("userInput");
const sendBtnEl       = document.getElementById("sendBtn");
const typingEl        = document.getElementById("typingIndicator");
const clearBtnEl      = document.getElementById("clearBtn");
const clearBtnHdrEl   = document.getElementById("clearBtnHeader");
const welcomeScreenEl = document.getElementById("welcomeScreen");
const sidebarEl       = document.getElementById("sidebar");
const sidebarToggleEl = document.getElementById("sidebarToggle");

/* ─────────────────────────────────────────────
   STATE
───────────────────────────────────────────── */
let isBotThinking = false;
let conversationStarted = false;

/* ─────────────────────────────────────────────
   UTILITIES
───────────────────────────────────────────── */

/** Return formatted time string like "09:45 AM" */
function getTimeString() {
  return new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
}

/** Simulate natural bot response delay */
function randomDelay() {
  return Math.floor(Math.random() * (BOT_DELAY_MAX - BOT_DELAY_MIN + 1)) + BOT_DELAY_MIN;
}

/** Scroll messages container to the bottom */
function scrollToBottom(smooth = true) {
  messagesEl.scrollTo({
    top: messagesEl.scrollHeight,
    behavior: smooth ? "smooth" : "instant",
  });
}

/**
 * Very lightweight Markdown → HTML renderer.
 * Handles: **bold**, *italic*, `code`, ```blocks```,
 *          bullet lists, numbered lists, --- hr
 */
function formatMessage(text) {
  // Escape HTML entities first
  let html = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  // Code blocks (``` ... ```)
  html = html.replace(/```([\s\S]*?)```/g, (_, code) => {
    return `<pre><code>${code.trim()}</code></pre>`;
  });

  // Inline code (`code`)
  html = html.replace(/`([^`\n]+)`/g, "<code>$1</code>");

  // Horizontal rule
  html = html.replace(/^---$/gm, "<hr>");

  // Bold (**text**)
  html = html.replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>");

  // Italic (*text*)
  html = html.replace(/\*(.+?)\*/g, "<em>$1</em>");

  // Process line by line for lists and paragraphs
  const lines = html.split("\n");
  const result = [];
  let inList = false;
  let listType = null;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // Bullet list item
    const bulletMatch = line.match(/^[•\-\*] (.+)/);
    // Numbered list item
    const numberedMatch = line.match(/^(\d+)\. (.+)/);

    if (bulletMatch) {
      if (!inList || listType !== "ul") {
        if (inList) result.push(`</${listType}>`);
        result.push("<ul>");
        inList = true; listType = "ul";
      }
      result.push(`<li>${bulletMatch[1]}</li>`);
    } else if (numberedMatch) {
      if (!inList || listType !== "ol") {
        if (inList) result.push(`</${listType}>`);
        result.push("<ol>");
        inList = true; listType = "ol";
      }
      result.push(`<li>${numberedMatch[2]}</li>`);
    } else {
      if (inList) {
        result.push(`</${listType}>`);
        inList = false; listType = null;
      }
      if (line.trim() === "" || line.trim() === "<hr>") {
        result.push(line.trim() || "<br>");
      } else {
        result.push(`<p>${line}</p>`);
      }
    }
  }
  if (inList) result.push(`</${listType}>`);

  return result.join("\n");
}

/* ─────────────────────────────────────────────
   RENDER FUNCTIONS
───────────────────────────────────────────── */

/**
 * Append a message bubble to the chat.
 * @param {string} text     - Message content
 * @param {"bot"|"user"} from - Sender
 */
function appendMessage(text, from) {
  // Hide welcome screen on first message
  if (!conversationStarted) {
    welcomeScreenEl.style.display = "none";
    conversationStarted = true;
  }

  const msgEl = document.createElement("div");
  msgEl.classList.add("message", `message--${from}`);

  const avatarEl = document.createElement("div");
  avatarEl.classList.add("message__avatar");
  avatarEl.textContent = from === "bot" ? "SB" : "ME";

  const bodyEl = document.createElement("div");
  bodyEl.classList.add("message__body");

  const bubbleEl = document.createElement("div");
  bubbleEl.classList.add("message__bubble");

  if (from === "bot") {
    bubbleEl.innerHTML = formatMessage(text);
  } else {
    // User messages: plain text, escape HTML
    bubbleEl.textContent = text;
  }

  const timeEl = document.createElement("div");
  timeEl.classList.add("message__time");
  timeEl.textContent = getTimeString();

  bodyEl.appendChild(bubbleEl);
  bodyEl.appendChild(timeEl);
  msgEl.appendChild(avatarEl);
  msgEl.appendChild(bodyEl);
  messagesEl.appendChild(msgEl);

  scrollToBottom();
}

/** Show the typing indicator */
function showTyping() {
  typingEl.classList.add("visible");
  scrollToBottom();
}

/** Hide the typing indicator */
function hideTyping() {
  typingEl.classList.remove("visible");
}

/* ─────────────────────────────────────────────
   CORE CHAT LOGIC
───────────────────────────────────────────── */

/**
 * Send a message: render user bubble → show typing → fetch API → render bot bubble
 * @param {string} messageText - Text to send
 */
async function sendMessage(messageText) {
  const text = messageText.trim();
  if (!text || isBotThinking) return;

  // Disable input while bot is thinking
  isBotThinking = true;
  sendBtnEl.disabled = true;
  userInputEl.disabled = true;

  // Render user message
  appendMessage(text, "user");

  // Clear input & reset height
  userInputEl.value = "";
  userInputEl.style.height = "auto";

  // Show typing dots
  showTyping();

  // Artificial delay for realism
  await new Promise((res) => setTimeout(res, randomDelay()));

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text }),
    });

    if (!res.ok) {
      throw new Error(`Server error: ${res.status}`);
    }

    const data = await res.json();
    hideTyping();
    appendMessage(data.response, "bot");

  } catch (err) {
    hideTyping();
    console.error("StudyBuddy API error:", err);
    appendMessage(
      "⚠️ Oops! I couldn't connect to the server. Make sure the Flask backend is running on port 5000.\n\n```\ncd backend\npython app.py\n```",
      "bot"
    );
  } finally {
    isBotThinking = false;
    sendBtnEl.disabled = false;
    userInputEl.disabled = false;
    userInputEl.focus();
  }
}

/* ─────────────────────────────────────────────
   CLEAR CHAT
───────────────────────────────────────────── */

function clearChat() {
  // Remove all messages
  while (messagesEl.firstChild) {
    messagesEl.removeChild(messagesEl.firstChild);
  }

  // Restore welcome screen
  welcomeScreenEl.style.display = "flex";
  messagesEl.appendChild(welcomeScreenEl);
  conversationStarted = false;
}

/* ─────────────────────────────────────────────
   AUTO-RESIZE TEXTAREA
───────────────────────────────────────────── */

function autoResizeTextarea() {
  userInputEl.style.height = "auto";
  const maxH = 120;
  userInputEl.style.height = Math.min(userInputEl.scrollHeight, maxH) + "px";
}

/* ─────────────────────────────────────────────
   MOBILE SIDEBAR
───────────────────────────────────────────── */

// Create overlay element
const overlayEl = document.createElement("div");
overlayEl.classList.add("sidebar-overlay");
document.body.appendChild(overlayEl);

function openSidebar() {
  sidebarEl.classList.add("open");
  overlayEl.classList.add("visible");
}
function closeSidebar() {
  sidebarEl.classList.remove("open");
  overlayEl.classList.remove("visible");
}

/* ─────────────────────────────────────────────
   EVENT LISTENERS
───────────────────────────────────────────── */

// Send on button click
sendBtnEl.addEventListener("click", () => {
  sendMessage(userInputEl.value);
});

// Send on Enter (Shift+Enter = new line)
userInputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    sendMessage(userInputEl.value);
  }
});

// Auto-resize textarea as user types
userInputEl.addEventListener("input", autoResizeTextarea);

// Clear chat buttons
clearBtnEl.addEventListener("click", clearChat);
clearBtnHdrEl.addEventListener("click", clearChat);

// Mobile sidebar toggle
sidebarToggleEl.addEventListener("click", () => {
  sidebarEl.classList.contains("open") ? closeSidebar() : openSidebar();
});
overlayEl.addEventListener("click", closeSidebar);

// Quick action buttons in sidebar
document.querySelectorAll(".quick-btn[data-query]").forEach((btn) => {
  btn.addEventListener("click", () => {
    const query = btn.dataset.query;
    closeSidebar();
    sendMessage(query);
  });
});

// Welcome screen chips
document.querySelectorAll(".chip[data-query]").forEach((chip) => {
  chip.addEventListener("click", () => {
    sendMessage(chip.dataset.query);
  });
});

/* ─────────────────────────────────────────────
   INIT: AUTO-WELCOME MESSAGE
───────────────────────────────────────────── */

(async function init() {
  // Small delay so the page renders first
  await new Promise((res) => setTimeout(res, 800));

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: "hello" }),
    });
    const data = await res.json();
    // Render the welcome message from the bot without user bubble
    appendMessage(data.response, "bot");
  } catch (err) {
    // Server not running — show offline fallback message
    appendMessage(
      "👋 Welcome to **StudyBuddy AI**!\n\n⚠️ *Backend not detected.* To start the Flask server:\n\n```\ncd backend\npip install -r requirements.txt\npython app.py\n```\n\nThen refresh this page. I'll be here when you get back! 🚀",
      "bot"
    );
  }

  userInputEl.focus();
})();
