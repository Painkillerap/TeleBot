from aiogram import Router

from aiogram.types import Message

from tbp1.keyboards import inline, reply, builders, fabrics
from tbp1.data.subloader import get_json

router = Router()


@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json("smiles.json")

    if msg == "ссылки":
        await message.answer("Вот ваши ссылки:", reply_markup=inline.links)
    elif msg == "спец. кнопки":
        await message.answer("Спец. кнопки", reply_markup=reply.spec)
    elif msg == "калькулятор":
        await message.answer("Введите выражение", reply_markup=builders.calc())
    elif msg == "смайлики":
        await message.answer(f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator())
    elif msg == "назад":
        await message.answer("Вы перешли в главное меню!", reply_markup=reply.main)
