from aiogram.fsm.state import State, StatesGroup


class ExpenseState(StatesGroup):
    wallet_id = State()
    title = State()
    total = State()