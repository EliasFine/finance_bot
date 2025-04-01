from repositories import CategoriesRepository


class CategoriesService:
    def __init__(self, categories_repository: CategoriesRepository):
        self.categories_repository = categories_repository

    def create(
            self,
            title: str,
            type_categories: bool,
            user_id: int,
    ):
        self.categories_repository.create(title, type_categories, user_id)

    def get_categories_by_user_id(self, user_id: int):
        return self.categories_repository.get_categories_by_user_id(user_id)