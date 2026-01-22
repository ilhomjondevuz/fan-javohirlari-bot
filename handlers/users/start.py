from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.default import send_phone
from loader import dp
from states.register import RegisterStatesGroup
from utils.db_api.database import db


@dp.message(CommandStart())
async def bot_start(message: Message, state: FSMContext):
    user = await db.select_user(str(message.from_user.id))  # ✅ await

    if not user:
        await message.answer(
            f"Salom, {message.from_user.full_name}!,\n"
            f"Botdan foydalanish uchun ro'yxatdan o'tish uchun pastdani tugmani bosib telefon raqamingizni yuboring",
            reply_markup=await send_phone()
        )
        await state.set_state(RegisterStatesGroup.phone)
        await state.set_data({
            'tg_id': str(message.from_user.id),   # Telegram IDni string qilish
            'fullname': message.from_user.full_name,
        })
    else:
        await message.answer(f"Salom, {message.from_user.full_name}")
