from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def choice_language() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="🇺🇿 O'zbek tili"
                ),
                KeyboardButton(
                    text="🇬🇧 English"
                ),
                KeyboardButton(
                    text="🇷🇺 Russian"
                )
            ]
        ],
        resize_keyboard=True
    )
