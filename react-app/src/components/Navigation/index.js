import React from "react";
import { NavLink, useLocation } from 'react-router-dom';
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import SearchBar from "../SearchBar";
import "./Navigation.css";
import yelpSmall from "../../images/yelp.png";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const location = useLocation();

  return (
    <div className="nav-container">
      <div className="nav-left">
        <NavLink exact to="/">
          <img className="small-logo" src={yelpSmall} alt="" />
        </NavLink>
      </div>
      {location.pathname === '/' && (
        <div className='searchbar'>
          <SearchBar />
        </div>
      )}
      {isLoaded && (
        <div>
          <ProfileButton user={sessionUser} />
        </div>
      )}
    </div>
  );
}

export default Navigation;
