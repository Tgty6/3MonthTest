from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from db import main_db



class OrderFSM(StatesGroup):
    product_id = State()
    size = State()
    quantity = State()
    contact = State()
    submit = State()



