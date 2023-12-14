import React, { useState } from 'react'
import { saveAs } from 'file-saver'; 
import axios from 'axios'; // Modulo para realizar peticiones HTTP

const DeCypher = () => {

  // Estados para gestionar el archivo, las evaluaciones y el nombre del archivo.
  const [file, setFile] = useState(null);
  const [evals, setEvals] = useState(null);
  const [inputName, setInputName] = useState('');

  // Manejadores para actualizar el estado con el archivo y las evaluaciones seleccionadas.
  const handleFileInput = (e) => {
    setFile(e.target.files[0]);
    const originalFileName = e.target.files[0].name;
    const modifiedFileName = originalFileName.replace(/\.enc$/, '');
    setInputName(modifiedFileName);
  };
  
  const handleEvalInput = (e) => {
    setEvals(e.target.files[0]);
  };

  // Función para enviar el archivo cifrado y las evaluaciones al servidor y descargar el archivo descifrado.
  const postEncryptedFile = async () => {
    const formData = new FormData();
    formData.append('encrypted', file);
    formData.append('evals', evals);
    formData.append('inputName', inputName);

    try {
      const response = await axios.post('http://127.0.0.1:5000/decrypt', formData, {
        responseType: 'blob', // Configuración para manejar la respuesta como un blob.
      });

      // Procesa la respuesta y utiliza file-saver para guardar el archivo descifrado.
      const blob = new Blob([response.data], {type: 'application/octet-stream'});
      saveAs(blob, inputName);
    }
    catch(error){
      console.error("Error Posting:", error);
    }
  }

  // Renderiza el componente con campos de entrada para el archivo y las evaluaciones, y un botón para enviar.
  return (
    <div>
      <h1 className='text-3xl font-bold'>DeCypher</h1>
      <div className='bg-color-100'>
        <div className='mx-auto p-2'>
          Encrypted File: --
          <input type="file" onChange={handleFileInput} />
        </div>
        <div className='mx-auto p-2'>
          Keys file: --
          <input type="file" onChange={handleEvalInput} />
        </div>
        <button className='btn btn-primary' onClick={postEncryptedFile}>
          Send
        </button>
      </div>
    </div>
  )
}

export default DeCypher
