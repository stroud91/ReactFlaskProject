import React, { useState, useEffect } from "react";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
import { useSelector } from "react-redux";
import { useDispatch } from "react-redux";
import { searchBusinessByName } from "../../store/business";
import "./SearchBar.css";

function SearchBar() {
  const dispatch = useDispatch();
  const history = useHistory();
  const [searchTerm, setSearchTerm] = useState('');
  const [searched, setSearched] = useState(false);
  const searchResults = useSelector((state) => state.business.search?.['queried businesses'] || []);

  const handleChange = (e) => {
    setSearchTerm(e.target.value);
    setSearched(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (searchTerm !== '') {
      await dispatch(searchBusinessByName(searchTerm));
      setSearched(true);
    }
  };

  useEffect(() => {
    if (searched) {
      dispatch(searchBusinessByName(searchTerm));
    }
  }, [dispatch, searchTerm, searched]);

  return (
    <section className='main-search-section'>
      <div className='search-info'>
        <form className='main-search-form' onSubmit={handleSubmit}>
          <input
            className='main-search-input'
            name="search"
            type="text"
            placeholder="Search for your next dining experience"
            value={searchTerm}
            onChange={handleChange}
          />
          <button className='search-button' type='submit'>
            <i className="fas fa-search"></i>
          </button>
        </form>
      </div>
      <div className={`${
        searched && searchResults
          ? "search-results-view"
          : "search-results-hidden"
      }`}>
        {searchResults && searchResults.length > 0 &&
          searchResults.map((business) => (
            <div
              className="search-business"
              onClick={() => history.push(`/business/${business.id}`)}
              key={business.id}
            >
              {business.name}
            </div>
          ))}
        {searched && searchResults.length === 0 && searchTerm.length > 0 && (
          <div>No businesses found, please try again</div>
        )}
      </div>
    </section>
  );
}

export default SearchBar;
