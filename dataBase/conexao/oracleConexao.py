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
            dsn = oracledb.makedsn(self.host, self.port, service_name=self.serviceName)
            print(f"Tentando conectar em {self.host}:{self.port}/{self.serviceName} com usuário {self.user}...")
            
            conn = oracledb.connect(user=self.user, password=self.password, dsn=dsn)
            cursor = conn.cursor()
            
            print("Conexão bem-sucedida!")
            return conn, cursor

        except Exception as e:
            print("Erro ao conectar no Oracle:", e)
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
