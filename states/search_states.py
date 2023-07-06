from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchState(StatesGroup):
    Search = State()
    React = State()
    Answer = State()
