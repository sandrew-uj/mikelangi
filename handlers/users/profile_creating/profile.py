from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from filters.is_private import IsPrivate
from handlers.users.profile_creating.users_image import show_image
from handlers.users.profile_creating.users_name import name_question
from loader import dp, bot
from utils.db_api import quick_commands as db


@dp.message_handler(IsPrivate(), Command("profile"))
async def my_profile(message: types.Message):
    name = message.from_user.full_name
    try:
        await message.answer(f'Привет, {message.from_user.full_name}!\n')
        await db.add_user(id=message.from_user.id, name=name)
    except Exception:
        await message.answer(f'Похоже, что у тебя уже есть анкета')
        user_id = message.from_user.id
        await show_profile(profile_owner_id=user_id, receiver_id=user_id)
        return await message.answer("Хотите изменить анкету? (/edit_profile)")
    await create_profile(message)


async def create_profile(message: types.Message):
    await message.answer('Давайте начнем заполнять анкету')
    await name_question(message)


@dp.message_handler(Command("show_profile"))
async def show_profile(profile_owner_id, receiver_id, reply_markup=None):
    try:
        profile_owner = await db.select_user(id=profile_owner_id)
        receiver = await db.select_user(id=receiver_id)
    except Exception:
        return await bot.send_message(profile_owner_id, 'Сначала необходимо создать анкету, для этого воспользуйтесь '
                                                        '/profile')

    if profile_owner.image:
        await show_image(profile_owner=profile_owner, receiver=receiver,
                         caption=f"{profile_owner.name}, {profile_owner.age}\n" +
                                 (f"{profile_owner.description}" if profile_owner.description else ""),
                         reply_markup=reply_markup)


@dp.message_handler(Command("edit_profile"))
async def edit_profile(message: types.Message):
    await name_question(message)
