from sqlite3 import Connection
from datetime import date


class OperationsRepository:
    def __init__(self, db: Connection):
        self.db = db
        self._create_table()

    def _create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS operations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            is_income BOOLEAN,
            total FLOAT,
            user_id INTEGER,
            wallet_id INTEGER,
            created DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (wallet_id) REFERENCES wallets (id)
            )
        '''
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

    def create(
            self,
            title: str,
            is_income: bool,
            total: float,
            user_id: int,
            wallet_id: int
    ):
        sql = '''INSERT INTO operations 
        (title, is_income, total, user_id, wallet_id) VALUES 
        (?, ?, ?, ?, ?)
        '''
        cursor = self.db.cursor()
        cursor.execute(sql, (title, is_income, total, user_id, wallet_id, ))
        self.db.commit()

    def get_by_wallet(self, wallet_id: int):
        sql = 'SELECT * FROM operations WHERE wallet_id = ?'
        cursor = self.db.cursor()
        cursor.execute(sql, (wallet_id, ))
        return cursor.fetchall()

    def get_by_dates(self, start_date: date, end_date: date):
        sql = 'SELECT * FROM operations WHERE created BETWEEN ? AND ?'
        cursor = self.db.cursor()
        cursor.execute(sql, (start_date, end_date,))
        return cursor.fetchall()
