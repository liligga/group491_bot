from aiogram import Router, F, types
from pprint import pprint
from aiogram_widgets.pagination import TextPaginator

from bot_config import database


catalog_router = Router()

@catalog_router.callback_query(F.data == "book_catalog")
async def catalog_handler(callback: types.CallbackQuery):
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
        # получаем для каждого товара его картинку(file_id из БД)
        cover = book.get("cover")
        await callback.message.answer_photo(
            photo=cover,
            caption=f"Название: {book.get('name', 'Без названия')}\nЦена: {book.get('price')}"
        )


@catalog_router.callback_query(F.data == "book_catalog_pagination")
async def catalog_pagination_handler(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer("Наш каталог книг")
    book_list = database.get_all_books()
    pprint(book_list)

    # Списковое включение, созданное по данным из БД. 
    # из себя представляет список строк
    text_data = [
        f"Название: {book.get('name', 'Без названия')}\nЦена: {book.get('price')} сом\nАвтор: {book.get('author')}\nГод издания: {book.get('year')}" for book in book_list
    ]
    
    # per_page = сколько записей из БД показать в одном сообщении
    paginator = TextPaginator(data=text_data, router=catalog_router, per_page=1)
    # магия
    current_text_chunk, reply_markup = paginator.current_message_data

    await callback.message.answer(
        text=current_text_chunk, 
        reply_markup=reply_markup
    )