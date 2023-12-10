from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from cypher import *

app = Flask(__name__)
CORS(app, expose_headers=["Content-Disposition"])  # Enable CORS

@app.route("/encrypt", methods=['POST'])
def encrypt_endpoint():

    print("si si ")
    file = request.files['file'] 
    print(request.form)
    pwd = request.form['password']
    inputName = request.form['fileName']
    outputName = request.form['OutputName']
    total_evs = int(request.form['total_evs'])
    min_points = int(request.form['min_points'])

    encrypted_stream = cypher(pwd, inputName,file, total_evs, min_points)

    return send_file(encrypted_stream, download_name=outputName+".enc",as_attachment=True)

@app.route("/decrypt", methods=['POST'])
def decrypt_endpoint():

    print("si si ")
    encrypted_file = request.files['encrypted'] 
    evals = request.files['evals']
    inputName = request.form['inputName']
    temp = inputName.split(".")
    final_name = ".".join(temp[:-1])

    decrypted_stream = decrypt(encrypted_file, evals)

    return send_file(decrypted_stream, download_name=final_name,as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
