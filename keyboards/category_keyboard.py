from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import CategoryCallback


def category_keyboard(categories):
    builder = InlineKeyboardBuilder()
    for category in categories:
        builder.button(text=category[1], callback_data=CategoryCallback(id=category[0], title=category[1]))
    builder.adjust(1)
    return builder.as_markup()