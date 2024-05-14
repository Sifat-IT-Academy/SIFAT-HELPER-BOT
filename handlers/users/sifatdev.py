from aiogram.types import Message, CallbackQuery, ContentType,ReplyKeyboardRemove
from loader import dp, db, bot, au
from aiogram.fsm.context import FSMContext
from aiogram import F
from aiogram.filters import Command,or_f,and_f
from states.reklama import Register, Login
from keyboards.inline import menu_buttons, inlinebuttons
from data.config import MILLIY_SER, SERTIFICAT_CHANNEL, CHANNELS

@dp.message(and_f(F.text.in_(["💻 Bizning kurslar"]),F.chat.type == "private"))
async def r_l(message: Message, state: FSMContext):
    await message.answer('Kursni tanlang', reply_markup=menu_buttons.crs)

@dp.message(F.text.in_(MILLIY_SER),F.chat.type == "private")
async def sifatdev(message: Message, state: FSMContext):
    await message.answer("asashd")

@dp.message(and_f(F.text == "🇺🇿 Milliy Sertifikat"),F.chat.type == "private")
async def sifatdev(message: Message, state: FSMContext):
    await message.answer(f"{message.chat.full_name}- Ro'yxatdan o'ting yoki Tizimga kiring", reply_markup=menu_buttons.r_l)

@dp.message(and_f(F.text.in_(["Ro'yxatdan o'tish","Tizimga kirish"]),F.chat.type == "private"))
async def r_l(message: Message, state: FSMContext):
    if message.text == "Ro'yxatdan o'tish":
        await message.answer('Ismingizni kiriting', reply_markup=ReplyKeyboardRemove())
        await state.set_state(Register.name)
    elif message.text == 'Tizimga kirish':
        await message.answer('Raqamingizni yuboring!', reply_markup=menu_buttons.contact_button)
        await state.set_state(Login.phone)


@dp.message(Register.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    text = f"Familyangizni kiriting!"
    await message.reply(text=text)
    await state.set_state(Register.fullname)

@dp.message(Register.fullname)
async def get_name(message: Message, state: FSMContext):
    fullname = message.text
    await state.update_data(fullname=fullname)
    text = f"Otangizni ismini kiriting!"
    await message.reply(text=text)
    await state.set_state(Register.middlename)

@dp.message(Register.middlename)
async def get_name(message: Message, state: FSMContext):
    middlename = message.text
    await state.update_data(middlename=middlename)
    text = f"Raqamingizni yuboring kiriting!"
    await message.reply(text=text, reply_markup=menu_buttons.contact_button)
    await state.set_state(Register.phone)

@dp.message(Register.phone)
async def get_name(message: Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(contact=contact)
    text = f"Parolingizni kiriting!"
    await message.reply(text=text, reply_markup=ReplyKeyboardRemove())
    await state.set_state(Register.parol)

@dp.message(Register.parol)
async def get_name(message: Message, state: FSMContext):
    parol = message.text
    await state.update_data(parol=parol)
    data = await state.get_data()
    name = data.get("name")
    fullname = data.get("fullname")
    middlename = data.get("middlename")
    contact = data.get("contact")
    parol = data.get("parol")
    text = f"""Ma'lumotlaringiz qabul qilindi!
Ism: {name}
Familya: {fullname}
Otangiz: {middlename}
Raqam: {contact}
Parol: {parol}    
"""
    await message.reply(text=text)
    await message.reply(text="Milliy sertifikatni olish uchun kursni tanlang", reply_markup=menu_buttons.MILLIY_SER)
    au.add_user(id=message.from_user.id, password=parol, phone=contact)

    await state.clear()

# @dp.message(Command("login"), F.chat.type == "private")
# async def login_start(message: Message, state: FSMContext):
#     await message.answer('Raqamingizni yuboring!', reply_markup=menu_buttons.contact_button)
#     await state.set_state(Login.phone)
    # await Login.phone.set()

@dp.message(or_f(F.text.regexp(r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"),F.contact), Login.phone)
async def login_password(message: Message, state: FSMContext):
    contact = message.contact.phone_number
    await state.update_data(phone=contact)
    await message.answer('Parolingizni kiriting!', reply_markup=ReplyKeyboardRemove())
    # await Login.parol.set()
    await state.set_state(Login.parol)

@dp.message(Login.parol)
async def process_login(message: Message, state: FSMContext):
    parol = message.text
    contact_data = await state.get_data()
    phone = contact_data.get("phone")

    if au.check(id=message.from_user.id, phone=phone, password=parol):
        await message.answer('Muvaffaqiyatli kirdingiz!')
        await message.reply(text="Milliy sertifikatni olish uchun kursni tanlang", reply_markup=menu_buttons.MILLIY_SER)
    else:
        await message.answer('Kiritilgan ma\'lumotlar noto\'g\'ri, iltimos tekshirib qayta urinib ko\'ring!')
        return

    await state.clear()

@dp.message(F.text.in_(MILLIY_SER))
async def get_tashkilot(message: Message, state: FSMContext):
    tashkilot = message.text
    await bot.send_message(chat_id=SERTIFICAT_CHANNEL, text=f"""
Foydalanuvchi ID: {message.from_user.id}
Foydalanuvchi: {message.from_user.full_name}
Kurs: {tashkilot}""")