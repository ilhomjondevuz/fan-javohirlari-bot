from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery


class GroupCallbackFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.message.chat.type in ("group", "supergroup")
