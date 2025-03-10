from services import OperationsService
from states import IncomeState
from aiogram import types
from aiogram.fsm.context import FSMContext


class IncomeHandler:
    def __init__(self, operations_service: OperationsService):
        self.operations_service = operations_service

    async def cdm_income(self, message: types.Message, state: FSMContext):
        await message.answer('Введите название дохода')
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

