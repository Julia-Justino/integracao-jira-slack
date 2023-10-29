import alerta
import jira

DadosSlack = alerta.DadosSlack(
    mensagem="TESTE COM POO PYTHON AAAAAAAAAA",
    conexao = "https://hooks.slack.com/services/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"
    
)

DadosSlack.enviar_mensagem()

DadosJira = jira.DadosJira(
    url = "https://stock-safe-solutions.atlassian.net/rest/api/3/issue",
    responsavel="stephany.justino@sptech.school",
    tokenConexao="ATATT3xFfGF0mPVHEz4vbo3MOd4BD1ZYrThPWNnZ-xmmItbdyJUmuJRTseI59LPB5E8TeFnBiM73Br0R_pDZt_iLcqOw66gcwXm8R-1pP2MaNdMN2Bph8UvJtrJTYSWZ3lkowRzn-AhFwZ8bReL0YGDZIAKngUt3PE0-dQ-GADmv-kDXF8MqiVA=12E14993"
)

DadosJira.abrirAlerta("TESTE COM POO", "STOCKSAFE", "Task")