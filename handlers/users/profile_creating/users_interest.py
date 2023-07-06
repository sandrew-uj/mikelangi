from aiogram import types

from filters.is_private import IsPrivate
from keyboards.default.description import description
from loader import dp
from states.profile_states import ProfileState
from utils.db_api import quick_commands as db


@dp.message_handler(IsPrivate(), state=ProfileState.EnterInterests)
async def get_interest(message: types.Message):
    interest = message.text
    await db.update_user_interest(interest=interest, id=message.from_user.id)

    await message.answer("Добавьте описание:", reply_markup=description)
    await ProfileState.next()
