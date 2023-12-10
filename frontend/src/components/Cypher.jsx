import React, { useState } from 'react'
import { saveAs } from 'file-saver';
import axios from 'axios';

const Cypher = () => {

  const [file, setFile] = useState(null);
  const [password, setPassword] = useState('');
  const [outputName, setOutputName] = useState('');
  const [totalEvs, setTotalEvs] = useState(0);
  const [minPoints, setMinPoints] = useState(0);

  const handleFileInput = (e) => {
    setFile(e.target.files[0]);
  };

  const handlePasswordChange = (e) => {
    setPassword(e.target.value);
  };

  const handleOutputNameChange = (e) => {
    setOutputName(e.target.value);
  };

  const handleTotalEvsChange = (e) => {
    setTotalEvs(e.target.value);
  };

  const handleMinPointsChange = (e) => {
    setMinPoints(e.target.value);
  };

const postFile = async (fileName) => {
  
  const formData = new FormData();
  formData.append('file', file);
  formData.append('password', password);
  formData.append('OutputName', outputName);
  formData.append('total_evs', totalEvs);
  formData.append('min_points', minPoints);

  try {
    const response = await axios.post('http://127.0.0.1:5000/encrypt', formData, {
      responseType: 'blob', // Importante para manejar la respuesta como un blob
    });

    const blob = new Blob([response.data], {type: 'application/octet-stream'})
    saveAs(blob, outputName+".enc")
  }
  catch(error){
    console.error("Error Posting:", error)
  }
}

  return (
    <div>
      <h1>Cypher</h1>
      <div className='bg-color-100'>
        <input type="file" onChange={handleFileInput} />
        <input type="text" placeholder="Password" onChange={handlePasswordChange} />
        <input type="text" placeholder="Output Name" onChange={handleOutputNameChange} />
        <input type="number" placeholder="Total EVs" onChange={handleTotalEvsChange} />
        <input type="number" placeholder="Min Points" onChange={handleMinPointsChange} />
        <button className='btn btn-primary' onClick={postFile}>
          Send
        </button>
      </div>
    </div>
  )
}

export default Cypher