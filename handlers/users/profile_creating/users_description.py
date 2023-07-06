from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from filters.is_private import IsPrivate
from handlers.users.profile_creating.profile import show_profile
from loader import dp
from states.profile_states import ProfileState
from utils.db_api import quick_commands as db


@dp.message_handler(IsPrivate(), text="Добавить", state=ProfileState.EnterDescription)
async def get_description(message: types.Message):
    await message.answer("Введите описание:", reply_markup=ReplyKeyboardRemove())
    await ProfileState.next()


@dp.message_handler(IsPrivate(), state=ProfileState.AddDescription)
async def add_description(message: types.Message, state: FSMContext):
    desc = message.text
    await db.update_user_description(description=desc, id=message.from_user.id)
    await save(message, state)


@dp.message_handler(IsPrivate(), text="Не надо", state=ProfileState.EnterDescription)
async def cancel(message: types.Message, state: FSMContext):
    await db.update_user_description(description=None, id=message.from_user.id)
    await save(message, state)


@dp.message_handler(IsPrivate(), text="Оставить", state=ProfileState.EnterDescription)
async def save(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer("Ваша анкета выглядит так:", reply_markup=ReplyKeyboardRemove())
    await show_profile(message)
