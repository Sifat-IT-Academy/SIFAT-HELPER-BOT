from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

our_sites = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔺 Telegram",url="https://t.me/sifatedu")],
        [InlineKeyboardButton(text="🔺 Instagram",url="https://www.instagram.com/sifatedu_navoi")],
        [InlineKeyboardButton(text="👨🏻‍💻 IT PARK REZIDENTI", callback_data='itpark')],
        [InlineKeyboardButton(text="🗒 FIRMA GUVOHNOMASI", callback_data='guvoh')],
        # [InlineKeyboardButton(text="🔺 Youtube",url="https://www.instagram.com/sifatedu_navoi")],

    ]
)

q_s = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❓ Savol", callback_data="question"),
            InlineKeyboardButton(text="🙋🏻‍♂️ Taklif", callback_data="suggestion")
        ]
    ]
)

log_reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ro'yxatdan o'tish", callback_data="reg"),
            InlineKeyboardButton(text="Tizimga kirish", callback_data="log")
        ]
    ]
)