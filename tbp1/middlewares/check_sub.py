from typing import Callable, Awaitable,Dict,Any

from aiogram import BaseMiddleware
from aiogram.types import Message


class CheckSubscription(BaseMiddleware):

    async  def __ceil__(
            self,
            handler: Callable[[Message,Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
