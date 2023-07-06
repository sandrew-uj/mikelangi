from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

LIKE = "❤️"
DISLIKE = "👎"
SLEEP = "💤"

like_or_not = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=LIKE),
            KeyboardButton(text=DISLIKE),
            KeyboardButton(text=SLEEP),
        ],
    ],
    resize_keyboard=True
)