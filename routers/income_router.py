from aiogram import Dispatcher, F
from handlers import IncomeHandler
from states import IncomeState
from callbacks import ChooseWalletCallback, CategoryCallback


class IncomeRouter:
    def __init__(self, dp: Dispatcher, income_handler: IncomeHandler):
        self.dp = dp
        self.income_handler = income_handler

    def register_paths(self):
        self.dp.message.register(self.income_handler.cmd_income, F.text.in_({'Доход 💰', '/income'}))
        self.dp.callback_query.register(self.income_handler.get_wallet, ChooseWalletCallback.filter())
        self.dp.callback_query.register(self.income_handler.get_category, CategoryCallback.filter())
        self.dp.message.register(self.income_handler.get_title, IncomeState.title)
        self.dp.message.register(self.income_handler.get_total, IncomeState.total)