from requests.auth import HTTPBasicAuth
import requests


resultado = requests.get('http://localhost:5000/login',auth=('jose', '123456'))

print(resultado.json())
