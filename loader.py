from aiogram import Bot, Dispatcher, Router
from data.config import BOT_TOKEN
from aiogram.enums import ParseMode
from utils.db_api.sqlite import Database, Sertificate, AuthDatabase

router = Router()

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
db = Database('main.db')
# au = AuthDatabase('auth.db')