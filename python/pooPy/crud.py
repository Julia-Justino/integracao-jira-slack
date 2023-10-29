import conexao
import alerta
import jira



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
registros = cursor.execute("SELECT uso_cpu FROM tb_registro")
resultado = cursor.fetchall()
for x in resultado:
    print(x)

resultadoInteiro = int(resultado)

if resultado>75:
    DadosSlack = alerta.DadosSlack(
    mensagem=f"TESTE: CPU está fora das métricas {resultado}",
    conexao = "https://hooks.slack.com/services/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"
    
)

DadosSlack.enviar_mensagem()

DadosJira = jira.DadosJira(
    url = "https://stock-safe-solutions.atlassian.net/rest/api/3/issue",
    responsavel="stephany.justino@sptech.school",
    tokenConexao="ATATT3xFfGF0Ts4XoKjh8AwEkcWNOEIN8ertxXPiILZcVXoiZduTrNPF9DVcihsmue8q2m4FdrYm8U_Cg6iwpeotYG7xAY3nA90u4uMf_uz02yw-01Fl-wp3k9fu6XY384mZb9GHa4oGPRJZ9XIhsBxMDSaPLeAV0K0yjrxg6vc79w1Y_LurqyA=965A04E3"
)

DadosJira.abrirAlerta(f"TESTE: CPU está fora das métricas {resultado}", "STOCKSAFE", "Task")

# Desconecta do banco de dados
#conexao.desconectar()