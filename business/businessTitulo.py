from context import CONTEXT

class Titulo(CONTEXT):
    def __init__(self):
        super().__init__()
        CONTEXT.__init__(self)

    def msg_retorno_except(self, code, msg):
        retorno = {"response": {"code:": code, "message": msg}}, code
        return retorno

    def msg_retorno_success(self, code, msg):
        retorno = {"response": {"code:": code, "data": msg}}, code
        return retorno

    def dados_retorno_success(self, code, msg):
        retorno = {"response": {"code":  code,"data": msg}}
        return retorno

    # Busca todos os títulos
    def get_titulos(self):
        try:
            sql = 'SELECT * FROM "production"."titulo";'
            data = self.Query(sql)
            self.Commit()
            return Titulo.dados_retorno_success(200, data)
        except Exception as e:
            menssage = "erro"
            code = 400
            return Titulo.msg_retorno_except(code, e)

    # Busca um título pelo ID
    def get_titulo(self, *args):
        try:
            sql = '''
                SELECT *
                FROM "production"."titulo"
                WHERE id_titulo = %s;
            '''
            data = self.Query(sql, args)
            self.Commit()
            return Titulo.dados_retorno_success(200, data)
        except Exception as e:
            menssage = "erro"
            code = 400
            return Titulo.msg_retorno_except(code, e)

    def post_titulo(self,  *args):
        try:
            sql = 'INSERT INTO "production"."titulo" (tx_descricao) VALUES (%s) RETURNING *'
            response = self.Execute(sql, args)
            self.Commit()
            return Titulo.msg_retorno_success(200, response)
        except Exception as e:
            self.Commit()
            return Titulo.msg_retorno_except(400, str(e))

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
                return Titulo.msg_retorno_success(200, response)
            else:
                return Titulo.msg_retorno_except(400, "erro na alteração")
        except Exception as e:
            self.Commit()
            return Titulo.msg_retorno_except(400, str(e))

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
                return Titulo.msg_retorno_success(200, "Titulo excluído")
            else:
                return Titulo.msg_retorno_except(400, "erro da exclusao")
        except Exception as e:
            self.Commit()
            return Titulo.msg_retorno_except(400, str(e))

Titulo = Titulo()