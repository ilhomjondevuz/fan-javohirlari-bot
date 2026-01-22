import re

from aiogram import types, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from app import db
from loader import dp
from states.register import RegisterStatesGroup


@dp.message(lambda message: message.text == 'hello')
async def send_hello(msg: types.Message):
    await msg.answer("Va alaykum salom")

@dp.message(F.contact, StateFilter(RegisterStatesGroup.phone))
async def send_phone(msg: Message, state: FSMContext):
    await state.update_data(phone=str(msg.contact.phone_number), username=msg.from_user.username)
    await msg.answer("Endi passport seriaingizni yuboring", reply_markup=ReplyKeyboardRemove())
    await state.set_state(RegisterStatesGroup.passport)

@dp.message(StateFilter(RegisterStatesGroup.passport), F.text)
async def send_passport(msg: Message, state: FSMContext):
    if re.match(r"^[A-Z]{2}\d{7}$", msg.text) or re.match(r"^[a-z]{2}[0-9]{7}$", msg.text):
        passport = msg.text.upper()
        await state.update_data(passport=passport)
        data = await state.get_data()
        print(data)
        await db.insert_user(**data)
        await msg.answer(f"Siz muvaffaqiyatli ro'yxatdan o'tdingiz")
        await state.clear()
        return None
    else:
        await msg.answer(f"Xato qayta kiriting:")
        return None
