from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


admin_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            
            KeyboardButton(text="Reklama yuborish"),
            KeyboardButton(text="Guruhlarga xabar yuborish"),
        ],
        [KeyboardButton(text="Foydalanuvchilar soni"),]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)