from aiogram.filters import BaseFilter
from aiogram.types import Message

from data import config


class AdminMessageFilter(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if not message.from_user:
            return False
        return f'{message.from_user.id}' in config.ADMINS
