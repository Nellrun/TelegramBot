from telethon import TelegramClient, events, Button
import asyncio

# Введите свои api_id и api_hash
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
bot_token = 'YOUR_BOT_TOKEN'

# Создайте нового клиента
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    # Ссылка на ваше веб-приложение
    web_app_url = 'http://127.0.0.1:8000/'
    
    # Отправка сообщения с кнопкой
    await event.respond('Welcome! Click the button below to open the web app.', buttons=[
        [Button.url('Open Web App', web_app_url)]
    ])

# Запуск клиента в асинхронном режиме
async def run_client():
    await client.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(run_client())
    client.start()
