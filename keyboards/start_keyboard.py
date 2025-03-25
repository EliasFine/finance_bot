from aiogram.utils.keyboard import ReplyKeyboardBuilder

def start_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Доход 💰')
    builder.button(text='Расход 🛒')
    builder.button(text='Мои счета')
    builder.adjust(2, 1)
    return builder.as_markup(resize_keyboard=True)