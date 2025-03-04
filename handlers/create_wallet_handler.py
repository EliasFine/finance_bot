from services import WalletService
from states import CreateWalletState
from aiogram import types
from aiogram.fsm.context import FSMContext


class CreateWalletHandler:
    def __init__(self, wallet_service: WalletService):
        self.wallet_service = wallet_service

    async def cmd_create_wallet(self, message: types.Message, state: FSMContext):
        await message.answer('Введите название кошелька')
        await state.set_state(CreateWalletState.title)

    async def get_title(self, message: types.Message, state: FSMContext):
        title = message.text
        await state.update_data(title=title)
        await message.answer('Введите баланс кошелька')
        await state.set_state(CreateWalletState.balance)

    async def get_balance(self, message: types.Message, state: FSMContext):
        balance = float(message.text)
        data = await state.get_data()
        title = data.get('title')
        user_id = message.from_user.id
        self.wallet_service.create(title, balance, user_id)
        await message.answer('Кошелек успешно создан')


