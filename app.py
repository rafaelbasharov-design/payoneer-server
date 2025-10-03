import os
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Берем ключ из переменных окружения Render
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    return "✅ Payoneer/Gmail AI Server is running!"

@app.route("/generate-reply", methods=["POST"])
def generate_reply():
    try:
        data = request.json
        email_text = data.get("email_text", "")

        if not email_text.strip():
            return jsonify({"error": "Email text is empty"}), 400

        # Генерация ответа
        completion = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Ты — помощник, который помогает писать вежливые email-ответы."},
                {"role": "user", "content": email_text}
            ],
            max_tokens=150
        )

        reply = completion.choices[0].message.content.strip()

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
