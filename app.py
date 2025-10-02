from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "✅ Gmail AI Server is running (stub mode)."

# Заглушка вместо реальной проверки
@app.route("/verify", methods=["POST"])
def verify():
    try:
        data = request.get_json(force=True)
        email = data.get("email")
        return jsonify({"success": True, "email": email})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
