from aiogram import types
from loader import dp, db
from aiogram.filters import Command,or_f,and_f
from aiogram.fsm.context import FSMContext
from keyboards.inline import admin_keyboard,menu_buttons,inlinebuttons
from aiogram import F


@dp.message(and_f(F.text=="🎒 SifatEdu",F.chat.type == "private"))
async def sifatedu_handler(message:types.Message):
    await message.answer(text="SifatEdu menu",reply_markup=menu_buttons.sifatedu_button)