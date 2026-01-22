from aiogram.enums import ChatType
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class PrivateMessageFilter(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return call.message.chat.type == ChatType.PRIVATE

