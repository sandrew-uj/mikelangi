import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ReplyKeyboardRemove

from filters.is_private import IsPrivate
from handlers.users.profile_creating.profile import show_profile
from keyboards.default.likes import like_or_not, LIKE, DISLIKE, SLEEP
from loader import dp, bot
from states.search_states import SearchState
from utils.db_api import quick_commands as db
from utils.db_api.quick_commands import add_love
from utils.db_api.schemas.user import User


@dp.message_handler(IsPrivate(), Command("search"))
async def my_search(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    print(f"{user_id} and {message.chat.id}")
    try:
        user = await db.select_user(id=user_id)
    except Exception:
        return await message.answer('Сначала необходимо создать анкету, для этого воспользуйтесь /profile')

    interests = await User.query.where(User.gender == user.interest and User.interest == user.gender).gino.all()
    my_interest = random.choice(interests)
    await show_profile(profile_owner_id=my_interest.id, receiver_id=user_id, reply_markup=like_or_not)
    print("data updating")
    await state.update_data(user_id=my_interest.id)
    print("success")
    # await SearchState.React.set()


@dp.message_handler(IsPrivate(), text=LIKE)
async def my_like(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = data.get("user_id")

    await bot.send_message(user_id, text="Ты понравился одному человеку\n"
                           "Посмотреть: /see_love")
    await add_love(user_id, message.from_user.id)
    # await show_profile(profile_owner_id=message.from_user.id, receiver_id=user_id, reply_markup=like_or_not)

    await my_search(message, state)
    # await state.finish()


@dp.message_handler(IsPrivate(), text=DISLIKE)
async def my_dislike(message: types.Message, state: FSMContext):
    print("dislike")
    await my_search(message, state)
    # await state.finish()


@dp.message_handler(IsPrivate(), text=SLEEP)
async def my_sleep(message: types.Message, state: FSMContext):
    await message.answer("Я устал", reply_markup=ReplyKeyboardRemove())
    # await state.finish()
