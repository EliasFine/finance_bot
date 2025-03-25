from aiogram import Dispatcher, F
from handlers import ExpenseHandler
from states import ExpenseState
from callbacks import ChooseWalletCallback


class ExpenseRouter:
    def __init__(self, dp: Dispatcher, expense_handler: ExpenseHandler):
        self.dp = dp
        self.expense_handler = expense_handler

    def register_paths(self):
        self.dp.message.register(self.expense_handler.cmd_expense, F.text.in_({'Расход 🛒', '/expense'}))
        self.dp.callback_query.register(self.expense_handler.get_wallet, ChooseWalletCallback.filter())
        self.dp.message.register(self.expense_handler.get_title, ExpenseState.title)
        self.dp.message.register(self.expense_handler.get_total, ExpenseState.total)