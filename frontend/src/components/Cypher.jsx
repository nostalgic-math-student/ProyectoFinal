import React, { useState } from 'react';
import { saveAs } from 'file-saver'; 
import axios from 'axios'; // Módulo para realizar peticiones HTTP.

const Cypher = () => {
  // Estados para manejar el archivo, la contraseña, el nombre de salida, y los parámetros del cifrado.
  const [file, setFile] = useState(null);
  const [password, setPassword] = useState('');
  const [outputName, setOutputName] = useState('');
  const [totalEvs, setTotalEvs] = useState(0);
  const [minPoints, setMinPoints] = useState(0);

  // Manejadores de eventos para actualizar los estados con los valores ingresados por el usuario.
  const handleFileInput = (e) => setFile(e.target.files[0]);
  const handlePasswordChange = (e) => setPassword(e.target.value);
  const handleOutputNameChange = (e) => setOutputName(e.target.value);
  const handleTotalEvsChange = (e) => setTotalEvs(e.target.value);
  const handleMinPointsChange = (e) => setMinPoints(e.target.value);

  // Función para enviar el archivo y los datos de cifrado al servidor y descargar el archivo cifrado.
  const postFile = async () => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('password', password);
    formData.append('OutputName', outputName);
    formData.append('total_evs', totalEvs);
    formData.append('min_points', minPoints);
    formData.append('fileName', file.name);

    try {
      const response = await axios.post('http://127.0.0.1:5000/encrypt', formData, {
        responseType: 'blob', // Configuración para manejar la respuesta como un blob.
      });
      const blob = new Blob([response.data], {type: 'application/octet-stream'});
      saveAs(blob, outputName + ".zip");
    }
    catch(error) {
      console.error("Error Posting:", error);
    }
  }

  // Renderiza el componente con campos de entrada para los datos de cifrado y un botón para enviar.
  return (
    <div className='mx-auto p-3'>
      <h1 className='font-bold text-3xl'>Cypher</h1>
      <div className='bg-color-100'>
        <input type="file" onChange={handleFileInput} />
        <input type="text" placeholder="Password" onChange={handlePasswordChange} />
        <input type="text" placeholder="Output Name" onChange={handleOutputNameChange} />
        <input type="number" placeholder="Total Evaluations" onChange={handleTotalEvsChange} />
        <input type="number" placeholder="Min Points" onChange={handleMinPointsChange} />
        <button className='btn btn-primary' onClick={postFile}>
          Send
        </button>
      </div>
    </div>
  )
}

export default Cypher
