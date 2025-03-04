from repositories import WalletRepository

class WalletService:
    def __init__(self, wallet_repository: WalletRepository):
        self.wallet_repository = wallet_repository

    def create(
            self,
            title: str,
            balance: float,
            user_id: int
    ):
        self.wallet_repository.create(title, balance, user_id)


