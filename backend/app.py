# Importación de módulos Flask para construir la aplicación web y manejar las peticiones HTTP.
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from cypher import *  # Importa las funciones de cifrado y descifrado previamente definidas.

app = Flask(__name__)
CORS(app, expose_headers=["Content-Disposition"])  # Habilita CORS (Cross-Origin Resource Sharing) para la app.

# Endpoint para cifrar un archivo. Utiliza el método POST para recibir los datos.
@app.route("/encrypt", methods=['POST'])
def encrypt_endpoint():
    # Recibe el archivo y otros datos necesarios para el proceso de cifrado desde el formulario.
    file = request.files['file'] 
    pwd = request.form['password']
    inputName = request.form['fileName']
    outputName = request.form['OutputName']
    total_evs = int(request.form['total_evs'])  # Número total de evaluaciones.
    min_points = int(request.form['min_points'])  # Número mínimo de puntos para el polinomio.

    # Llama a la función 'cypher' para cifrar el archivo.
    print("aqui", pwd)
    encrypted_stream = cypher(pwd, inputName, file, total_evs, min_points)

    # Envía el archivo cifrado como respuesta, con la opción de descargarlo.
    return send_file(encrypted_stream, download_name=outputName+".enc", as_attachment=True)

# Endpoint para descifrar un archivo. Utiliza el método POST para recibir los datos.
@app.route("/decrypt", methods=['POST'])
def decrypt_endpoint():
    # Recibe el archivo cifrado y las evaluaciones necesarias para el proceso de descifrado.
    encrypted_file = request.files['encrypted']
    evals = request.files['evals']
    inputName = request.form['inputName']

    # Prepara el nombre del archivo final removiendo la extensión.
    temp = inputName.split(".")
    final_name = ".".join(temp[:-1])

    print("final name es", final_name)

    # Llama a la función 'decrypt' para descifrar el archivo.
    decrypted_stream = decrypt(encrypted_file, evals)

    # Envía el archivo descifrado como respuesta, con la opción de descargarlo.
    return send_file(decrypted_stream, download_name=final_name, as_attachment=True)

# Inicia la aplicación en el puerto 3000, accesible desde cualquier dirección IP.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
