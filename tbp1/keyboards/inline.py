from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="YouTube", url="http://youtu.be"),
            InlineKeyboardButton(text="Telegram", url="tg://...")
        ]
    ],
    resize_keyboard=True,
)

