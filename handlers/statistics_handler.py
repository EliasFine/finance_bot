from services import OperationsService
from aiogram import types
from datetime import date, timedelta
from keyboards import statistics_keyboard
from callbacks import StatisticsCallback
from aiogram.fsm.context import FSMContext


class StatisticsHandler:
    def __init__(self, operations_service: OperationsService):
        self.operations_service = operations_service

    async def show_stats(self, message: types.Message, state: FSMContext):
        start_date = date.today()
        end_date = date.today() + timedelta(days=1)
        await state.update_data(start_date=start_date, end_date=end_date, scale='d')
        date_str = f'{start_date.strftime("%d.%m")}'
        operations = self.operations_service.get_by_dates(start_date, end_date)
        msg = '\n'.join([f'{o[1]} {o[3]}' for o in operations]) if len(operations) > 0 else 'действий нет'
        await message.answer(msg, reply_markup=statistics_keyboard(date_str))

    async def _edit_stats(self, callback: types.CallbackQuery, state: FSMContext):
        data = await state.get_data()
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        scale = data.get('scale')

        if scale == 'd':
            date_str = f'{start_date.strftime("%d.%m")}'
        elif scale == 'w':
            date_str = f'{start_date.strftime("%d.%m")} - {end_date.strftime("%d.%m")}'
        else:
            date_str = f'{start_date.strftime("%m.%Y")}'

        operations = self.operations_service.get_by_dates(start_date, end_date)
        msg = '\n'.join([f'{o[1]} {o[3]}' for o in operations]) if len(operations) > 0 else 'действий нет'
        await callback.message.edit_text(msg, reply_markup=statistics_keyboard(date_str))

    async def statistics_callback(
            self,
            callback: types.CallbackQuery,
            callback_data: StatisticsCallback,
            state: FSMContext
    ):

        if callback_data.action == 'back':
            data = await state.get_data()
            scale = data.get('scale')
            start_date = data.get('start_date')

            if scale == 'd':
                start_date = start_date - timedelta(days=1)
                end_date = start_date + timedelta(days=1)
            elif scale == 'w':
                start_date = start_date - timedelta(weeks=1)
                end_date = start_date + timedelta(weeks=1)
            else:
                m = start_date.month
                y = start_date.year
                end_date = start_date - timedelta(days=1)
                start_date = date(month=m - 1 if m != 1 else 12, day=1, year=y if m != 1 else y - 1)

            await state.update_data(start_date=start_date, end_date=end_date)

        elif callback_data.action == 'next':
            data = await state.get_data()
            scale = data.get('scale')
            start_date = data.get('start_date')

            if scale == 'd':
                start_date = start_date - timedelta(days=1)
                end_date = start_date + timedelta(days=1)
            elif scale == 'w':
                start_date = start_date - timedelta(weeks=1)
                end_date = start_date + timedelta(weeks=1)
            else:
                m = start_date.month
                y = start_date.year
                start_date = date(month=m + 1 if m != 12 else 1, day=1, year=y if m != 12 else y + 1)
                m = start_date.month
                y = start_date.year
                end_date = date(month=m + 1 if m != 12 else 1, day=1, year=y + 1 if m == 12 else y) - timedelta(days=1)

            await state.update_data(start_date=start_date, end_date=end_date)

        elif callback_data.action == 'scale':
            data = await state.get_data()
            scale = data.get('scale')
            start_date = data.get('start_date')

            if scale == 'd':
                scale = 'w'
                while start_date.weekday() > 0:
                    start_date -= timedelta(days=1)
                end_date = start_date + timedelta(days=6)

            elif scale == 'w':
                scale = 'm'
                m = start_date.month
                y = start_date.year
                start_date = date(month=m, day=1, year=y)
                end_date = date(month=m + 1 if m != 12 else 1, day=1, year=y + 1 if m == 12 else y) - timedelta(days=1)
            else:
                scale = 'd'
                start_date = date.today()
                end_date = date.today() + timedelta(days=1)

            await state.update_data(start_date=start_date, end_date = end_date, scale=scale)


        await self._edit_stats(callback, state)
