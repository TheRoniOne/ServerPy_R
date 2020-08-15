# Server Python + R

## Descripcion:
Este es un repo de pruebas que busca crear un servidor simple y un flujo entre Python y R
Python sera usado para hacer la llamada a R por medio de un subproceso
El script tmb instala las librerias necesarias de R (tidyverse, jsonlite)

## Para ejecutar el script de Python, ejecutar el comando:
python server.py "direccion del folder donde se guardara el json recibido por el servidor" "nombre con el que se guardara el json recibido por el servidor" "C:/Users/RoniD/Downloads/serverP+R/resultados"

### Importante:
Para que funcione correctamente, se debe iniciar el servidor desde un cmd fuera de vscode

## Ejemplos:
- python server.py "C:/Users/RoniD/Downloads/serverP+R" "requestRecibido.json" "C:/Users/RoniD/Downloads/serverP+R/resultados"

- Rscript limpiador.R "C:/Users/RoniD/Downloads/serverP+R" "telecom.json" "C:/Users/RoniD/Downloads/serverP+R/resultados"
