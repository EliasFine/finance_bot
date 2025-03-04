from aiogram import Dispatcher
from handlers import CommandHandler
from aiogram.filters.command import Command


class CommandRouter:
    def __init__(self, dp: Dispatcher, command_handler: CommandHandler):
        self.dp = dp
        self.command_handler = command_handler

    def register_paths(self):
        self.dp.message.register(self.command_handler.start_handler, Command('start'))