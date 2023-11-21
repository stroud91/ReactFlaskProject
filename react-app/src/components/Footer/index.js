import React from 'react';
import './Footer.css';
const Footer = () => {
  return (
    <footer className="footer-container">
      <div className="authors-section">
        <h4>Project Authors</h4>
        <ul>
          <li><a href="https://github.com/author1" target="_blank" rel="noopener noreferrer">Ledian Fekaj</a></li>
          <li><a href="https://github.com/author2" target="_blank" rel="noopener noreferrer">Enea Jorgji</a></li>
          <li><a href="https://github.com/author3" target="_blank" rel="noopener noreferrer">Gar Hung</a></li>

        </ul>
      </div>
      <div className="other-projects-section">
        <h4>Check out our other projects</h4>
        <ul>
          <li><a href="" target="_blank" rel="noopener noreferrer">Luxury Watches</a></li>
          <li><a href="" target="_blank" rel="noopener noreferrer">Diet Crusher</a></li>
          <li><a href="" target="_blank" rel="noopener noreferrer">Project 3</a></li>

        </ul>
      </div>
    </footer>
  );
};

export default Footer;
