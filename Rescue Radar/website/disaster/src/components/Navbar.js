import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {

  const handleChatDetectionClick = () => {
    window.location.href = 'http://localhost:5005'; 
  };

  return (
    <nav className="navbar">
      <NavLink to="/about" className="navbar-logo-link">
        <div className="navbar-logo"></div>
      </NavLink>
      <ul className="navbar-menu">
        <li>
          <NavLink to="/" exact className={({ isActive }) => (isActive ? 'active' : '')}>
            Home
          </NavLink>
        </li>
        <li>
          <NavLink className={({ isActive }) => (isActive ? 'active' : '')} onClick={handleChatDetectionClick}>
            ChatBot
          </NavLink>
        </li>
        <li>
          <NavLink to="/education" className={({ isActive }) => (isActive ? 'active' : '')}>
            Education
          </NavLink>
        </li>
        <li>
          <NavLink to="/contacts" className={({ isActive }) => (isActive ? 'active' : '')}>
            Contacts
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
