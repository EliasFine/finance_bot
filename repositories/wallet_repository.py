from sqlite3 import Connection


class WalletRepository:
    def __init__(self, db: Connection):
        self.db = db
        self._create_table()

    def _create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS wallets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            balance FLOAT,
            user_id INTEGER,
            created DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
            )
        '''
        cursor = self.db.cursor()
        cursor.execute(sql)
        self.db.commit()

    def create(
            self,
            title: str,
            balance: float,
            user_id: int
    ):
        sql = '''INSERT INTO wallets 
        (title, balance, user_id) VALUES 
        (?, ?, ?)
        '''
        cursor = self.db.cursor()
        cursor.execute(sql, (title, balance, user_id, ))
        self.db.commit()

    def get_by_user_id(self, user_id: int):
        sql = "SELECT * FROM wallets WHERE user_id = ?"
        cursor = self.db.cursor()
        cursor.execute(sql, (user_id, ))
        return cursor.fetchall()