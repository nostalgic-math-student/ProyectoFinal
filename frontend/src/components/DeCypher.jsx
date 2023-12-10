import React, { useState } from 'react'
import { saveAs } from 'file-saver';
import axios from 'axios';

const DeCypher = () => {

  const [file, setFile] = useState(null);
  const [evals, setEvals] = useState(null);
  const [inputName, setInputName] = useState('');

  const handleFileInput = (e) => {
    setFile(e.target.files[0]);
    setInputName(e.target.files[0].name);
  };
  
  const handleEvalInput = (e) => {
    setEvals(e.target.files[0]);
  };
 
const postEncryptedFile = async (fileName) => {
  
  const formData = new FormData();
  formData.append('encrypted', file);
  formData.append('evals', evals);
  formData.append('inputName', inputName);

  try {
    const response = await axios.post('http://127.0.0.1:5000/decrypt', formData, {
      responseType: 'blob', // Importante para manejar la respuesta como un blob
    });

    const contentDisposition = response.headers['content-disposition'];
    console.log(contentDisposition)
    let finalArrayName = inputName.split(".")
    let finalName = finalArrayName.slice(0,-1).join(".");

    const blob = new Blob([response.data], {type: 'application/octet-stream'})
    saveAs(blob, finalName)
  }
  catch(error){
    console.error("Error Posting:", error)
  }
}

  return (
    <div>
      <h1>DeCypher</h1>
      <div className='bg-color-100'>
        <input type="file" placeholder='Insert encrypted file' onChange={handleFileInput} />
        <input type="file" placeholder='Insert keys file' onChange={handleEvalInput} />
        <button className='btn btn-primary' onClick={postEncryptedFile}>
          Send
        </button>
      </div>
    </div>
  )
}

export default DeCypher