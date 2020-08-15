import sys, subprocess
import json
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

locJSON = sys.argv[1] # suponiendo que quieras guardar el json recibido en un folder distinto
nombreJSON = sys.argv[2] # para q puedas diferenciar resultados de usuarios usando el nombre del json
locResultado = sys.argv[3] # suponiendo que quieras guardar el resultado del procesamiento en un folder distinto

comandoR = 'Rscript "C:/Users/RoniD/Downloads/serverP+R/limpiador.R" "{}" "{}" "{}"'.format(locJSON, nombreJSON, locResultado)

@app.route("/calcularResultado", methods = ["POST"])
def calcularResultado():
    requestJSON = request.get_json(force = True)
    with open("miRequest.json", "w", encoding= "utf8") as file:
        json.dump(requestJSON, file)
    subprocess.run(comandoR)
    dirResultado = "{}/resultado.json".format(locResultado)
    # with open(dirResultado, "r") as file:
    #     resultado = json.load(file)
    #     print(resultado)

    # Lo leemos con pandas para simular como si fueramos a hacer ML con esa info
    df = pd.read_json(dirResultado)
    print("jsonificado")
    return jsonify(df.to_json(orient= "records"))

if __name__ == "__main__":
    app.run(debug= True)