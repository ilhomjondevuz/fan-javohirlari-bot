from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.database import db


async def sciences_markup(lang: str = 'uz') -> InlineKeyboardMarkup | None:
    sciences = await db.select_sciences()
    if not sciences:
        return None  # Bo'sh bo'lsa, markup yo'q

    markup = InlineKeyboardMarkup()
    field_map = {'uz': 'name_uz', 'en': 'name_en', 'ru': 'name_ru'}
    field = field_map.get(lang, 'name_ru')

    for science in sciences:
        markup.add(
            InlineKeyboardButton(
                text=science[field],
                callback_data=f"science_{science['id']}"
            )
        )

    return markup
