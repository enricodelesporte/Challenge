import cx_Oracle

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
            dsn = cx_Oracle.makedsn(self.host, self.port, service_name=self.serviceName)
            self.conn = cx_Oracle.connect(user=self.user, password=self.password, dsn=dsn)
            print("Conexão bem-sucedida!")
            return self.conn
        
        except cx_Oracle.Error as e:
            print("Erro ao conectar:", e)
            return None

    def desconectar(self):
        if self.conn:
            self.conn.close()
            print("Conexão encerrada.")