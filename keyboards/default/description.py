from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

description = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Оставить"),
            KeyboardButton(text="Добавить"),
            KeyboardButton(text="Не надо")
        ],
    ],
    resize_keyboard=True
)