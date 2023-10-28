import alerta

DadosSlack = alerta.DadosSlack(
    mensagem="TESTE COM POO PYTHON AAAAAAAAAA",
    conexao = "https://hooks.slack.com/services/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"
    
)

DadosSlack.enviar_mensagem()