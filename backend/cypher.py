import pyAesCrypt
import numpy as np
import hashlib
from scipy.interpolate import lagrange
import io
import zipfile

def cypher(pwd, inputName ,file_stream ,total_evs=3, min_points=2):

    # generamos polinomio de t = min_points 
    try:
        if total_evs >= min_points:
            hashed_seed = int(hashlib.sha256(pwd.encode()).hexdigest(), 16) % (2**32 - 1)

            np.random.seed(hashed_seed)
            poly = np.poly1d(np.random.rand(min_points))
            evals = [(x, poly(x)) for x in np.random.rand(total_evs)]
            cypher_key = np.round(poly.coeffs[-1],6)

            print(poly)
            print(evals)
            print(cypher_key)

            buffer_size = 64*1024
            encrypted_stream = io.BytesIO()
            file_stream.seek(0)

            pyAesCrypt.encryptStream(file_stream, encrypted_stream, str(cypher_key), buffer_size)

            encrypted_stream.seek(0)

            zip_stream = io.BytesIO()

            with zipfile.ZipFile(zip_stream, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.writestr(inputName+".enc", encrypted_stream.getvalue())

                evals_str = '\n'.join([f'{x}, {fx}' for x, fx in evals])
                zip_file.writestr('evaluations.txt', evals_str)

            zip_stream.seek(0)

            return zip_stream

        else:
            raise Exception("polynomial grade is lower than number of points")

    except TypeError:
        print("Type of file error")


def decrypt(encrypted_filestream,evals):
    
    buffer_size = 64*1024
    decrypted_filestream = io.BytesIO()
    encrypted_filestream.seek(0)
    content = evals.read().decode("utf-8")
    lineas = content.split('\n')

    evals_temp = [vals.split(",") for vals in lineas]
    evals_real = [(float(val[0]), float(val[1])) for val in evals_temp]
    
    try_key = lagrange_interpolation(evals_real)

    print("TRYKEY", try_key)
    
    try:
        pyAesCrypt.decryptStream(encrypted_filestream, decrypted_filestream ,str(try_key), buffer_size,len(encrypted_filestream.getvalue()) )
        print(decrypted_filestream, "decfy")
        decrypted_filestream.seek(0)

        return decrypted_filestream

    except TypeError:
        print("type error")

def lagrange_interpolation(puntos):
    x = [val[0] for val in puntos]
    y = [val[1] for val in puntos]

    M = len(x)
    poly = np.poly1d(0.0)
    for j in range(M):
        pt = np.poly1d(y[j])
        for k in range(M):
            if k == j:
                continue
            factor = x[j]-x[k]
            pt *= np.poly1d([1.0, -x[k]])/factor
        poly += pt
    return np.round(poly.coef[-1],6)