import oracledb

class oracleConexao:
    def __init__(self, user, password, host, port, serviceName):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.serviceName = serviceName
        self.conn = None

    def conectar():
        try: 
            conexao = oracledb.connect(
                user="rm565760",
                password="150606",
                dsn="localhost:1521/orcl"
            )
            cursor = conexao.cursor()
            print("Conexão bem-sucedida!")
            return conexao, cursor
        except Exception as e:
            print("Erro ao conectar:", e)
            return None, None

    def desconectar(conexao, cursor):
        try:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
            print("Conexão encerrada.")
        except Exception as e:
            print("Erro ao desconectar:", e)
