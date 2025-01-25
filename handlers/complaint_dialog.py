from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state

from database import Database
from bot_config import database


complaint_router = Router()

class Complaint(StatesGroup):
    name = State()
    age = State()
    complaint = State()


@complaint_router.message(Command("stop"))
@complaint_router.message(F.text == "стоп")
async def stop_dialog(message: types.Message, state: FSMContext):
    await message.answer("Диалог остановлен")
    await state.clear()


@complaint_router.message(Command("complaint"), default_state)
async def start_complaint(message: types.Message, state: FSMContext):
    await message.answer("Оставьте жалобу ответив на несколько вопросов. Можете остановить диалог с ботом введя '/stop' или 'стоп'")
    await message.answer("Как Вас зовут?")
    await state.set_state(Complaint.name)


@complaint_router.message(Complaint.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=message.text)
    await message.answer("Сколько Вам лет?")
    await state.set_state(Complaint.age)


@complaint_router.message(Complaint.age)
async def process_age(message: types.Message, state: FSMContext):
    age = message.text
    await state.update_data(age=age)
    await message.answer("Напишите Вашу жалобу")
    await state.set_state(Complaint.complaint)


@complaint_router.message(Complaint.complaint)
async def process_message(
    message: types.Message, 
    state: FSMContext, 
    # database: Database,
):
    complaint = message.text
    await state.update_data(complaint=complaint)
    await message.answer("Спасибо")
    data = await state.get_data()
    # здесь будет сохранение в БД
    print(data) # {'name': 'gdfd', 'age': '12', 'complaint': 'fsdfdsfdsf'}
    database.save_complaint(data)
    await state.clear()