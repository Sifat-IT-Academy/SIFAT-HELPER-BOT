from aiogram.types import Message
from loader import dp, db, bot
from aiogram.filters import and_f
from keyboards.inline import menu_buttons
from aiogram import F
from data.config import SERTIFICAT_CHANNEL

@dp.message(and_f(F.text.in_(["🔴 Asosiy menuga qaytish","/start"])))
async def start_command(message:Message):
    user_info = await bot.get_chat(message.from_user.id)
    try:
        await message.answer(text="Assalomu alaykum, botimizga hush kelibsiz",reply_markup=menu_buttons.main_button)
        await bot.send_message(chat_id=SERTIFICAT_CHANNEL , text=f"""
🆕 Yangi foydalanuvchi!
🆔 Foydalanuvchi ID: {message.from_user.id}
📛 Foydalanuvchi: {message.from_user.full_name}  
📍 Foydalanuvchining BIO-si: {user_info.bio}
➖➖➖➖➖➖➖➖➖➖➖
🖐Jami: {db.count_users()[0]}""", parse_mode="HTML")
    except:
        await message.answer(text="Asosiy menu",reply_markup=menu_buttons.main_button)


@dp.message(F.new_chat_member)
async def new_member(message:Message):
    user = message.new_chat_member.get("first_name")
    await message.answer(f"{user} Guruhga xush kelibsiz!")
    try:
        await message.delete()
    except:
        pass

@dp.message(F.left_chat_member)
async def new_member(message:Message):
    # print(message.new_chat_member)
    user = message.left_chat_member.full_name
    await message.answer(f"{user} Xayr!")
    try:
        await message.delete()
    except:
        pass

@dp.message(F.document)
async def start(message:Message):
    docu = message.document.file_id
    await message.answer(f'{docu}')