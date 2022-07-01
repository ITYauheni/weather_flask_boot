from flask import request
import requests
import json

import os

from app import app
from config import Config

config = Config()

def send_message(chat_id, text):
    weather_response = get_current_weather(text)
    if config.bot_token:
        url = f"https://api.telegram.org/bot{config.bot_token}/sendMessage"
        data = {"chat_id": chat_id, "text": weather_response}
        requests.post(url, data=data)


def get_current_weather(city: str):
    weather_api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={config.weather_api_token}"
    weather_response = requests.get(weather_api).json()
    if weather_response.get('main', None):
        temperature = int(weather_response['main']['temp']) - 273
        return f"It's {temperature} ℃ in {city} right now"
    else:
        return f"I don't have information about '{city}' city"


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        chat_id = request.json["message"]["chat"]["id"]
        request_text = request.json['message']['text']
        send_message(chat_id, request_text)
        print('message should posted')
    return {"ok": True}
