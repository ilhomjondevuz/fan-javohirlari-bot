from aiogram.fsm.state import StatesGroup, State


class RegisterStatesGroup(StatesGroup):
    phone = State()
    passport = State()
