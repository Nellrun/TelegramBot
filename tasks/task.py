import asyncio
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', handlers=[logging.StreamHandler()])

async def job():
    logging.info('Periodic task executed')

if __name__ == '__main__':
    asyncio.run(job())
