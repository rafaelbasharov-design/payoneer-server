from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Укажи свой API ключ в переменной окружения OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return "Payoneer/AI Gmail Server is running!"

@app.route("/generate-reply", methods=["POST"])
def generate_reply():
    try:
        data = request.json
        user_text = data.get("text", "")

        if not user_text:
            return jsonify({"reply": "Ошибка: пустой текст для анализа"}), 400

        # Запрос в OpenAI
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты помощник, который пишет короткие и вежливые ответы на email."},
                {"role": "user", "content": f"Вот письмо, на которое нужно ответить:\n\n{user_text}"}
            ],
            max_tokens=150,
            temperature=0.7
        )

        reply_text = completion["choices"][0]["message"]["content"].strip()

        return jsonify({"reply": reply_text})

    except Exception as e:
        return jsonify({"reply": f"Ошибка сервера: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
