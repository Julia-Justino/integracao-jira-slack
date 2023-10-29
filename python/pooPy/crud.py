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
registros = cursor.execute("SELECT uso_cpu FROM tb_registro WHERE uso_ram > 90")
resultado = cursor.fetchall()
for x in resultado:
    print(x)



if registros is not "":
    DadosSlack = alerta.DadosSlack(
    mensagem=f"TESTE: CPU está fora das métricas {resultado}",
    conexao = "https://hooks.slack.com/services/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"
    
)

DadosSlack.enviar_mensagem()

DadosJira = jira.DadosJira(
    url = "https://stock-safe-solutions.atlassian.net/rest/api/3/issue",
    responsavel="stephany.justino@sptech.school",
    tokenConexao="ATATT3xFfGF0mPVHEz4vbo3MOd4BD1ZYrThPWNnZ-xmmItbdyJUmuJRTseI59LPB5E8TeFnBiM73Br0R_pDZt_iLcqOw66gcwXm8R-1pP2MaNdMN2Bph8UvJtrJTYSWZ3lkowRzn-AhFwZ8bReL0YGDZIAKngUt3PE0-dQ-GADmv-kDXF8MqiVA=12E14993"
)

DadosJira.abrirAlerta(f"TESTE: CPU está fora das métricas {resultado}", "STOCKSAFE", "Task")

# Desconecta do banco de dados
#conexao.desconectar()