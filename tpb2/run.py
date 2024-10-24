import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.database.models import async_main
from app.handlers.handlers import router

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()


async def main():
    await async_main()
    load_dotenv()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
