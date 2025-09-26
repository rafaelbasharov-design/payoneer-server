from flask import Flask, jsonify, request

app = Flask(__name__)

# Health check (Render will ping this endpoint)
@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "ok"}), 200

# Тестовый роут (можно проверить в браузере)
@app.route("/", methods=["GET"])
def home():
    return "<h1>Payoneer Server is running!</h1>"

# Пример будущего эндпоинта для проверки оплаты
@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    # Тут потом будет логика проверки через Payoneer API
    return jsonify({"received": data}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
