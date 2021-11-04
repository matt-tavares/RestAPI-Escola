# Contexto da aplicação
# Preencha com os dados do seu banco de dados postgres

class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "DB_user_name",
                "password": "Db_password",
                "host": "Host_address",
                "port": "5432",
                "database": "DB_name"
            }
        }