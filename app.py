"""
app.py — StudyBuddy AI
========================
Flask REST API server.

Endpoints:
  POST /chat       { "message": "..." } → { "response": "..." }
  GET  /health     → { "status": "ok" }
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_bot_response

# ─────────────────────────────────────────────
# APP INITIALISATION
# ─────────────────────────────────────────────

app = Flask(__name__)
CORS(app)   # Allow cross-origin requests from the frontend


# ─────────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────────

@app.route("/chat", methods=["POST"])
def chat():
    """
    Receive a user message and return the bot's response.

    Request JSON:
        { "message": "tell me about python" }

    Response JSON:
        { "response": "🐍 Python — The Language of the Future..." }
    """
    data = request.get_json(silent=True)

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field in request body."}), 400

    user_message: str = data["message"]
    bot_reply: str = get_bot_response(user_message)

    return jsonify({"response": bot_reply})


@app.route("/health", methods=["GET"])
def health():
    """Simple health-check endpoint."""
    return jsonify({"status": "ok", "bot": "StudyBuddy AI", "version": "1.0.0"})


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 50)
    print("  StudyBuddy AI Backend — Starting...")
    print("  POST http://localhost:5000/chat")
    print("  GET  http://localhost:5000/health")
    print("=" * 50)
    app.run(debug=True, host="0.0.0.0", port=5000)
