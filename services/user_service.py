from repositories import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def signup(self, user_id: int, full_name: str, user_name: str):
        if self.user_repository.get_by_id(user_id) is not None:
            return False

        self.user_repository.create(user_id, full_name, user_name)
        return True


