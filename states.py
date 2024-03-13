from aiogram.dispatcher.filters.state import State, StatesGroup


class AdminStates(StatesGroup):
    add_evos_state = State()
