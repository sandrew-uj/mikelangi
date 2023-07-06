from aiogram import types
from aiogram.types import CallbackQuery
from filters.is_private import IsPrivate
from handlers.users.profile_creating.users_age import age_question
from keyboards.inline.confirmation import conf_callback, confirmation_keyboard
from loader import dp
from states.profile_states import ProfileState
from utils.db_api import quick_commands as db


@dp.callback_query_handler(conf_callback.filter(action="save"), state=ProfileState.EnterName)
async def save_name(call: CallbackQuery):
    await call.answer(cache_time=10)
    await age_question(call.message, call.from_user.id)


@dp.message_handler(IsPrivate(), state=ProfileState.EnterName)
async def get_name(message: types.Message):
    name = message.text
    await db.update_user_name(name=name, id=message.from_user.id)
    await age_question(message, message.from_user.id)


async def name_question(message: types.Message):
    await ProfileState.EnterName.set()
    await message.answer("Как вас зовут?")
    user = await db.select_user(id=message.from_user.id)
    if user.name:
        await message.answer(f"Оставить текущее имя?\n {user.name}", reply_markup=confirmation_keyboard)
