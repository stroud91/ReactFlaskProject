import React from "react";
import { NavLink, useLocation } from 'react-router-dom';
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import SearchBar from "../SearchBar";
import "./Navigation.css";
import yelpSmall from "../../images/yelp.png";
import yelpWhite from "../../images/yelpingLogo_white.png"

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const location = useLocation();

  return (
    <div className={location.pathname !== '/' ? ('nav-container') : ("nav-container-main")}>
      <div className="nav-left">
        <NavLink exact to="/" className="logo_link">
          <img className="small-logo" src={location.pathname !== '/' ? (yelpSmall) : (yelpWhite)} alt="" />
        </NavLink>
      </div>
      {/* {location.pathname === ‘/’ && ( */}
      <div className='searchbar'>
        <SearchBar />
      </div>
      {/* )} */}
      {isLoaded && (
        <div>
          <ProfileButton user={sessionUser} />
        </div>
      )}
    </div>
  );
}

export default Navigation;
