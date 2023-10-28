# para  baixar o pacote: python3 -m pip install PyMySQL
import pymysql

class ConexaoBancoDeDados:
    def __init__(self, host, porta, banco, usuario, senha):
        self.host = host
        self.porta = porta
        self.banco = banco
        self.usuario = usuario
        self.senha = senha

    def conectar(self):
        self.conexao = pymysql.connect(
            host=self.host,
            port=self.porta,
            database=self.banco,
            user=self.usuario,
            password=self.senha,
        )

    def desconectar(self):
        self.conexao.close()