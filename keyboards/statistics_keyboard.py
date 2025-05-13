from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import StatisticsCallback


def statistics_keyboard(date_str: str):
    builder = InlineKeyboardBuilder()

    builder.button(text='⬅️', callback_data=StatisticsCallback(action='back'))
    builder.button(text=date_str, callback_data=StatisticsCallback(action='scale'))
    builder.button(text='➡️', callback_data=StatisticsCallback(action='next'))

    builder.adjust(3)
    return builder.as_markup()
