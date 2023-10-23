import requests

resp = requests.post("http://localhost:9898/auth/token", json={"login": "gerasimovrm", "password": "123"})

access_token = resp.json()["accessToken"]

resp =
