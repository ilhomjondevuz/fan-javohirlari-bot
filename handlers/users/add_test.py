from aiogram import F
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.inline import sciences_markup
from loader import dp
from utils.db_api import TEXTS
from utils.db_api.database import db


@dp.message(F.text.in_([TEXTS['add_test_uz'], TEXTS['add_test_en'], TEXTS['add_test_ru']]))
async def test_selection(message: Message):
    user = await db.select_user(str(message.from_user.id))
    resp_text = TEXTS["add_test_uz"]
    if user['language'] == 'uz':
        resp_text = TEXTS['add_test_uz']
    elif user['language'] == 'en':
        resp_text = TEXTS['add_test_en']
    elif user['language'] == 'ru':
        resp_text = TEXTS['add_test_ru']
    await message.answer(resp_text, parse_mode="HTML")