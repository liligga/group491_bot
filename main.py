import asyncio
import logging
from aiogram import Bot

from bot_config import bot, dp, database
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.other_messages import other_router
from handlers.book_catalog import catalog_router
from handlers.complaint_dialog import complaint_router
from handlers.book_management import book_admin_router


async def on_startup(bot: Bot):
    database.create_tables()


async def main():
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(catalog_router)
    dp.include_router(complaint_router)
    dp.include_router(book_admin_router)

    # в самом конце
    dp.include_router(other_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
