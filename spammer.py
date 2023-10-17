import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://ngl.link/api/submit"

user = input("Username: ")
mensagem = input("Mensagem: ")

spam = True

parametros = {
    "username": user,
    "question": mensagem,
    "deviceId": "null"
}

while spam:
    response = requests.post(url, verify=False, json=parametros)

    if response.status_code == 200:
        print("Enviado com sucesso!")
    else:
        print("Requisição invalida. Esperando 15 segundos antes de reenviar...")
        time.sleep(15)