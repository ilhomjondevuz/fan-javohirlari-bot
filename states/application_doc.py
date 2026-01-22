from aiogram.fsm.state import StatesGroup, State


class ApplicationStatesGroup(StatesGroup):
    fullname = State()
    birthdate = State()
    direction = State()
