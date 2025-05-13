from aiogram.filters.callback_data import CallbackData


class StatisticsCallback(CallbackData, prefix='statistics'):
    action: str
