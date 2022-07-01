from flask import request
import requests

import os

from app import app


def send_message(chat_id, text):
    method = "SendMessage"
    token = ""
    if os.path.exists('telegram_bot_token.txt'):
        with open('telegram_bot_token.txt', 'rt', encoding='utf-8') as token:
            token = token.read()
    if token:
        url = f"https://api.telegram.org/bot{token}/{method}"
        data = {"chat_id": chat_id, "text": text}
        requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        chat_id = request.json["message"]["chat"]["id"]
        request_text = request.json['message']['text']
        send_message(chat_id, request_text[::-1])
    return {"ok": True}
