from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

from data import config


class AdminCallbackFilter(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return callback.from_user.id in config.ADMINS
