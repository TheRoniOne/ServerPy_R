import sys, subprocess
from flask import Flask, request, jsonify
import json
import pandas as pd

app = Flask(__name__)

locJSON = sys.argv[1]
nombreJSON = sys.argv[2]
locResultado = sys.argv[3]

comandoR = 'Rscript "D:/Datos de Usuario/rgamezv/Downloads/prueba/limpiador.R" "{}" "{}" "{}"'.format(locJSON, nombreJSON, locResultado)

@app.route("/calcularResultado", methods = ["POST"])
def calcularResultado():
    requestJSON = request.get_json(force = True)
    with open("miRequest.json", "w", encoding= "utf8") as file:
        json.dump(requestJSON, file)
    subprocess.run(comandoR)
    dirResultado = '{}/resultado.json'.format(locResultado)
    # with open(dirResultado, "r") as file:
    #     resultado = json.load(file)
    #     print(resultado)

    # Lo leemos con pandas para simular como si fueramos a hacer ML con esa info
    df = pd.read_json(dirResultado)
    print("jsonificado")
    return jsonify(df.to_json(orient= "records"))

if __name__ == "__main__":
    app.run(debug= True)