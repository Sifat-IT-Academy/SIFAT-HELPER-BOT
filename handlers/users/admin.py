from aiogram import types
from loader import dp, db, bot
from data.config import ADMINS  
from aiogram.filters import Command,or_f,and_f
from aiogram.fsm.context import FSMContext
from keyboards.inline import admin_keyboard,menu_buttons,inlinebuttons
from aiogram import F
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts,Form
import time
from utils.db_api.sqlite import all_groups_ids

@dp.message(Command("admin"),IsBotAdminFilter(ADMINS),F.chat.type == "private")
async def is_admin(message:types.Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)

@dp.message(and_f(F.text=="Foydalanuvchilar soni",F.chat.type == "private"),IsBotAdminFilter(ADMINS))
async def users_count(message:types.Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(and_f(F.text=="Reklama yuborish",F.chat.type == "private"),IsBotAdminFilter(ADMINS))
async def advert_dp(message:types.Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)

async def send_advert(message:types.Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.01)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()

@dp.message(and_f(F.text=="Guruhlarga xabar yuborish",F.chat.type == "private"),IsBotAdminFilter(ADMINS))
async def advert_dp_gr(message:types.Message,state:FSMContext):
    await state.set_state(Adverts.gruop)
    await message.answer(text="Guruhlarga xabar yuborishingiz mumkin !")

@dp.message(Adverts.gruop)
async def send_advert_gr(message:types.Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = all_groups_ids()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user,from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.1)
    
    await message.answer(f"xabar {count}ta guruhga yuborildi")
    await state.clear()