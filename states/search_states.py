from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchState(StatesGroup):
    React = State()
    Answer = State()
