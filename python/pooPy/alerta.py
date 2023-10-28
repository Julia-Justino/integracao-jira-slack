import requests
import json

class DadosSlack:
    def __init__(self, mensagem, conexao):
        self.conexao = conexao
        self.mensagem = mensagem

    def enviar_mensagem(self):
        # Envia a mensagem para o Slack
        post = requests.post(self.conexao, json={"text": self.mensagem})
        print(post.status_code)
