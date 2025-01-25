from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    # message.from_user.id
    # await message.answer(f"Привет, {name}")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш сайт", url="https://geeks.kg"),
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://instagram.com")
            ],
            [
                types.InlineKeyboardButton(
                    text="О нас", callback_data="about_us"
                )
            ],
            [
                types.InlineKeyboardButton(text="Каталог", callback_data="book_catalog")
            ],
            [
                types.InlineKeyboardButton(text="Каталог с пагинацией", callback_data="book_catalog_pagination")
            ]
        ]
    )
    await message.answer(f"Привет, {name}", reply_markup=kb)


@start_router.callback_query(F.data == "about_us")
async def about_us_handler(callback: types.CallbackQuery):
    # await callback.answer("Мы - магазин книг")
    await callback.answer()
    await callback.message.answer("Мы - магазин книг")