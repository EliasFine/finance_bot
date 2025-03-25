from callbacks import ChooseWalletCallback
from services import OperationsService, WalletService
from states import IncomeState
from aiogram import types
from aiogram.fsm.context import FSMContext
from keyboards import choose_wallet_keyboard


class IncomeHandler:
    def __init__(self, operations_service: OperationsService, wallet_service: WalletService):
        self.operations_service = operations_service
        self.wallet_service = wallet_service

    async def cmd_income(self, message: types.Message, state: FSMContext):
        wallets = self.wallet_service.get_by_user_id(message.from_user.id)
        if len(wallets) == 1:
            await message.answer('Введите название дохода')
            await state.set_state(IncomeState.title)
            return
        await message.answer('Выберите счет', reply_markup=choose_wallet_keyboard(wallets))

    async def get_wallet(self, callback: types.CallbackQuery, state: FSMContext, callback_data: ChooseWalletCallback):
        await callback.message.edit_text(text=f'Выбран счет {callback_data.title}', reply_markup=None)
        await state.update_data(wallet_id=callback_data.id)
        await callback.message.answer('Введите название дохода')
        await state.set_state(IncomeState.title)

    async def get_title(self, message: types.Message, state: FSMContext):
        title = message.text
        await state.update_data(title=title)
        await message.answer('Введите сумму дохода')
        await state.set_state(IncomeState.total)

    async def get_total(self, message: types.Message, state: FSMContext):
        total = float(message.text)
        data = await state.get_data()
        title = data.get('title')
        user_id = message.from_user.id
        wallet_id = 1
        self.operations_service.create(title, is_income=True, total=total, user_id=user_id, wallet_id=wallet_id)
        await message.answer('Доход успешно сохранен')

