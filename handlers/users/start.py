from aiogram import types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from keyboards.default import send_phone
from loader import dp
from states.register import RegisterStatesGroup


@dp.message(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"Salom, {message.from_user.full_name}!,\nBotdan foydalanish uchun ro'yxatdan o'tish uchun pastdani tugmani bosib telefon raqamingizni yuboring", reply_markup=await send_phone())
    await state.set_state(RegisterStatesGroup.phone)
    await state.set_data({
        'tg_id': message.from_user.id,
        'fullname': message.from_user.full_name,
    })
