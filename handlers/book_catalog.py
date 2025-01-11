from aiogram import Router, F, types


catalog_router = Router()

@catalog_router.callback_query(F.data == "book_catalog")
async def about_us_handler(callback: types.CallbackQuery):
    # await callback.answer("Мы - магазин книг")
    await callback.answer()
    await callback.message.answer("Наш каталог книг")