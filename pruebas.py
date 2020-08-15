import subprocess
import sys

locJSON = sys.argv[1] # suponiendo que quieras guardar el json recibido en un folder distinto
nombreJSON = sys.argv[2] # para q puedas diferenciar resultados de usuarios usando el nombre del json
locResultado = sys.argv[3] # suponiendo que quieras guardar el resultado del procesamiento en un folder distinto

comandoR = 'Rscript "C:/Users/RoniD/Downloads/serverP+R/limpiador.R" "{}" "{}" "{}"'.format(locJSON, nombreJSON, locResultado)

print(comandoR)
subprocess.run(comandoR)