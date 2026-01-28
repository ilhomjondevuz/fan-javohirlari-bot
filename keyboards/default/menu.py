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

async def admin_menu_keyboard_uz() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👥 Barcha o'quvchilar"),
                KeyboardButton(text="➕📝 Test qo'shish")
            ],
            [
                KeyboardButton(text="🎓 Ta'lim yo'nalishlari"),
                KeyboardButton(text="💰 Kontrakt narxlari")
            ],
            [
                KeyboardButton(text="📝 Imtihon qo'shish"),
                KeyboardButton(text="🧪 Testlar bo'limi")
            ]
        ],
        resize_keyboard=True
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

async def admin_menu_keyboard_en() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👥 All students"),
                KeyboardButton(text="➕📝 Add test")
            ],
            [
                KeyboardButton(text="🎓 Education fields"),
                KeyboardButton(text="💰 Contract prices")
            ],
            [
                KeyboardButton(text="📝 Add exam"),
                KeyboardButton(text="🧪 Test Section")
            ]
        ],
        resize_keyboard=True
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

async def admin_menu_keyboard_ru() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👥 Все ученики"),
                KeyboardButton(text="➕📝 Добавить тест")
            ],
            [
                KeyboardButton(text="🎓 Направления обучения"),
                KeyboardButton(text="💰 Стоимость контрактов")
            ],
            [
                KeyboardButton(text="📝 Добавить экзамен"),
                KeyboardButton(text="🧪 Раздел тестов")
            ]
        ],
        resize_keyboard=True
    )

