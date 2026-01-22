from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def menu_keyboard_uz() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="📄 O'qishga hujjat topshirish"
                ),
                KeyboardButton(
                    text="📝 Imtihon topshirish"
                )
            ],
            [
                KeyboardButton(
                    text="💬 Admin bilan bog'lanish"
                ),
                KeyboardButton(
                    text="✉️ Ma'muriyatga yozish"
                )
            ],
            [
                KeyboardButton(
                    text="📚 Universitet haqida ma'lumot"
                ),
                KeyboardButton(
                    text="🌐 Tilni o'zgartirish"
                )
            ]
        ],
        resize_keyboard=True,  # klaviaturani moslash
        one_time_keyboard=False  # doim ko'rinadigan klaviatura
    )

async def menu_keyboard_en() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="📄 Submit Documents"
                ),
                KeyboardButton(
                    text="📝 Take Exam"
                )
            ],
            [
                KeyboardButton(
                    text="💬 Contact Admin"
                ),
                KeyboardButton(
                    text="✉️ Write to Administration"
                )
            ],
            [
                KeyboardButton(
                    text="📚 About University"
                ),
                KeyboardButton(
                    text="🌐 Change Language"
                )
            ]
        ],
        resize_keyboard=True,  # klaviaturani moslash
        one_time_keyboard=False  # doim ko'rinadigan klaviatura
    )

async def menu_keyboard_ru() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="📄 Подать документы"
                ),
                KeyboardButton(
                    text="📝 Сдать экзамен"
                )
            ],
            [
                KeyboardButton(
                    text="💬 Связаться с админом"
                ),
                KeyboardButton(
                    text="✉️ Написать администрации"
                )
            ],
            [
                KeyboardButton(
                    text="📚 Информация о университете"
                ),
                KeyboardButton(
                    text="🌐 Изменить язык"
                )
            ]
        ],
        resize_keyboard=True,  # klaviaturani moslash
        one_time_keyboard=False  # doim ko'rinadigan klaviatura
    )
