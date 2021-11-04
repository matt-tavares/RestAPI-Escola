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
        self.commit()
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

CAPP = Context

#
# class Titulo(Context):
#     def __init__(self):
#         Context.__init__(self)
#
#     def get_titulos(self):
#         try:
#             sql = 'SELECT * FROM "production"."titulo";'
#             data = self.Query(sql)
#             self.Commit()
#             return data
#         except Exception as e:
#             # Retorna código do erro do postgres
#             return e.pgcode
#
#     def post_titulo(self,  *args):
#         try:
#             sql = 'INSERT INTO "production"."titulo" (tx_descricao) VALUES (%s) RETURNING *'
#             response = self.Execute(sql, args)
#             self.Commit()
#             code = 200
#             #return response, 200
#         except Exception as e:
#             return e
#
#             # Retorna código do erro do postgres
#         #     if e.pgcode == '23505':
#         #         code = 400
#         #         response = "Violação de Unique key"
#
#     def put_titulo(self,  *args):
#         try:
#             sql = '''
#                     UPDATE "production"."titulo"
#                     SET tx_descricao = %s
#                     WHERE id_titulo = %s
#                     RETURNING *;
#                 '''
#             response = self.query(sql, args)
#             self.commit()
#             return response, 200
#         except Exception as e:
#             # Retorna código do erro do postgres
#             return e.pgcode
#
#     def delete_titulo(self,  *args):
#         try:
#             sql = '''
#                     DELETE FROM "production"."titulo"
#                     WHERE id_titulo = %s
#                     RETURNING *;
#                 '''
#             self.execute(sql, args)
#             self.commit()
#         except Exception as e:
#             # Retorna código do erro do postgres
#             return e.pgcode
#
# if __name__ == '__main__':
#     titulo = Titulo()
#     print(titulo.post_titulo("Python3"))
#     #titulo.put_titulo("Especialistaaa", 12)
#     #titulo.delete_titulo(6)
#     #print(titulo.get_titulos())