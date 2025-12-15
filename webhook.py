from flask import Flask, request
from yookassa import Configuration
import telegram
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
SHOP_ID = os.getenv("SHOP_ID")
SECRET_KEY = os.getenv("SECRET_KEY")

print("DEBUG BOT_TOKEN =", repr(BOT_TOKEN))

bot = telegram.Bot(token=BOT_TOKEN)

Configuration.account_id = SHOP_ID
Configuration.secret_key = SECRET_KEY

@app.route("/yookassa-webhook", methods=["POST"])
def yookassa_webhook():
    data = request.json
    status = data["object"]["status"]
    description = data["object"]["description"]
    chat_id = description.split()[-1]

    if status == "succeeded":
        bot.send_message(chat_id=chat_id, text="✅ Оплата прошла успешно! Доступ открыт.")

    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
