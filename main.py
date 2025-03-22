
import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
TRADE_URL = os.getenv("TRADE_URL")

LAST_MSG_FILE = "last_message.txt"

def fetch_trade_message():
    try:
        response = requests.get(TRADE_URL)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Failed to fetch trade message. Status code: {response.status_code}"
    except Exception as e:
        return f"Error fetching trade message: {e}"

def get_last_message():
    if os.path.exists(LAST_MSG_FILE):
        with open(LAST_MSG_FILE, "r") as f:
            return f.read().strip()
    return ""

def set_last_message(msg):
    with open(LAST_MSG_FILE, "w") as f:
        f.write(msg.strip())

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text
    }
    requests.post(url, data=payload)

def main():
    current_message = fetch_trade_message()
    last_message = get_last_message()

    if current_message and current_message != last_message:
        send_telegram_message(current_message)
        set_last_message(current_message)
    else:
        print("No new trade message. Skipping...")

if __name__ == "__main__":
    main()
