from flask import Flask, request
import os

app = Flask(__name__)

VERIFY_TOKEN = "my_secret_token_123"  # Укажи этот токен в Facebook Webhook

@app.route("/", methods=["GET"])
def verify():
    """Функция для подтверждения Webhook в Facebook"""
    token_sent = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    if token_sent == VERIFY_TOKEN:
        return challenge
    return "Forbidden", 403


@app.route("/webhook", methods=["POST"])
def webhook():
    """Получение сообщений от WhatsApp API"""
    data = request.json
    if data:
        print("Получены данные:", data)

        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                message = change.get("value", {}).get("messages", [{}])[0]
                if message:
                    sender = message.get("from")
                    text = message.get("text", {}).get("body", "").lower()

                    # Ответ на "Привет" и "Пока"
                    if "привет" in text:
                        send_whatsapp_message(sender, "Привет! Как я могу помочь?")
                    elif "пока" in text:
                        send_whatsapp_message(sender, "До свидания!")
                    else:
                        send_whatsapp_message(sender, "Я не понимаю ваше сообщение.")

    return "EVENT_RECEIVED", 200


def send_whatsapp_message(recipient_id, text):
    """Функция отправки сообщений через WhatsApp API"""
    import requests
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",  # Укажи токен Facebook API
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": recipient_id,
        "text": {"body": text}
    }
    response = requests.post("https://graph.facebook.com/v18.0/YOUR_PHONE_ID/messages", json=data, headers=headers)
    print("Ответ от WhatsApp API:", response.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)