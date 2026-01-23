from aiogram import F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.default import choice_language, menu_keyboard_uz, menu_keyboard_en, menu_keyboard_ru
from loader import dp
from states import ChangeLangStatesGroup
from utils.db_api import TEXTS
from utils.db_api.database import db


@dp.message(F.text.in_(TEXTS.values()))
async def change_language(message: Message, state: FSMContext):
    await message.answer(
        "(Tilni tanlang)(Choose a language)(Выберите язык):",
        reply_markup=await choice_language()
    )
    await state.set_state(ChangeLangStatesGroup.change_lang)

@dp.message(F.text.in_(TEXTS['languages']), StateFilter(ChangeLangStatesGroup.change_lang))
async def change_lang(message: Message, state: FSMContext):
    lang_code = 'uz'
    if message.text == "🇺🇿 O'zbek tili":
        lang_code = 'uz'
        await message.answer("Bo'limni tanlang:", reply_markup= await menu_keyboard_uz())
        await state.clear()
    elif message.text == "🇬🇧 English":
        lang_code = 'en'
        await message.answer("Choose a section:", reply_markup=await menu_keyboard_en())
        await state.clear()
    elif message.text == "🇷🇺 Russian":
        lang_code = 'ru'
        await message.answer("Выберите раздел:", reply_markup=await menu_keyboard_ru())
        await state.clear()
    else:
        await message.answer(
            "(Tillardan birini tanlang) (Выберите один из языков (Choose one of the languages)",
            reply_markup=await choice_language()
        )
        await db.change_language(message.from_user.id, lang_code)
