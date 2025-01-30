from aiogram import Dispatcher, types
from config import bot

async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Здраствуйте {message.from_user.first_name}!\n')

async def info_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Этот бот позволяет просматривать товары, '
                                f'их описание, цены и фото, обеспечивая быстрый и '
                                f'удобный доступ к информации.')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])