# 🤖 StudyBuddy AI — Rule-Based CS Mentor Chatbot

> A production-quality, intelligent-looking student mentor chatbot built entirely with Python, Flask, and Vanilla JavaScript — **no LLM, no AI APIs, no ML libraries**.

![StudyBuddy AI Banner](https://img.shields.io/badge/StudyBuddy-AI%20Mentor-38bdf8?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📖 Project Overview

**StudyBuddy AI** is a smart, rule-based chatbot designed to help Computer Science students with:
- 📚 Learning roadmaps for 20+ CS topics
- 🗺️ Curated resources, YouTube channels & practice platforms
- 💪 Motivational support and study tips
- 😄 Programming jokes and fun facts
- 🎯 Guidance through stress, procrastination, and exam anxiety

This project was built to demonstrate **clean software architecture**, **backend API design**, and **modern UI/UX** without relying on any paid AI services.

---

## ✨ Features

### 🤖 Chatbot Engine
- **30+ intents** including greetings, CS topics, student support, study tips, jokes, and more
- Keyword-based intent detection with multi-pass matching
- Randomised responses — never feels repetitive
- Covers: Python, Java, C++, C, JavaScript, HTML, CSS, SQL, DSA, OOP, DBMS, OS, Networks, AI, ML, Deep Learning, Web Dev, Git, and more

### 🎨 Frontend
- Dark glassmorphism UI with animated background grid
- ChatGPT-inspired chat layout
- Typing indicator with bounce animation
- Markdown-like formatting (bold, italic, code blocks, lists)
- Auto-scroll, auto-resize textarea
- Welcome screen with quick-action chips
- Sidebar with 20+ quick-action buttons
- Timestamps on every message
- Mobile-responsive with overlay sidebar
- Keyboard shortcuts (Enter to send, Shift+Enter for new line)

### ⚙️ Backend
- Clean Flask REST API
- CORS enabled for local development
- Modular 3-file architecture
- Zero external AI dependencies
- Health check endpoint

---

## 🛠 Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Language  | Python 3.8+        |
| Framework | Flask 3.0          |
| CORS      | Flask-CORS         |
| Frontend  | HTML5, CSS3, Vanilla JS |
| Fonts     | Space Mono, DM Sans (Google Fonts) |

---

## 📂 Folder Structure

```
studybuddy-ai/
│
├── backend/
│   ├── app.py          # Flask server & API routes
│   ├── chatbot.py      # Rule-based engine (intent detection)
│   ├── intents.py      # All intents, keywords & responses
│   └── requirements.txt
│
├── frontend/
│   ├── index.html      # App shell & markup
│   ├── style.css       # Dark glassmorphism theme
│   └── script.js       # Chat logic, API calls, UI interactions
│
└── README.md
```

---

## 🚀 Installation & Running Locally

### Prerequisites
- Python 3.8 or higher
- pip

### Step 1 — Clone the Repository
```bash
git clone https://github.com/yourusername/studybuddy-ai.git
cd studybuddy-ai
```

### Step 2 — Set Up the Backend
```bash
cd backend
pip install -r requirements.txt
```

### Step 3 — Start the Flask Server
```bash
python app.py
```

You should see:
```
==================================================
  StudyBuddy AI Backend — Starting...
  POST http://localhost:5000/chat
  GET  http://localhost:5000/health
==================================================
```

### Step 4 — Open the Frontend
Open `frontend/index.html` in your browser.

> **Tip:** For the best experience, use the Live Server extension in VS Code, or serve with Python:
> ```bash
> cd frontend
> python -m http.server 3000
> ```
> Then visit `http://localhost:3000`

---

## 🔌 API Reference

### `POST /chat`
Send a user message and receive a bot response.

**Request:**
```json
{
  "message": "learn python"
}
```

**Response:**
```json
{
  "response": "🐍 Python — The Language of the Future\n\n**🗺️ Beginner Roadmap:**\n..."
}
```

### `GET /health`
Check if the server is running.

**Response:**
```json
{
  "status": "ok",
  "bot": "StudyBuddy AI",
  "version": "1.0.0"
}
```

---

## 💬 Sample Interactions

| You say                | StudyBuddy responds with                         |
|------------------------|--------------------------------------------------|
| `hello`                | Friendly greeting with capabilities overview     |
| `learn python`         | Full Python roadmap + resources + YouTube links  |
| `DSA`                  | Complete DSA learning path + LeetCode tips       |
| `i'm stressed`         | Empathetic support + practical stress-busters    |
| `procrastinating`      | Science-based productivity advice                |
| `failed exam`          | Encouragement + action plan                      |
| `tell me a joke`       | One of 6 programming jokes (random)              |
| `fun fact`             | One of 6 CS fun facts (random)                   |
| `study tips`           | Pomodoro, spaced repetition, active learning     |
| `motivate me`          | Powerful motivational messages                   |
| `git`                  | Git commands cheatsheet + resources              |
| `machine learning`     | ML roadmap: maths prerequisites → scikit-learn   |

---

## 📸 Screenshots

> *(Add screenshots of your running app here)*

```
frontend/screenshots/
├── welcome-screen.png
├── chat-python.png
├── chat-dsa.png
├── mobile-view.png
└── sidebar-open.png
```

---

## 🔮 Future Improvements

- [ ] Persistent chat history (localStorage / SQLite)
- [ ] User profiles and progress tracking
- [ ] Quiz mode — test your CS knowledge
- [ ] Integration with LeetCode API for problem recommendations
- [ ] Voice input support (Web Speech API)
- [ ] PWA support — installable on mobile
- [ ] Dark / light theme toggle
- [ ] Export conversation as PDF

---

## 🧑‍💻 Architecture

```
User Types Message
       │
       ▼
  index.html / script.js
  (fetch POST /chat)
       │
       ▼
  Flask: app.py
  (receives JSON)
       │
       ▼
  chatbot.py
  preprocess_input() → find_intent()
       │
       ▼
  intents.py
  (keyword matching → random response)
       │
       ▼
  Flask returns JSON
       │
       ▼
  script.js renders bubble
  (Markdown formatting + animation)
```

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙏 Acknowledgements

Built with ❤️ as a showcase project for learning Python backend development and modern frontend design.

Resources referenced in responses:
- [python.org](https://python.org)
- [freeCodeCamp](https://freecodecamp.org)
- [NeetCode](https://neetcode.io)
- [The Odin Project](https://theodinproject.com)
- [roadmap.sh](https://roadmap.sh)
- [Andrew Ng's Courses](https://coursera.org/specializations/machine-learning-introduction)

---

*"The best time to start was yesterday; the second best time is now."* 🚀
