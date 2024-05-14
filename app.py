from aiogram import Dispatcher
from loader import *
import middlewares, filters, handlers, asyncio
from utils.notify_admins import *
from utils.set_bot_commands import set_default_commands
from utils.db_api.sqlite import Database, Sertificate
import handlers.users.sifatdev as a

async def main():
    dp.startup.register(on_startup_notify)
    dp.shutdown.register(on_shutdown_notify)
    # dp.include_router(a.router)
    # dp.include_routers(a.router)  
    try:db.create_table_users()
    except:pass
    try:au.create_table_users()
    except:pass
    await set_default_commands(bot)
    await dp.start_polling(bot, polling_timeout=1)
    

if __name__ == '__main__':
    asyncio.run(main())