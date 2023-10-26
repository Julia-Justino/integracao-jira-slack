import requests
import json

mensagemAlerta = {"text": f"""
    TESTE 001 COM PYTHON
"""}

conexao = "https://hooks.slack.com/services/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"
post = requests.post(conexao, data=json.dumps(mensagemAlerta))
print(post.status_code)