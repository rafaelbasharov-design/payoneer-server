from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Маршрут проверки сервера
@app.route("/")
def home():
    return {"message": "Payoneer server is running!"}

# Маршрут для создания платежного запроса (эмуляция Payoneer API)
@app.route("/request-payment", methods=["POST"])
def request_payment():
    data = request.json
    amount = data.get("amount")
    currency = data.get("currency", "USD")
    customer_email = data.get("email")

    # ⚠️ Здесь в будущем мы подключим Payoneer API
    return jsonify({
        "status": "pending",
        "amount": amount,
        "currency": currency,
        "customer_email": customer_email,
        "payment_id": "test_12345"
    })

# Маршрут проверки статуса платежа
@app.route("/verify-payment/<payment_id>", methods=["GET"])
def verify_payment(payment_id):
    # ⚠️ Тут будет запрос в Payoneer API
    return jsonify({
        "payment_id": payment_id,
        "status": "success"  # пока фейковый успех
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
Купить нужно холодный кошелек-флешка
Скачать программу Ledger nano x(l)
Без него не сможешь оплатить