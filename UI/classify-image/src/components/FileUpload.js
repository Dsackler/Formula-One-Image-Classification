import React, { useCallback, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import './FileUpload.css';

const FileUpload = () => {
  const [serverResponse, setServerResponse] = useState(null);
  const onDrop = useCallback(async (acceptedFiles) => {
    const file = acceptedFiles[0];

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post('http://127.0.0.1:5000/classify_image', formData, {
          headers: {
            'Content-Type': 'multipart/form-data', // Ensure proper content type
          },
        });
        console.log('Server Response:', response.data);
        const formattedName = response.data[0].split('_').map((word) => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
        setServerResponse(formattedName)
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div>
      <div className="ImageSection">
        <img src="/images/carlos_pic.jpg" alt="Driver 1" />
        <img src="/images/charles_pic.jpg" alt="Driver 2" />
        <img src="/images/daniel_pic.jpg" alt="Driver 3" />
        <img src="/images/lewis_pic.jpg" alt="Driver 4" />
        <img src="/images/seb_pic.jpg" alt="Driver 4" />
      </div>
        <div {...getRootProps()} className={`dropzone ${isDragActive ? 'active' : ''}`}>
          <input {...getInputProps()} />
          <p>Drag & drop a file here, or click to select a file</p>
      </div>
      {serverResponse && (
        <div>
          <h2>You uploaded a picture of:</h2>
          <h3>{serverResponse}</h3>
        </div>
      )}
    </div>
    
  );
};

export default FileUpload;