from aiogram import Router
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.types import Message

from tbp1.filters.is_admin import IsAdmin
from tbp1.filters.is_digit_or_float import CheckForDigits
from tbp1.keyboards import reply

router = Router()


@router.message(CommandStart(), IsAdmin(7192473711))
async def start(message: Message):
    await message.answer(f"Hello, {message.from_user.first_name}", reply_markup=reply.main)


@router.message(Command("pay"),CheckForDigits())
async def pay_the_order(message: Message, command: CommandObject) -> None:
    await message.answer(f"Вы успешно оплатили товар")