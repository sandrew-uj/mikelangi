from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfileState(StatesGroup):
    EnterName = State()
    EnterAge = State()
    EnterPhoto = State()
    EnterGender = State()
    EnterInterests = State()
    EnterDescription = State()
    AddDescription = State()
