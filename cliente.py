import requests
import json

url = "http://localhost:5000/calcularResultado"
with open("telecom.json", "r") as file:
    miJSON = json.load(file)

resultado = requests.post(url, json=miJSON)
print(resultado.json())
with open("miResultado.json", "w") as file:
    file.write(resultado.json())