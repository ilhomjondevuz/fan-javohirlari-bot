from aiogram import F
from aiogram.types import Message

from filters.admins_message import AdminMessageFilter
from loader import dp
from utils import export_users_to_excel
from utils.db_api import TEXTS
from utils.db_api.database import db


from aiogram.types import FSInputFile

@dp.message(
    AdminMessageFilter(),
    F.text.in_([
        TEXTS['admin_menu_users_uz'],
        TEXTS['admin_menu_users_en'],
        TEXTS['admin_menu_users_ru']
    ])
)
async def admin_menu_users(message: Message):
    users = await db.select_users()
    users_file_path = await export_users_to_excel(users)

    document = FSInputFile(users_file_path)
    await message.answer_document(document)

