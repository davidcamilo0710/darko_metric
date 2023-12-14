import os
import requests

token = os.environ["BOT_TOKEN"]
chat_id = os.environ["TELEGRAM_CHANEL_ID"]

url = f"https://api.telegram.org/bot{token}/sendMessage"
texto_mensaje = "Hola, esta es una prueba desde Python."

params = {
    'chat_id': chat_id,
    'text': texto_mensaje
}
response = requests.post(url, params=params)

print(response.json())
