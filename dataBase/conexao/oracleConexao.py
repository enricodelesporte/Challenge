import cx_Oracle

class oracleConexao:
    def __init__(self, user, password, host, port, serviceName):
        dsn = cx_Oracle.makedsn(host, port, service_name=serviceName)
        self.connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)

    def conectar(self):
        try:
            self.connection = cx_Oracle.connect(user=self.user, password=self.password, dsn=self.dsn)
            print("Conexão bem-sucedida!")
        except cx_Oracle.Error as e:
            print("Erro ao conectar:", e)

    def desconectar(self):
        if self.connection:
            self.connection.close()
            print("Conexão encerrada.")
