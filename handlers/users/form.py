from aiogram.types import Message
from loader import dp, db, bot
from data.config import ADMINS, COURSES, SERTIFICAT_CHANNEL
from aiogram.filters import Command,or_f,and_f
from aiogram.fsm.context import FSMContext
from keyboards.inline import admin_keyboard,menu_buttons,inlinebuttons
from aiogram import F
from filters.admin import IsBotAdminFilter
from states.reklama import Adverts,Form
import time
from utils.db_api.sqlite import all_groups_ids
from aiogram.types import Message,InlineKeyboardButton,ReplyKeyboardRemove
from utils.db_api.sqlite import Sertificate
import tracemalloc

tracemalloc.start()


@dp.message(and_f(F.text == "🗞 Xalqaro IT sertifikat"),F.chat.type == "private")
async def command_first_name_handler(message: Message,state:FSMContext) -> None:
    await state.set_state(Form.first_name)
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum, {full_name} ro'yhatdan o'tish uchun ismingizni kiriting!"
    await message.reply(text=text,reply_markup=ReplyKeyboardRemove())

@dp.message(Form.first_name,F.text.func(lambda text: text.isalpha() and len(text)>=5))
async def get_first_name(message:Message,state:FSMContext): 
     first_name = message.text
     await state.update_data(first_name=first_name)

     await state.set_state(Form.last_name)
     text = f"Familyangizni kiriting!"
     await message.reply(text=text)

@dp.message(Form.first_name)
async def not_get_first_name(message:Message,state:FSMContext):
    text = f"Iltimos ismingizni kiriting!"
    await message.reply(text=text)  


@dp.message(Form.last_name,F.text.func(lambda text: text.isalpha() and len(text)>=5))
async def get_last_name(message:Message,state:FSMContext):
     
     last_name = message.text
     await state.update_data(last_name=last_name)

     await state.set_state(Form.middle_name)
     text = f"Otangizni ismini kiriting!"
     await message.reply(text=text) 

@dp.message(Form.last_name)
async def not_get_last_name(message:Message,state:FSMContext):
    text = f"Iltimos familiyangizni yuboring!"
    await message.reply(text=text)    

@dp.message(Form.middle_name,F.text)
async def get_middle_name(message:Message,state:FSMContext):

    middle_name = message.text
    await state.update_data(middle_name=middle_name)
    await state.set_state(Form.lavozim)
    text = f"Lavozimingizni kiriting"
    await message.reply(text=text)

@dp.message(Form.middle_name)
async def not_get_middle_name(message:Message,state:FSMContext):
    text = f"Iltimos otangizni ismini kiriting!"
    await message.reply(text=text)

@dp.message(Form.lavozim,F.text)
async def get_middle_name(message:Message,state:FSMContext):

    lavozim = message.text
    await state.update_data(lavozim=lavozim)
    await state.set_state(Form.region)
    text = f"Yashash viloyatingizni yozing!"
    await message.reply(text=text)

@dp.message(Form.lavozim)
async def not_get_middle_name(message:Message,state:FSMContext):
    text = f"Iltimos, Otangizning lavozimini kiriting!"
    await message.reply(text=text)

@dp.message(Form.region,F.text)
async def get_middle_name(message:Message,state:FSMContext):

    region = message.text
    await state.update_data(region=region)
    await state.set_state(Form.tuman)
    text = f"Yashash tumaningizni yozing!"
    await message.reply(text=text)

@dp.message(Form.region)
async def not_get_middle_name(message:Message,state:FSMContext):
    text = f"Iltimos, Yashash viloyatingizni yozing!"
    await message.reply(text=text)

@dp.message(Form.tuman,F.text)
async def get_middle_name(message:Message,state:FSMContext):

    region = message.text
    await state.update_data(region=region)
    await state.set_state(Form.JShShIR)
    text = f"Pasportdagi JShShIR-ni kiritng!"
    await message.reply(text=text)

@dp.message(Form.tuman)
async def not_get_middle_name(message:Message,state:FSMContext):
    text = f"Iltimos, Yashash tumaningizni yozing!"
    await message.reply(text=text)

@dp.message(Form.JShShIR,F.text.func(lambda text: text.isdigit() and len(text)==14))
async def get_middle_name(message:Message,state:FSMContext):

    JShShIR = message.text
    await state.update_data(JShShIR=JShShIR)
    await state.set_state(Form.passport_photo)
    text = f"Pasportdagi rasmini yuboring!"
    await message.reply(text=text)

