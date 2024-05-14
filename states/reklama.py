from aiogram.fsm.state import State, StatesGroup

class Adverts(StatesGroup):
    adverts = State()
    gruop = State()
    
class Question(StatesGroup):
    question = State()

class Sug(StatesGroup):
    sug = State()

class Register(StatesGroup):
    name = State()
    fullname = State()
    middlename = State()
    phone = State()
    parol = State()

class Login(StatesGroup):
    phone = State()
    parol = State()

class Form(StatesGroup):
    first_name = State()
    last_name = State()
    middle_name = State()
    lavozim = State()
    region = State()
    tuman = State()
    JShShIR = State()
    passport_photo = State()
    course = State()
    phone_number = State()
    tashkilot = State()