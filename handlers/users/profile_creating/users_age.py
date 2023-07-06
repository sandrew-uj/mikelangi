from aiogram import types
from aiogram.types import CallbackQuery
from filters.is_private import IsPrivate
from handlers.users.profile_creating.users_image import image_question
from keyboards.inline.confirmation import conf_callback, confirmation_keyboard
from loader import dp
from states.profile_states import ProfileState
from utils.db_api import quick_commands as db


async def age_question(message: types.Message, user_id):
    await ProfileState.next()
    await message.answer("Сколько вам лет?")
    user = await db.select_user(id=user_id)
    if user.age:
        await message.answer(f"Оставить текущий возраст?\n {user.age}", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(conf_callback.filter(action="save"), state=ProfileState.EnterAge)
async def save_age(call: CallbackQuery):
    await call.answer(cache_time=10)
    await image_question(call.message, call.from_user.id)


@dp.message_handler(IsPrivate(), state=ProfileState.EnterAge)
async def get_age(message: types.Message):
    age = message.text
    await db.update_user_age(age=int(age), id=message.from_user.id)
    await image_question(message, message.from_user.id)
