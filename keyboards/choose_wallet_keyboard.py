from aiogram.utils.keyboard import InlineKeyboardBuilder
from callbacks import ChooseWalletCallback



def choose_wallet_keyboard(wallets):
    builder = InlineKeyboardBuilder()
    for wallet in wallets:
        builder.button(text=wallet[1], callback_data=ChooseWalletCallback(id=wallet[0], title=wallet[1]))
    builder.adjust(1)
    return builder.as_markup()
