from aiogram.filters.callback_data import CallbackData


class ChooseWalletCallback(CallbackData, prefix='choose_wallet'):
    id: int
    title: str
