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
    outputName = request.form['OutputName']
    total_evs = int(request.form['total_evs'])
    min_points = int(request.form['min_points'])

    encrypted_stream, evals = cypher(pwd, file, total_evs, min_points)

    return send_file(encrypted_stream, download_name=outputName+".enc",as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
