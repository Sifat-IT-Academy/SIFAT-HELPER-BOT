from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from data.config import COURSES, MILLIY_SER
main_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🎒 SifatEdu"),
        ],
        [
            KeyboardButton(text="💼 Biz haqimizda"),
        
        ],
        [KeyboardButton(text="Savol va takliflar ❔"),]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

sifatedu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🗞 Xalqaro IT sertifikat"),
            KeyboardButton(text="🇺🇿 Milliy Sertifikat"),

        ],
        [
            KeyboardButton(text="📃 Mening sertifikatlarim"),
            KeyboardButton(text="💻 Bizning kurslar"),
        ],
        [KeyboardButton(text="🔴 Asosiy menuga qaytish"),
        ],
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

asos = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔴 Asosiy menuga qaytish"),
        ],  
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

r_l = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ro'yxatdan o'tish"),
            KeyboardButton(text="Tizimga kirish"),
        ]        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

course_button = ReplyKeyboardBuilder()

for i in COURSES:
    course_button.add(KeyboardButton(text=i))
course_button.adjust(2)
course_markup = course_button.as_markup(input_field_placeholder="Kursni tanlang",resize_keyboard=True)

milly_button = ReplyKeyboardBuilder()

for i in MILLIY_SER:
    milly_button.add(KeyboardButton(text=i))
milly_button.adjust(2)
crs = milly_button.as_markup(input_field_placeholder="Kursni tanlang",resize_keyboard=True)

contact_button = ReplyKeyboardMarkup(
    keyboard=[[
    KeyboardButton(text="Kontakt yuborish", request_contact=True),]],
    resize_keyboard=True,
    input_field_placeholder="Kontakt yuborish tugmasini bosing"
)

tashkilot_button = ReplyKeyboardMarkup(
    keyboard=[[
    KeyboardButton(text="💼 Tashkilot hisobidan o'qish"),
        KeyboardButton(text="👨🏻‍🎓 O'z hisobimdan o'qish"),

    ]
    
    ],
    resize_keyboard=True,
    input_field_placeholder="Kontakt yuborish tugmasini bosing"
)