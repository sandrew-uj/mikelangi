from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

MALE="♂️"
FEMALE="♀️"

gender = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=MALE),
            KeyboardButton(text=FEMALE)
        ],
    ],
    resize_keyboard=True
)