from aiogram import Router, F, types
from pprint import pprint

from bot_config import database


catalog_router = Router()

@catalog_router.callback_query(F.data == "book_catalog")
async def about_us_handler(callback: types.CallbackQuery):
    # await callback.answer("Мы - магазин книг")
    await callback.answer()
    await callback.message.answer("Наш каталог книг")
    book_list = database.get_all_books()
    pprint(book_list)
    for book in book_list: 
        # ('Гарри Потер', 1998, 'Джоан Роулинг', 2333)
        # {'author': 'Джоан Роулинг',
        # 'id': 1,
        # 'name': 'Гарри Потер',
        # 'price': 2333,
        # 'year': 1998}

        await callback.message.answer(
            f"Название: {book.get('name', 'Без названия')}\nЦена: {book.get('price')}"
        )