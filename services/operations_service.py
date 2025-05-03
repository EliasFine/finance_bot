from repositories import OperationsRepository
from datetime import date

class OperationsService:
    def __init__(self, operations_repository: OperationsRepository):
        self.operations_repository = operations_repository

    def create(
            self,
            title: str,
            is_income: bool,
            total: float,
            user_id: int,
            wallet_id: int
    ):
        self.operations_repository.create(title, is_income, total, user_id, wallet_id)

    def get_by_dates(
            self,
            start_date: date,
            end_date: date
    ):
        return self.operations_repository.get_by_dates(start_date, end_date)
