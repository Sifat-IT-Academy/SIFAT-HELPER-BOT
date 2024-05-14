from data.config import ADMINS, BOT_TOKEN
from aiogram import Bot, Dispatcher
from data.config import SERTIFICAT_CHANNEL

bot = Bot(token=BOT_TOKEN)

async def on_startup_notify():
    for admin in ADMINS:
        await bot.send_message(chat_id=SERTIFICAT_CHANNEL,text="✅Bot ishga tushirildi")

async def on_shutdown_notify():
    for admin in ADMINS:
        await bot.send_message(chat_id=SERTIFICAT_CHANNEL, text="❌Bot to'xtatildi")