import conexao


conexao = conexao.ConexaoBancoDeDados(
    host="localhost",
    porta=3306,
    banco="StockSafe",
    usuario="aluno",
    senha="sptech",
)

# Conecta com o banco de dados
conexao.conectar()

# Cria uma tabela no banco de dados
cursor = conexao.conexao.cursor()
""" 
cursor.execute(f"CREATE TABLE IF NOT EXISTS pessoas (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), idade INT)")
conexao.conexao.commit() """

# Insere um registro na tabela
"""cursor.execute(f"INSERT INTO pessoas (nome, idade) VALUES ('João', 25)")
conexao.conexao.commit()"""

# Lista os registros da tabela
registros = cursor.execute(f"SELECT nome FROM tb_funcionario")
for registro in registros:      
    print(registros)

pessoas = ["João", "Maria", "Pedro"]
for pessoa in pessoas:
    print(pessoa)
# Desconecta do banco de dados
#conexao.desconectar()