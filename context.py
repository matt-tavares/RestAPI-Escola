import psycopg2 as db
from connection import Config

class Context(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config['postgres'])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def Commit(self):
        self.connection.commit()

    def FetchAll(self):
        return self.cursor.fetchall()

    def Execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.FetchAll()

    def Query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.FetchAll()

CONTEXT = Context