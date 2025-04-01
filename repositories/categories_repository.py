from sqlite3 import Connection


class CategoriesRepository:
    def __init__(self, db: Connection):
        self.db = db
        self._create_table()

    def _create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            type_categories BOOLEAN,
            user_id INTEGER NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
            )
        '''
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

    def create(
            self,
            title: str,
            type_categories: bool,
            user_id: int=None,
    ):
        sql = '''INSERT INTO categories 
        (title, type_categories, user_id) VALUES 
        (?, ?, ?)
        '''
        cursor = self.db.cursor()
        cursor.execute(sql, (title, type_categories, user_id, ))
        self.db.commit()

    def get_categories_by_user_id(self, user_id: int):
        sql = '''SELECT * FROM categories WHERE user_id = ? OR user_id IS NULL'''
        cursor = self.db.cursor()
        cursor.execute(sql, (user_id,))
        return cursor.fetchall()