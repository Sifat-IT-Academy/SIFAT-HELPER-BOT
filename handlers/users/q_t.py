from aiogram.types import Message, CallbackQuery
from loader import dp, db, bot
from aiogram.filters import Command, or_f, and_f  # Операторы для фильтров
from aiogram.fsm.context import FSMContext  # Контекст состояния
from keyboards.inline import admin_keyboard, menu_buttons, inlinebuttons  # Импорт клавиатур
from aiogram import F  # Фильтры для обработчиков
from utils.db_api.sqlite import all_groups_ids  # Импорт функции для работы с базой данных
import tracemalloc  # Импорт модуля для отслеживания памяти
from states.reklama import Question, Sug  # Импорт состояний
from aiogram.types import InlineKeyboardButton, ReplyKeyboardRemove  # Импорт типов сообщений

# Запуск отслеживания памяти
tracemalloc.start()

# Обработчик команды "Savol va takliflar ❔"
@dp.message(F.text == "Savol va takliflar ❔")
async def sifatdev(message: Message, state: FSMContext):
    await message.answer("Savolingiz yoki taklifingiz bo'lsa murojat qiling", reply_markup=inlinebuttons.q_s)

# Обработчик callback-запроса "question"
@dp.callback_query(F.data == "question")
async def question(call: CallbackQuery, state: FSMContext):
    await call.message.delete()  # Удаление сообщения с кнопками
    await call.message.answer("Savolni yuboring", reply_markup=ReplyKeyboardRemove())  # Отправка сообщения с просьбой отправить вопрос
    await state.set_state(Question.question)  # Установка состояния "question"

# Обработчик сообщений в состоянии "question"
@dp.message(Question.question)
async def question(message: Message, state: FSMContext):
    t = message.text
    await state.update_data(question=t)  # Обновление данных состояния с вопросом
    await message.answer("Sizning savolingiz adminga yuborildi, barcha savollaringiz tez orada javob beriladi", reply_markup=ReplyKeyboardRemove())  # Подтверждение получения вопроса
    # Отправка вопроса в чат администраторам
    await bot.send_message(chat_id=-1002061183513, text=f"""
Foydalanuvchi <a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>-ning <i>savoli</i>
<b>{t}</b>
""", parse_mode="HTML")
    print(t)  # Вывод вопроса в консоль
    await state.clear()

# Обработчик callback-запроса "suggestion"
@dp.callback_query(F.data == "suggestion")
async def suggestion(call: CallbackQuery, state: FSMContext):
    await call.message.delete()  # Удаление сообщения с кнопками
    await call.message.answer("Taklifingizni yuboring", reply_markup=ReplyKeyboardRemove())  # Отправка сообщения с просьбой отправить предложение
    await state.set_state(Sug.sug)  # Установка состояния "sug"

# Обработчик сообщений в состоянии "sug"
@dp.message(Sug.sug)
async def suggestion(message: Message, state: FSMContext):
    t = message.text
    await state.update_data(sug=t)  # Обновление данных состояния с предложениемs
    await message.answer("Taklifingiz adminga yuborildi, barcha takliflaringiz tez orada javob beriladi", reply_markup=ReplyKeyboardRemove())  # Подтверждение получения предложения
    # Отправка предложения в чат администраторам
    await bot.send_message(chat_id=-1002061183513, text=f"""
Foydalanuvchi <a href="tg://user?id={message.from_user.id}">{message.from_user.full_name}</a>-ning <i>taklifi</i>
<b>{t}</b>
""", parse_mode="HTML")
    await state.clear()