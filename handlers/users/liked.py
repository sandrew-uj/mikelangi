import random

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hcode, hlink

from filters.is_private import IsPrivate
from handlers.users.profile_creating.profile import show_profile
from keyboards.default.likes import like_or_not, LIKE, DISLIKE, SLEEP
from loader import dp, bot
from states.search_states import SearchState
from utils.db_api import quick_commands as db
from utils.db_api.quick_commands import delete_love
from utils.db_api.schemas.love import Love


@dp.message_handler(IsPrivate(), Command("see_love"))
async def im_liked(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    print(f"{user_id} and {message.chat.id}")
    try:
        love = await Love.query.where(Love.liked == user_id).gino.first()
    except Exception:
        return await message.answer("Пока что ты никому не понравился(\n"
                                    "Смотреть анкеты: /search")

    if love:
        await show_profile(profile_owner_id=love.likes, receiver_id=love.liked, reply_markup=like_or_not)
        await state.update_data(user_id=love.likes)
        await SearchState.Answer.set()
    else:
        return await message.answer("Пока что ты никому не понравился(\n"
                                    "Смотреть анкеты: /search")


@dp.message_handler(IsPrivate(), state=SearchState.Answer, text=LIKE)
async def match_like(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = data.get("user_id")

    user = await db.select_user(user_id)
    await message.answer("Общаться:\n" +
                         hlink(f"{user.name}", f"tg://user?id={user_id}"))

    await my_mismatch(message, state)


@dp.message_handler(IsPrivate(), state=SearchState.Answer, text=DISLIKE)
async def my_mismatch(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_id = data.get("user_id")

    await delete_love(message.from_user.id, user_id)
    await im_liked(message, state)
    await SearchState.Search.set()


@dp.message_handler(IsPrivate(), state=SearchState.Answer, text=SLEEP)
async def my_missleep(message: types.Message, state: FSMContext):

    await message.answer("Я устал", reply_markup=ReplyKeyboardRemove())
    await state.finish()
