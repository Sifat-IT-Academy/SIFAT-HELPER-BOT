from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN") 
ADMINS = env.list("ADMINS")  
IP = env.str("ip") 
CHANNELS = list(map(int,env.list("CHANNELS"))) 
COURSES = ["Django for Everybody Specialization"]
MILLIY_SER = ["KURS1", "KURS2", "KURS3"]
COURSES_LINK = ["https://www.coursera.org/specializations/django"]
SERTIFICAT_CHANNEL = -1002061183513