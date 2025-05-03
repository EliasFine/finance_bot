from services import OperationsService
from aiogram import types
from datetime import date, timedelta


class StatisticsHandler:
    def __init__(self, operations_service: OperationsService):
        self.operations_service = operations_service

    async def show_stats(self, message: types.Message):
        start_date = date.today()
        end_date = date.today() + timedelta(days=1)
        operations = self.operations_service.get_by_dates(start_date, end_date)
        msg = '\n'.join([f'{o[1]} {o[3]}' for o in operations])
        await message.answer(msg)


