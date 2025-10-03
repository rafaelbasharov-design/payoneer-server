from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# 🔑 Добавь сюда свой OpenAI API ключ (или используй Render → Environment Variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "AI Gmail Server is running 🚀"

@app.route("/generate-reply", methods=["POST"])
def generate_reply():
    try:
        data = request.json
        email_text = data.get("email_text", "")

        if not email_text:
            return jsonify({"error": "No email text provided"}), 400

        # Запрос к OpenAI (GPT-3.5 / GPT-4)
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Напиши вежливый ответ на это письмо:\n\n{email_text}\n\nОтвет:",
            max_tokens=150,
            temperature=0.7
        )

        ai_reply = response.choices[0].text.strip()
        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
