from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from filters.is_private import IsPrivate
from handlers.users.profile_creating.users_image import show_image
from handlers.users.profile_creating.users_name import name_question
from loader import dp
from utils.db_api import quick_commands as db


@dp.message_handler(IsPrivate(), Command("profile"))
async def my_profile(message: types.Message):
    name = message.from_user.full_name
    try:
        await message.answer(f'Привет, {message.from_user.full_name}!\n')
        await db.add_user(id=message.from_user.id, name=name)
    except Exception:
        await message.answer(f'Похоже, что у тебя уже есть анкета')
        return await show_profile(message)
    await create_profile(message)


async def create_profile(message: types.Message):
    await message.answer('Давайте начнем заполнять анкету')
    await name_question(message)


@dp.message_handler(Command("show_profile"))
async def show_profile(message: types.Message):
    try:
        user = await db.select_user(id=message.from_user.id)
    except Exception:
        return await message.answer('Сначала необходимо создать анкету, для этого воспользуйтесь /profile')

    if user.image:
        await show_image(user, message)
    await message.answer(f"{user.name}, {user.age}\n" +
                         (f"{user.description}" if user.description else ""))
    await message.answer("Хотите изменить анкету? (/edit_profile)")


@dp.message_handler(Command("edit_profile"))
async def edit_profile(message: types.Message):
    await name_question(message)
