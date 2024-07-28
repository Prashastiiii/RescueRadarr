import React from 'react';
import './Home.css';

const Home = () => {
  const handleEarthquakeDetectionClick = () => {
    window.location.href = 'http://localhost:5001'; // URL where your Flask app is running
  };
  
  const handleTsunamiDetectionClick = () => {
    window.location.href = 'http://localhost:5002'; // URL where your Flask app is running
  };
  const handleFloodDetectionClick = () => {
    window.location.href = 'http://localhost:5000'; // URL where your Flask app is running
  };

  return (
    <div className="home">
      <h2>Disaster Detection</h2>
      <div className="buttons">
        <button onClick={handleEarthquakeDetectionClick}>Earthquake Detection</button>
        <button onClick={handleTsunamiDetectionClick}>Tsunami Detection</button>
        <button onClick={handleFloodDetectionClick}>Flood Detection</button>
      </div>
    </div>
  );
};

export default Home;
