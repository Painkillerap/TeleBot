from typing import Any

from aiogram.filters import BaseFilter
from aiogram.types import Message
from aiogram.filters import CommandObject

class CheckForDigits(BaseFilter):

    async def __call__(self, message: Message, **kwargs: Any) -> bool:
        command = CommandObject = kwargs.get("command")
        arg = command.args

        if arg.isnumeric() or (arg.count(".") == 1 and arg.replace(".","").isnumeric()):
            return True
        return False