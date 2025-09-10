from dataBase.conexao.oracleConexao import oracleConexao

class DBManager:
    conexao = None
    cursor = None

    @classmethod
    def conectar(cls):
        if cls.conexao is None or cls.cursor is None:
            conexao = oracleConexao(
                user="rm565760",
                password="150606",
                host="oracle.fiap.com.br",
                port="1521",
                serviceName="orcl"
            )
            cls.conexao, cls.cursor = conexao.conectar()
        return cls.conexao, cls.cursor

    @classmethod
    def desconectar(cls):
        if cls.conexao and cls.cursor:
            conexao = oracleConexao("", "", "", "", "")
            conexao.desconectar(cls.conexao, cls.cursor)
            cls.conexao, cls.cursor = None, None