import os
import json

class Config:

    bot_token = ""
    weather_api_token = ""

    def __init__(self):
        if os.path.exists('tokens.json'):
            with open('tokens.json', 'rt', encoding='utf-8') as config:
                config_json = json.load(config)
                self.bot_token = config_json['bot']
                self.weather_api_token = config_json['weather']