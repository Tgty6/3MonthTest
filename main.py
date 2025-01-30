from aiogram import executor
import logging
from config import bot, Admins, dp
from handlers import (commands, store_fsm, send_products)
from buttons import start
from db import main_db

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='Бот включен!', reply_markup=start)

    await main_db.create_db()


commands.register_handlers(dp)

store_fsm.register_handlers_store(dp)

send_products.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)