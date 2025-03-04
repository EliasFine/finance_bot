from sqlite3 import Connection
from typing import List


class UserRepository:
    def __init__(self, db: Connection):
        self.db = db
        self._create_table()

    def _create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT,
            user_name TEXT,
            created DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        '''
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

    def create(
            self,
            user_id: int,
            full_name: str,
            user_name: str
    ):
        sql = '''INSERT INTO users 
            (id, full_name, user_name) VALUES
            (?, ?, ?)
        '''
        cursor = self.db.cursor()
        cursor.execute(sql, (user_id, full_name, user_name, ))
        self.db.commit()

    def get_all(self) -> List[tuple]:
        sql = "SELECT * FROM users"
        cursor = self.db.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def get_by_id(self, user_id: int) -> tuple | None:
        sql = "SELECT * FROM users WHERE id = ?"
        cursor = self.db.cursor()
        cursor.execute(sql, (user_id, ))
        return cursor.fetchone()