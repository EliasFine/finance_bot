from aiogram.fsm.state import State, StatesGroup


class IncomeState(StatesGroup):
    wallet_id = State()
    title = State()
    total = State()