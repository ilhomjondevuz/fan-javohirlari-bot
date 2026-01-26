from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from filters.admins_message import AdminMessageFilter
from keyboards.default import choice_language, menu_keyboard_uz, menu_keyboard_en, menu_keyboard_ru, \
    admin_menu_keyboard_uz, admin_menu_keyboard_en, admin_menu_keyboard_ru
from loader import dp
from states.register import RegisterStatesGroup
from utils.db_api.database import db


@dp.message(CommandStart(), AdminMessageFilter())
async def admin_start(message: Message, state: FSMContext):
    user = await db.select_user(str(message.from_user.id))
    language = user.get('language', 'uz')

    if language == 'uz':
        markup = await admin_menu_keyboard_uz()
    elif language == 'en':
        markup = await admin_menu_keyboard_en()
    else:  # ru
        markup = await admin_menu_keyboard_ru()

    await message.answer(
        f"Salom, {message.from_user.full_name}",
        reply_markup=markup
    )

@dp.message(CommandStart())
async def bot_start(message: Message, state: FSMContext):
    user = await db.select_user(str(message.from_user.id))  # ✅ await
    if not user:
        await message.answer(
            f"🇺🇿 Salom, Hello, Привет {message.from_user.full_name}!\n"
            f"🇺🇿 Tilni tanlang:\n"
            f"🇬🇧 Choose your language:\n"
            f"🇷🇺 Выберите язык:",
            reply_markup=await choice_language()  # til tanlash klaviaturasi
        )

        await state.set_state(RegisterStatesGroup.lang)
        await state.set_data({
            'tg_id': str(message.from_user.id),
            'fullname': message.from_user.full_name,
        })
    else:
        language = user.get('language', 'uz')  # default 'uz'
        if language == 'uz':
            markup = await menu_keyboard_uz()
        elif language == 'en':
            markup = await menu_keyboard_en()
        else:  # ruscha
            markup = await menu_keyboard_ru()

        await message.answer(f"Salom, {message.from_user.full_name}", reply_markup=markup)

