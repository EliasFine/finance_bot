from aiogram.filters.callback_data import CallbackData


class CategoryCallback(CallbackData, prefix='category'):
    id: int
    title: str