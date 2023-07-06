from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from filters.is_private import IsPrivate
from handlers.users.profile_creating.users_image import show_image
from handlers.users.profile_creating.users_name import name_question
from loader import dp
from utils.db_api import quick_commands as db


@dp.message_handler(IsPrivate(), Command("search"))
async def my_search(message: types.Message):
    name = message.from_user.full_name
    try:
        await message.answer(f'Привет, {message.from_user.full_name}!\n')
        await db.add_user(id=message.from_user.id, name=name)
    except Exception:
        await message.answer(f'Похоже, что у тебя уже есть анкета')
        return await show_profile(message)
    await create_profile(message)