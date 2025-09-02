import oracledb

class oracleConexao:
    def __init__(self, user, password, host, port, serviceName):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.serviceName = serviceName
        self.conn = None

    def conectar(self):
        try: 
            self.conn = oracledb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                serviceName=self.serviceName
            )
            cursor = self.conn.cursor()
            print("Conexão bem-sucedida!")
            return self.conn, cursor
        except Exception as e:
            print("Erro ao conectar:", e)
            return None, None

    def desconectar(self, conn, cursor):
        try:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            print("Conexão encerrada.")
        except Exception as e:
            print("Erro ao desconectar:", e)

            return self.conn, cursor
        except Exception as e:
            print("Erro ao conectar:", e)
            return None, None

    def desconectar(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            print("Conexão encerrada.")
        except Exception as e:
            print("Erro ao desconectar:", e)
            print("Conexão encerrada.")
        except Exception as e:
            print("Erro ao desconectar:", e)
