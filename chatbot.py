"""
chatbot.py — StudyBuddy AI
============================
Pure rule-based chatbot engine.
No ML, no NLP libraries, no external AI APIs.

Architecture:
  preprocess_input()  → normalise user text
  find_intent()       → keyword matching against INTENTS
  get_bot_response()  → main public entry point
"""

import re
from intents import INTENTS, get_response


# ─────────────────────────────────────────────
# TEXT PREPROCESSING
# ─────────────────────────────────────────────

def preprocess_input(text: str) -> str:
    """
    Normalise user input for consistent matching:
      - Lowercase
      - Strip leading/trailing whitespace
      - Collapse multiple spaces
      - Remove punctuation (except hyphens within words)
    """
    text = text.lower().strip()
    text = re.sub(r"[^\w\s\-]", " ", text)   # remove punctuation
    text = re.sub(r"\s+", " ", text)          # collapse whitespace
    return text


# ─────────────────────────────────────────────
# INTENT DETECTION
# ─────────────────────────────────────────────

def find_intent(user_text: str) -> str:
    """
    Scan every intent's keyword list.
    Return the first matching intent name, or 'default'.

    Matching rules (priority order):
      1. Exact phrase match (highest priority)
      2. All words of a multi-word keyword present
      3. Single-word keyword present as a whole word
    """
    text_clean = preprocess_input(user_text)

    # ── Pass 1: exact phrase match ────────────────────────────────────────
    for intent_name, intent_data in INTENTS.items():
        if intent_name == "default":
            continue
        for keyword in intent_data["keywords"]:
            kw = keyword.lower().strip()
            if kw == text_clean:
                return intent_name

    # ── Pass 2: keyword is a sub-string / phrase contained in user text ───
    for intent_name, intent_data in INTENTS.items():
        if intent_name == "default":
            continue
        for keyword in intent_data["keywords"]:
            kw = keyword.lower().strip()
            # Use word-boundary regex for single words; direct substring for phrases
            if " " in kw:
                if kw in text_clean:
                    return intent_name
            else:
                pattern = r"\b" + re.escape(kw) + r"\b"
                if re.search(pattern, text_clean):
                    return intent_name

    return "default"


# ─────────────────────────────────────────────
# MAIN RESPONSE FUNCTION
# ─────────────────────────────────────────────

def get_bot_response(user_message: str) -> str:
    """
    Public entry point called by Flask.

    Parameters
    ----------
    user_message : str
        Raw text sent by the user.

    Returns
    -------
    str
        Bot response string (may contain markdown / emojis).
    """
    if not user_message or not user_message.strip():
        return "It looks like your message was empty! 😊 Type **help** to see what I can do."

    intent = find_intent(user_message)
    return get_response(intent)
