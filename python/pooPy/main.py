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
    tokenConexao="ATATT3xFfGF0Ts4XoKjh8AwEkcWNOEIN8ertxXPiILZcVXoiZduTrNPF9DVcihsmue8q2m4FdrYm8U_Cg6iwpeotYG7xAY3nA90u4uMf_uz02yw-01Fl-wp3k9fu6XY384mZb9GHa4oGPRJZ9XIhsBxMDSaPLeAV0K0yjrxg6vc79w1Y_LurqyA=965A04E3"
)

DadosJira.abrirAlerta("TESTE COM POO", "STOCKSAFE", "Task")