import React from 'react'

const Cypher = () => {

  const handleFileInput = (e) => {
    // Access the selected file
    const file = e.target.files[0];

    // Log the file name
    if (file) {
        console.log("Selected file: ", file.name);
    }
};

const postFile = async (fileName) => {
  try {
    const response = await fetch('http://localhost:3001/api/cypher', {
      method: 'POST',
      headers:{
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({fileName: fileName})
    });
    const data = await response.json();
    console.log("response:", data)
  }
  catch(error){
    console.error("Error Posting:", error)
  }
}

  return (
    <div>
      <h1>
      Cypher
      </h1>

    <div className='bg-color-100'>
      <input type="file" onChange={handleFileInput}/>
    </div>

    </div>
  )
}

export default Cypher