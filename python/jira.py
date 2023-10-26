import requests 
from requests.auth import HTTPBasicAuth
import json

url = "https://stock-safe-solutions.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth("stephany.justino@sptech.school", "ATATT3xFfGF0vKkV0Ego4FNhNlsS6W0V_XSGB2lHlPvXREdjKHHxWbz9LvIX1oJ7dZZAofbTow6zQI57eYD97dRblwN4AClbQ96zq7l5ydxM0M6PGQ_XHFXv-tP7ooT5GtjIv5ZAJuBFe98WFHrvTwiM06dAEvKMoJYvZykrbOMbOA6EsOzGz_A=1A14A4B4")

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
mensagemAlerta = {"text": f"""
    TESTE 001 COM PYTHON
"""}
payload = json.dumps({
    "fields":{
        "summary":"teste",
        "project": {"key":"STOCKSAFE"},
        'issuetype':{'name':'Submit a request or incident'}
    }
})

response = requests.request(
    "POST", 
    url,
    data=payload,
    headers=headers,
    auth=auth
)
print(json.dumps(json.loads(response.text), sort_keys=True, indent=4,separators=(",",": ")))