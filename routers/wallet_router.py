from aiogram import Dispatcher
from handlers import CreateWalletHandler
from aiogram.filters.command import Command
from states import CreateWalletState


class WalletRouter:
    def __init__(self, dp: Dispatcher, create_wallet_handler: CreateWalletHandler):
        self.dp = dp
        self.create_wallet_handler = create_wallet_handler

    def register_paths(self):
        self.dp.message.register(self.create_wallet_handler.cmd_create_wallet, Command('new_wallet'))
        self.dp.message.register(self.create_wallet_handler.get_title, CreateWalletState.title)
        self.dp.message.register(self.create_wallet_handler.get_balance, CreateWalletState.balance)