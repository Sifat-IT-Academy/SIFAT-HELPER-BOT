from aiogram import types
from loader import dp, db
from aiogram.filters import Command,or_f,and_f
from aiogram.fsm.context import FSMContext
from keyboards.inline import admin_keyboard,menu_buttons,inlinebuttons
from aiogram import F

@dp.callback_query(F.data == "itpark")
async def question(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()  # Удаление сообщения с кнопками
    image_url = "https://sifatedu.uz/static/media/certificateresident.262dec9e6e7c7f1ce160.png"
    await call.message.answer_photo(photo=image_url)

@dp.callback_query(F.data == "guvoh")
async def question(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()  # Удаление сообщения с кнопками
    image_url = "BQACAgIAAxkBAAIEeWZDYeCI20cbQwJr21iT4hyYHCE_AALkSQACwwMhSlKq2KhCNPVSNQQ"
    await call.message.answer_document(document=image_url)