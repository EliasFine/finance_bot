from aiogram import Dispatcher
from handlers import IncomeHandler
from aiogram.filters.command import Command
from states import IncomeState
from callbacks import ChooseWalletCallback


class IncomeRouter:
    def __init__(self, dp: Dispatcher, income_handler: IncomeHandler):
        self.dp = dp
        self.income_handler = income_handler

    def register_paths(self):
        self.dp.message.register(self.income_handler.cmd_income, Command('income'))
        self.dp.callback_query.register(self.income_handler.get_wallet, ChooseWalletCallback.filter())
        self.dp.message.register(self.income_handler.get_title, IncomeState.title)
        self.dp.message.register(self.income_handler.get_total, IncomeState.total)