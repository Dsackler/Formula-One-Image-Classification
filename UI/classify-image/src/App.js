import React from 'react';
import FileUpload from './components/FileUpload';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Drag and Drop File Upload</h1>
        <FileUpload />
      </header>
    </div>
  );
}

export default App;