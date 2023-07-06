from aiogram import types

from filters.is_private import IsPrivate
from keyboards.default.gender import gender
from loader import dp
from states.profile_states import ProfileState
from utils.db_api import quick_commands as db


async def gender_question(message: types.Message):
    await ProfileState.next()
    await message.answer("Ваш пол:", reply_markup=gender)


@dp.message_handler(IsPrivate(), state=ProfileState.EnterGender)
async def get_gender(message: types.Message):
    g = message.text
    await db.update_user_gender(gender=g, id=message.from_user.id)

    await message.answer("Кто вам интересен?", reply_markup=gender)
    await ProfileState.next()
