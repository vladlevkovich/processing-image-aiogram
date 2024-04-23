from aiogram import Bot, Dispatcher
from middlewares.db_middleware import DataBaseSessionMiddleware
from db.db_connect import db
from handlers import users_handlers, bot_handlers, image_handlers
from dotenv import load_dotenv
import asyncio
import os


load_dotenv()


bot = Bot(token=os.getenv('BOT'))
dp = Dispatcher()


async def main():
    dp.update.middleware(DataBaseSessionMiddleware(session_pool=db.session))
    dp.include_router(users_handlers.router)
    dp.include_router(bot_handlers.router)
    dp.include_router(image_handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
