from aiogram import types
from loader import dp, db
from aiogram.filters import Command,or_f,and_f
from aiogram.fsm.context import FSMContext
from keyboards.inline import admin_keyboard,menu_buttons,inlinebuttons
from aiogram import F

@dp.message(and_f(F.text.in_(["💼 Biz haqimizda","/about"]),F.chat.type == "private"))
async def about_commands(message:types.Message, state:FSMContext):
    text = """<i><b>Sifat o‘quv markazi</b> 2023 yil 1 iyunda Karmana tumani, Arg‘un MFY faollar zali binosida o‘z faoliyatini boshlagan. Dastlab Sifat o‘quv markazida Foundation (HTML, CSS) kurslari keyin esa Frontend va Backend kurslari xam o‘quvchilar talabi asosida tashkil etildi.\nBizning o‘quv dasturlarimizga 200 dan ortiq dasturlashga qiziquvchi yoshlar jalb etilgan. Ulardan eng kichigi 10 yosh va eng kattasi 35 yosh hisoblanadi.\nSifatda  faqat ta'lim berish bilan emas dasturlar yaratish va kompaniyalar bilan faol hamkorlik qilishni ham amalga oshirmoqdamiz. 
<b>Sifatedu</b> - Online ta'lim berish
platformasi.
<b>Sifatdev</b> - Dasturchilar jamoasi
hisoblanadi.</i>\n\n<blockquote>Ilm - bu har bir yaxshilikning boshi!</blockquote>\n\n+998997501717\n+998883780808"""
    image_url = "https://i.ibb.co/1Xzr39T/sifat.png"
    await message.answer_photo(photo=image_url,caption=text,reply_markup=inlinebuttons.our_sites, parse_mode="HTML")