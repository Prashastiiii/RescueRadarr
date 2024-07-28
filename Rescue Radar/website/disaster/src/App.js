import React from 'react';
import { BrowserRouter as Router, Route, Routes, useLocation } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Contacts from './pages/Contacts';
import Education from './pages/Education';
import About from './pages/About';  
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram, faTwitter, faLinkedin } from '@fortawesome/free-brands-svg-icons';
import { faEnvelope, faPhone } from '@fortawesome/free-solid-svg-icons';
import './App.css';

function Footer() {
  const location = useLocation();
  const hideFooter = location.pathname === '/contacts' || location.pathname === '/education';

  return (
    !hideFooter && (
      <footer className="social-icons">
        <a href="https://www.instagram.com" target="_blank" rel="noopener noreferrer">
          <FontAwesomeIcon icon={faInstagram} />
        </a>
        <a href="https://www.twitter.com" target="_blank" rel="noopener noreferrer">
          <FontAwesomeIcon icon={faTwitter} />
        </a>
        <a href="https://www.linkedin.com" target="_blank" rel="noopener noreferrer">
          <FontAwesomeIcon icon={faLinkedin} />
        </a>
        <a href="mailto:someone@example.com" target="_blank" rel="noopener noreferrer">
          <FontAwesomeIcon icon={faEnvelope} />
        </a>
        <a href="tel:+1234567890" target="_blank" rel="noopener noreferrer">
          <FontAwesomeIcon icon={faPhone} />
        </a>
      </footer>
    )
  );
}

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/contacts" element={<Contacts />} />
            <Route path="/education" element={<Education />} />
            <Route path="/about" element={<About />} /> {}
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
