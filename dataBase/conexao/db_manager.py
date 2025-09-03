from dataBase.conexao.oracleConexao import oracleConexao

class DBManager:
    _conexao = None
    _cursor = None

    @classmethod
    def conectar(cls):
        if cls._conexao is None or cls._cursor is None:
            conexao = oracleConexao(
                user="rm565760",
                password="150606",
                host="oracle.fiap.com.br",
                port="1521",
                serviceName="orcl"
            )
            cls._conexao, cls._cursor = conexao.conectar()
        return cls._conexao, cls._cursor

    @classmethod
    def desconectar(cls):
        if cls._conexao and cls._cursor:
            conexao = oracleConexao("", "", "", "", "")
            conexao.desconectar(cls._conexao, cls._cursor)
            cls._conexao, cls._cursor = None, None