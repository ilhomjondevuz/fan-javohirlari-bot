from aiogram import F
from aiogram.types import Message

from filters.admins_message import AdminMessageFilter
from loader import dp
from utils import export_users_to_excel
from utils.db_api import TEXTS
from utils.db_api.database import db


@dp.message(AdminMessageFilter(), F.text in [TEXTS['admin_menu_users_uz'], TEXTS['admin_menu_users_en'], TEXTS['admin_menu_users_ru']])
async def admin_menu_users(message: Message):
    users = await db.select_users()
    users_file = export_users_to_excel(users)
    print(users_file)