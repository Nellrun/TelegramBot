from telethon import TelegramClient, events, Button, types
from dotenv import load_dotenv
import os
import asyncio

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значений из переменных окружения
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

# Создайте нового клиента
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    # Ссылка на ваше веб-приложение
    web_app_url = os.getenv('WEB_URL')
    
    # Отправка сообщения с кнопкой
    await event.respond('Welcome! Click the button below to open the web app.', buttons=[
        [types.KeyboardButtonWebView('Open Web App', web_app_url)]
    ])

# Запуск клиента в асинхронном режиме
async def run_client():
    await client.run_until_disconnected()

if __name__ == '__main__':
    client.run_until_disconnected()
