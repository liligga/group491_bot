from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from database import Database
from bot_config import database


book_admin_router = Router()
book_admin_router.message.filter(
    F.from_user.id == 243154734
)


class Book(StatesGroup):
    name = State()
    year = State()
    author = State()
    price = State()

@book_admin_router.message(Command("newbook"))
async def new_book(message: types.Message, state: FSMContext):
    await message.answer("Введите название книги")
    message.from_user.id
    await state.set_state(Book.name)

@book_admin_router.message(Book.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите год издания книги")
    await state.set_state(Book.year)

@book_admin_router.message(Book.year)
async def process_year(message: types.Message, state: FSMContext):
    year = message.text
    if not year.isdigit():
        await message.answer("Вводите только цифры")
        return
    year = int(year)
    if year < 0 or year > 2025:
        await message.answer("Вводите только действительный год издания")
        return
    await state.update_data(year=message.text)
    await message.answer("Введите автора книги")
    await state.set_state(Book.author)

@book_admin_router.message(Book.author)
async def process_author(message: types.Message, state: FSMContext):
    await state.update_data(author=message.text)
    await message.answer("Введите цену книги")
    await state.set_state(Book.price)

@book_admin_router.message(Book.price)
async def process_price(message: types.Message, state: FSMContext):
    price = message.text # "123.8"
    if not price.isdigit():
        await message.answer("Вводите только цифры")
        return
    price = int(price)
    if price <= 0:
        await message.answer("Вводите только положительную цену")
        return
    await state.update_data(price=price)
    await message.answer("Спасибо, книга была сохранена")
    data = await state.get_data()
    print(data)
    database.save_book(data)
    await state.clear()
