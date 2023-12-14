# Importación de módulos necesarios para el cifrado, generación de números aleatorios y manejo de archivos.
import pyAesCrypt
import numpy as np
import hashlib
from scipy.interpolate import lagrange
import io
import zipfile

# Función para cifrar un archivo.
def cypher(pwd, inputName ,file_stream ,total_evs=3, min_points=2):
    # Verifica que el número de evaluaciones sea suficiente para el polinomio.
    try:
        if total_evs >= min_points:
            
            # Genera una semilla a partir de una contraseña para la reproducibilidad de los números aleatorios.
            hashed_seed = int(hashlib.sha256(pwd.encode()).hexdigest(), 16) % (2**32 - 1)
            np.random.seed(hashed_seed)

            # Crea un polinomio de grado 'min_points - 1'.
            poly = np.poly1d(np.random.rand(min_points))

            # Evalúa el polinomio en puntos aleatorios.
            evals = [(x, poly(x)) for x in np.random.rand(total_evs)]

            # Usa el último coeficiente del polinomio como clave de cifrado.
            cypher_key = np.round(poly.coeffs[-1],6)
            print("key", cypher_key)

            # Configura el tamaño del buffer y prepara el flujo de bytes para el archivo cifrado.
            buffer_size = 64*1024
            encrypted_stream = io.BytesIO()
            file_stream.seek(0)

            # Cifra el flujo del archivo.
            pyAesCrypt.encryptStream(file_stream, encrypted_stream, str(cypher_key), buffer_size)

            # Prepara un archivo zip para almacenar el archivo cifrado y las evaluaciones del polinomio.
            encrypted_stream.seek(0)
            zip_stream = io.BytesIO()
            with zipfile.ZipFile(zip_stream, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.writestr(inputName+".enc", encrypted_stream.getvalue())
                evals_str = '\n'.join([f'{x}, {fx}' for x, fx in evals])
                zip_file.writestr(inputName+'_keys.txt', evals_str)
            zip_stream.seek(0)

            # Retorna el flujo del archivo zip.
            return zip_stream
        else:
            raise Exception("polynomial grade is lower than number of points")
    except TypeError:
        print("Type of file error")

# Función para descifrar un archivo.
def decrypt(encrypted_filestream,evals):
    buffer_size = 64*1024
    decrypted_filestream = io.BytesIO()
    encrypted_filestream.seek(0)

    # Lee las evaluaciones del polinomio desde el archivo y las procesa.
    content = evals.read().decode("utf-8")
    lineas = content.split('\n')
    evals_temp = [vals.split(",") for vals in lineas]
    evals_real = [(float(val[0]), float(val[1])) for val in evals_temp]

    print("EVALS", evals_real)
    # Utiliza la interpolación de Lagrange para reconstruir el último coeficiente del polinomio.
    try_key = lagrange_interpolation(evals_real)

    print("trykey", try_key)

    # Intenta descifrar el flujo del archivo con la clave obtenida.
    try:
        pyAesCrypt.decryptStream(encrypted_filestream, decrypted_filestream ,str(try_key), buffer_size)
        decrypted_filestream.seek(0)

        # Retorna el flujo del archivo descifrado.
        return decrypted_filestream
    except TypeError:
        print("type error")

# Función para realizar la interpolación de Lagrange.
def lagrange_interpolation(puntos):
    # Separa los puntos en coordenadas x e y.
    x = [val[0] for val in puntos]
    y = [val[1] for val in puntos]

    # Realiza la interpolación para cada punto y suma los polinomios resultantes.
    M = len(x)
    poly = np.poly1d(0.0)
    for j in range(M):
        pt = np.poly1d(y[j])
        for k in range(M):
            if k == j: continue
            factor = x[j]-x[k]
            pt *= np.poly1d([1.0, -x[k]])/factor
        poly += pt
    # Retorna el último coeficiente del polinomio resultante.
    
    return np.round(poly.coef[-1],6)
