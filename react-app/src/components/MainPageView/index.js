import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { getBusinesses } from '../../store/business'
import React, { useState, useEffect } from "react";
import RecentActivity from "../RecentActivity"
import { Link } from "react-router-dom/cjs/react-router-dom.min";
import SearchBar from "../SearchBar"

function MainPage() {

  const [search, setSearch] = useState('');
  const [businesses, setBusinesses] = useState([])


  const handleSubmit = (e) => {
    e.preventDefault();

  }

  const handleChange = (e) => {
    setSearch(e.target.value);
  }

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/business/");
      const responseData = await response.json();
      setBusinesses(responseData);
    }
    fetchData();
  }, []);

  return businesses ? (
    <div className='main-container'>
      <header className='main-header'>
      </header>
      < RecentActivity />
      <footer className='main-footer'>
        <p>&copy; 2023 Business Directory</p>
      </footer>
    </div>
  ) : (
    <div>Loading...</div>
  );
}

export default MainPage;
