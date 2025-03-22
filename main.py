
import requests
import os
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
TRADE_URL = os.getenv("TRADE_URL")

def fetch_trade_message():
    try:
        response = requests.get(TRADE_URL)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return "Failed to fetch trade message. Status code: " + str(response.status_code)
    except Exception as e:
        return "Error fetching trade message: " + str(e)

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": message}
    response = requests.post(url, data=payload)
    print("Telegram response:", response.text)

if __name__ == "__main__":
    message = fetch_trade_message()
    send_telegram_message(message)
