from aiogram import Dispatcher, F
from handlers import StatisticsHandler
from callbacks import StatisticsCallback


class StatisticsRouter:
    def __init__(self, dp: Dispatcher, statistics_handler: StatisticsHandler):
        self.dp = dp
        self.statistics_handler = statistics_handler

    def register_paths(self):
        self.dp.message.register(self.statistics_handler.show_stats, F.text.in_({'Статистика 📊', '/statistics'}))
        self.dp.callback_query.register(self.statistics_handler.statistics_callback, StatisticsCallback.filter())
