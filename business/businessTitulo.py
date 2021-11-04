from context import CAPP

# Retorna código do erro do postgres
#     if e.pgcode == '23505':
#         code = 400
#         response = "Violação de Unique key"

class Titulo(CAPP):
    def __init__(self):
        CAPP.__init__(self)

    def msg_retorno_except(self, code, msg):
        retorno = {"Retorno": {"Code:": code, "Message": msg}}, code
        return retorno

    def msg_retorno_success(self, code, msg):
        retorno = {"Retorno": {"Code:": code, "Message": msg}}, code
        return retorno

    def get_titulos(self):
        try:
            sql = 'SELECT * FROM "production"."titulo";'
            data = self.Query(sql)
            self.Commit()
            return data
        except Exception as e:
            menssage = "erro"
            code = 400
            return BTitulo.msg_retorno_except(code, menssage)

    def post_titulo(self,  *args):
        try:
            sql = 'INSERT INTO "production"."titulo" (tx_descricao) VALUES (%s) RETURNING *'
            response = self.Execute(sql, args)
            self.Commit()
            return BTitulo.msg_retorno_success(200, response)
        except Exception as e:
            return BTitulo.msg_retorno_except(400, "erro")

    def put_titulo(self,  *args):
        try:
            sql = '''
                    UPDATE "production"."titulo"
                    SET tx_descricao = %s
                    WHERE id_titulo = %s
                    RETURNING *;
                '''
            response = self.Query(sql, args)
            self.Commit()
            if response:
                return BTitulo.msg_retorno_success(200, response)
            else:
                return BTitulo.msg_retorno_except(400, "erro na alteração")
        except Exception as e:
            return BTitulo.msg_retorno_except(400, e)

    def delete_titulo(self,  *args):
        try:
            sql = '''
                    DELETE FROM "production"."titulo"
                    WHERE id_titulo = %s
                    RETURNING *;
                '''
            retorno = self.Execute(sql, args)
            self.Commit()
            if retorno:
                return BTitulo.msg_retorno_success(200, "Titulo excluído")
            else:
                return BTitulo.msg_retorno_except(400, "erro da exclusao")
        except Exception as e:
            return BTitulo.msg_retorno_except(400, e)

BTitulo = Titulo()

if __name__ == '__main__':
    titulo = Titulo()
    #print(BTitulo.post_titulo("Python3"))
    print(BTitulo.put_titulo("Teste", 71))
    #print(BTitulo.delete_titulo(71))
    #print(BTitulo.get_titulos())