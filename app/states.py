from aiogram.fsm.state import StatesGroup, State


class Chatai(StatesGroup):
    text = State()
    wait = State()


class Chatgiga(StatesGroup):
    text = State()
    wait = State()