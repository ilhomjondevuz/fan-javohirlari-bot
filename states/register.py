from aiogram.fsm.state import StatesGroup, State


class RegisterStatesGroup(StatesGroup):
    lang = State()
    phone = State()
    passport = State()
