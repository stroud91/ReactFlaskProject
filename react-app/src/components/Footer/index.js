import React from 'react';
import './Footer.css';
import githubLogo from '../Image/logo_github.svg';

const Footer = () => {
  return (
    <footer className="footer-container">
      <div className="authors-section">
        <h4>Project Authors</h4>
        <ul>
          <li>
            <a href="https://github.com/stroud91" target="_blank" rel="noopener noreferrer">
              <img src={githubLogo} alt="GitHub" className="github-logo" />
              Ledian Fekaj
            </a>
          </li>
          <li>
            <a href="https://github.com/ejorgji1" target="_blank" rel="noopener noreferrer">
              <img src={githubLogo} alt="GitHub" className="github-logo" />
              Enea Jorgji
            </a>
          </li>
          <li>
            <a href="https://github.com/gjinhung" target="_blank" rel="noopener noreferrer">
              <img src={githubLogo} alt="GitHub" className="github-logo" />
              Gar Hung
            </a>
          </li>
        </ul>
      </div>
      <div className="other-projects-section">
        <h4>Check out our other projects</h4>
        <ul>
          <li>
            <a href="https://github.com/ejorgji1/Capstone-Project" target="_blank" rel="noopener noreferrer">
              Luxury Watches
            </a>
          </li>
          <li>
            <a href="https://github.com/stroud91/DietCrusherProject" target="_blank" rel="noopener noreferrer">
              Diet Crusher
            </a>
          </li>
          <li>
            <a href="https://github.com/gjinhung/cityrafinal" target="_blank" rel="noopener noreferrer">
              City Ra
            </a>
          </li>
        </ul>
      </div>
    </footer>
  );
};

export default Footer;
