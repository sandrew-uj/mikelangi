import io
import os

from aiogram import types
from aiogram.types import CallbackQuery

from filters.is_private import IsPrivate
from handlers.users.profile_creating.users_gender import gender_question
from keyboards.inline.confirmation import conf_callback, confirmation_keyboard
from loader import dp
from states.profile_states import ProfileState
from utils.db_api import quick_commands as db


async def image_question(message: types.Message, user_id):
    await ProfileState.next()
    await message.answer("Загрузите фото:")
    user = await db.select_user(id=user_id)
    if user.image:
        await show_image(user, message)
        await message.answer(f"Оставить текущее фото?", reply_markup=confirmation_keyboard)


@dp.callback_query_handler(conf_callback.filter(action="save"), state=ProfileState.EnterPhoto)
async def save_photo(call: CallbackQuery):
    await call.answer(cache_time=10)
    await gender_question(call.message)


@dp.message_handler(IsPrivate(), content_types=types.ContentType.PHOTO, state=ProfileState.EnterPhoto)
async def get_photo(message: types.Message):
    image = message.photo[-1]
    with await image.download(destination=io.BytesIO()) as photo:
        print(photo)
        image_bytes = photo.read()

    await db.update_user_image(image=image_bytes, id=message.from_user.id)
    await gender_question(message)


async def show_image(user, message):
    with open('photos/profile_image.jpg', 'wb') as f:
        f.write(user.image)

    input_file = types.InputFile(path_or_bytesio='photos/profile_image.jpg')
    await message.answer_photo(input_file)
    os.remove('photos/profile_image.jpg')
