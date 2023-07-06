from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gender = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="♂️"),
            KeyboardButton(text="♀️")
        ],
    ],
    resize_keyboard=True
)