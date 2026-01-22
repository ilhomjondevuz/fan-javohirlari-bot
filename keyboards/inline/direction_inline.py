from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.database import db

from aiogram.filters.callback_data import CallbackData


class DirectionCallback(CallbackData, prefix="direction"):
    id: int
    step: int


async def direction_menu(language: str = "uz") -> InlineKeyboardMarkup:
    directions = await db.select_directions()
    keyboard = []

    for direction in directions:
        text = direction.get(f"name_{language}", direction["name_uz"])

        keyboard.append([
            InlineKeyboardButton(
                text=text,
                callback_data=DirectionCallback(
                    id=direction["id"],
                    step=0
                ).pack()
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
