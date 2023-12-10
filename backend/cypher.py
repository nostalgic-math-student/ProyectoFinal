import pyAesCrypt
import numpy as np
import hashlib
from scipy.interpolate import lagrange
import io

def cypher(pwd, file_stream ,total_evs=3, min_points=2):

    # generamos polinomio de t = min_points 
    try:
        if total_evs >= min_points:
            hashed_seed = int(hashlib.sha256(pwd.encode()).hexdigest(), 16) % (2**32 - 1)
            
            np.random.seed(hashed_seed)

            poly = 10*np.poly1d(np.random.rand(min_points))
            evals = [(x, poly(x)) for x in 10*np.random.rand(total_evs)]
            cypher_key = np.round(poly.coeffs[-1],5)

            print(poly)
            print(evals)
            print(cypher_key)

            buffer_size = 64*1024
            encrypted_stream = io.BytesIO()
            file_stream.seek(0)

            pyAesCrypt.encryptStream(file_stream, encrypted_stream, str(cypher_key), buffer_size)

            encrypted_stream.seek(0)


            return encrypted_stream, evals

        else:
            raise Exception("polynomial grade is lower than number of points")

    except TypeError:
        print("Type of file error")


def decrypt(encrypted_filestream,evals):
    
    buffer_size = 1024*64
    decrypted_filestream = io.BytesIO()
    encrypted_filestream.seek(0)
    try_key = lagrange_interpolation(evals)
    
    try:
        pyAesCrypt.decryptStream(encrypted_filestream, decrypted_filestream ,str(try_key), 64*1024,len(encrypted_filestream.getvalue()) )
        decrypted_filestream.seek(0)

        return decrypted_filestream

    except TypeError:
        print("TypeError")

def lagrange_interpolation(puntos):
    x = [val[0] for val in puntos]
    y = [val[1] for val in puntos]
    poly = lagrange(x,y)
    return np.round(poly.coef[-1],5)

def encrypt_file(key, source, outputName):
    output =  outputName + ".enc"
    pyAesCrypt.encryptFile(source, output, key)

    return output

def decrypt_file(key,source):
    dfile = source.split(".")
    print(dfile)
    output = dfile[0]+"dec."+dfile[1]
    pyAesCrypt.decryptFile(source,output,key)

    return 