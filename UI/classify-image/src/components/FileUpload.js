import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const FileUpload = () => {
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
      } catch (error) {
        console.error('Error uploading file:', error);
      }
    }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div {...getRootProps()} className={`dropzone ${isDragActive ? 'active' : ''}`}>
      <input {...getInputProps()} />
      <p>Drag & drop a file here, or click to select a file</p>
    </div>
  );
};

export default FileUpload;