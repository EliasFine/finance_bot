from aiogram.fsm.state import State, StatesGroup


class CreateWalletState(StatesGroup):
    title = State()
    balance = State()