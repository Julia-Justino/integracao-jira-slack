import requests 
from requests.auth import HTTPBasicAuth
import json

class DadosJira:
    def __init__(self, url, responsavel, tokenConexao):
        self.url = url
        self.responsavel = responsavel
        self.token = tokenConexao

    def abrirAlerta(self, resumo, senhaProjeto, tipoChamado):
        auth = HTTPBasicAuth(self.responsavel, self.token)
        headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
        }

        payload = json.dumps({
            "fields":{
                "summary":f"{resumo}",
                "project": {"key":f"{senhaProjeto}"},
                'issuetype':{'name':f"{tipoChamado}"},
              
        }
        })

        response = requests.request(
            "POST", 
            self.url,
            data=payload,
            headers=headers,
            auth=auth
        )

        print(json.dumps(json.loads(response.text), sort_keys=True, indent=4,separators=(",",": ")))