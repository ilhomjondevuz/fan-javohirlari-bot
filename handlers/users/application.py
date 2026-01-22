from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from keyboards.inline.direction_inline import direction_menu
from loader import dp
from states import ApplicationStatesGroup
from utils.db_api.database import db


@dp.message(F.text == "📄 O'qishga hujjat topshirish")
async def application(message: Message, state: FSMContext):
    await message.answer("Isn-familiyangizni to'liq kiriting:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(ApplicationStatesGroup.fullname)

@dp.message(StateFilter(ApplicationStatesGroup.fullname), F.text)
async def set_fullname(message: Message, state: FSMContext):
    await state.set_data({
        "fullname": message.text
    })
    await message.answer("Endi tug'ilgan yilingizni yuboring")
    await state.set_state(ApplicationStatesGroup.birthdate)

@dp.message(StateFilter(ApplicationStatesGroup.birthdate), F.text)
async def set_birthdate(message: Message, state: FSMContext):
    data = await state.get_data()
    year = int(message.text)
    user = await db.select_user(str(message.from_user.id))  # ✅ await
    if 990 <= year <= 2008:
        await state.update_data(year=year)
        await message.answer("Qaysi yo'nalishga topshirasiz", reply_markup=await direction_menu(data.get(user.get('language'))))
    else:
        await message.answer("‼️ Tu'gilgan yilingiz xato. Qayta yuboring")
        return
    await state.set_state(ApplicationStatesGroup.direction)

# @dp.callback_query(StateFilter(ApplicationStatesGroup.direction))
# async def set_direction(call: CallbackQuery, state: FSMContext):

