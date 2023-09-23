import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import { getBusinesses } from '../../store/business'
import React, { useState, useEffect } from "react";



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
        <h1>Welcome to Our Business Directory</h1>
      </header>
      <section className='main-search-section'>
        <div className='search-info'>
          <h4>Search for businesses by name, category, address, or phone number:</h4>
          <form className='main-search-form' onSubmit={handleSubmit}>
            <input
              className='main-search-input'
              name="search"
              type="text"
              placeholder="Plumbing, Electrician, Construction, Floorcare, etc."
              value={search}
              onChange={handleChange}
            />
            <button className='search-button' type='submit'>

            </button>
          </form>
        </div>
      </section>
      <footer className='main-footer'>
        <p>&copy; 2023 Business Directory</p>
      </footer>
    </div>
  ) : (
    <div>Loading...</div>
  );
}

export default MainPage;