@dp.message(Form.JShShIR)
async def not_get_middle_name(message:Message,state:FSMContext):
    text = f"Iltimos, JShShIR yozing!"
    await message.reply(text=text)

@dp.message(Form.passport_photo,F.photo)
async def get_passport_photo(message:Message,state:FSMContext):

    passport_photo = message.photo[-1].file_id 
    await state.update_data(passport_photo=passport_photo)
    await state.set_state(Form.course)
    text = f"Kursni tanlang!"
    await message.reply(text=text, reply_markup=menu_buttons.course_markup)

@dp.message(Form.passport_photo)
async def not_get_passport_photo(message:Message,state:FSMContext):
    text = f"Iltimos pasport rasmini yuboring!"
    await message.reply(text=text)  

@dp.message(Form.course,F.text.in_(COURSES))
async def get_course(message:Message,state:FSMContext):
    course = message.text
    await state.update_data(course=course)
    await state.set_state(Form.phone_number)
    text = f"Telefon nomeringizni kiriting!"
    await message.reply(text=text,reply_markup=menu_buttons.contact_button)

@dp.message(Form.course)
async def not_get_region(message:Message,state:FSMContext):
    text = f"Kurslardan birini tanlang!"
    await message.reply(text=text,reply_markup=menu_buttons.course_markup)


@dp.message(or_f(F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"),F.contact),Form.phone_number)
async def set_phone_number(message:Message,state:FSMContext):
    phone_number = message.contact.phone_number if message.contact else message.text
    
    await state.update_data(phone_number=phone_number)
    await state.set_state(Form.tashkilot)
    text = f"O'qish turini tanlang!"
    await message.reply(text=text,reply_markup=menu_buttons.tashkilot_button)


@dp.message(Form.phone_number)
async def not_get_middle_name(message:Message,state:FSMContext):
    text = f"Iltimos telefon raqamingizni to'g'ri kiriting!"
    await message.reply(text=text,reply_markup=menu_buttons.contact_button)


@dp.message(Form.tashkilot,F.text.in_(["💼 Tashkilot hisobidan o'qish","👨🏻‍🎓 O'z hisobimdan o'qish"]))
async def get_tash_course(message:Message,state:FSMContext):
    tashkilot_course = message.text
    telegram_id = message.from_user.id
    data = await state.get_data()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    middle_name = data.get("middle_name")
    passport_photo = data.get("passport_photo")
    region = data.get("region")
    lavozim = data.get("lavozim")
    tuman = data.get("tuman")
    JShShIR = data.get("JShShIR")
    course = data.get("course")
    phone_number = data.get("phone_number")
    fish = last_name +" "+ first_name + " " + middle_name
    text = f"FISH: <a href='tg://user?id={telegram_id}'>{fish}</a>\nRegion: {region}\ncourse: {course}\nTel: {phone_number}\n"
    response = Sertificate.create_certificate(first_name=first_name,last_name=last_name,middle_name=middle_name,lavozim=lavozim,region=region,tuman=tuman,JShShIR=JShShIR, phone_number=phone_number,course=course,telegram_id=str(telegram_id), position="Yo'q")
    if tashkilot_course=='💼 Tashkilot hisobidan o\'qish':
        await message.answer_document(document='BQACAgIAAxkBAAIE5WZDZTzQZ4WUD9lY7AABYL4bUvmnugACe0oAAtZF2UmhDteCSk332jUE')
    elif tashkilot_course=='👨🏻‍🎓 O\'z hisobimdan o\'qish':
         await message.answer_document(document='BQACAgIAAxkBAAIE52ZDZVOsM1c5y1-fDHVzCJdyikvQAAJlQAACZu2BSbyThrai6tr5NQQ')


    if response=="Muvaffaqiyatli ro'yhatdan o'tdingiz":    
        await bot.send_photo(chat_id=SERTIFICAT_CHANNEL,photo=passport_photo,caption=text)    
        text = f"Arizangiz qabul qilindi. Tez orada siz bilan bog'lanamiz"
        await message.reply(text=text)
    await message.answer(response, reply_markup=menu_buttons.main_button)
    await state.clear()

@dp.message(Form.tashkilot)
async def not_get_tash_name(message:Message,state:FSMContext):
    text = f"O'qish turini tanlang!"
    await message.reply(text=text,reply_markup=menu_buttons.tashkilot_button)


# @dp.message(F.chat.type == "private")
# async def not_get_middle_name(message:Message,state:FSMContext):
#     text = f"Boshqa bo'limlar tez orada ishga tushadi!"
#     await message.reply(text=text,reply_markup=menu_buttons.main_button)