import React from 'react';
import FileUpload from './components/FileUpload';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Formula 1 Image Classifier</h1>
        <p>Upload a clear image of Carlos Sainz Jr, Charles Leclerc, Daniel Ricciardo, Lewis Hamilton, or Sebastian Vettel and I will identify the driver!</p>
        <FileUpload />
      </header>
    </div>
  );
}

export default App;