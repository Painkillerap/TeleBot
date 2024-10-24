from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import app.database.request as rq
import app.keyboards.inline as inline
import app.keyboards.reply as reply

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.set_user(message.from_user.id)
    await message.reply(f"Добро пожаловать в магазин кроccовок!", reply_markup=reply.main)


@router.message(F.text == 'Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=await inline.categories())


@router.callback_query(F.data.startswith('category_'))
async def category(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Выберите товар по категории',
                                  reply_markup=await inline.items(callback.data.split('_')[1]))


@router.callback_query(F.data.startswith('item_'))
async def item(callback: CallbackQuery):
    item_data = await rq.get_item(callback.data.split('_')[1])
    await callback.answer('Вы выбрали товар')
    await callback.message.answer(
        f'Название: {item_data.name}\nОписание: {item_data.description}\nЦена: {item_data.price}$',
        reply_markup=await inline.items(callback.data.split('_')[1]))
