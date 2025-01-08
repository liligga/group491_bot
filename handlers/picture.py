from aiogram import Router, types
from aiogram.filters import Command

picture_router = Router()


@picture_router.message(Command("picture"))
async def send_picture_handler(message: types.Message):
    cat_image = types.FSInputFile("images/cat.jpg")
    await message.answer_photo(
        photo=cat_image,
        caption="Умный кот"
    )