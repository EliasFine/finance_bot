from aiogram.fsm.state import State, StatesGroup


class StatisticsState(StatesGroup):
    start_data = State()
    end_date = State()
