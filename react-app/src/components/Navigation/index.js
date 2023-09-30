import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import SearchBar from '../SearchBar'
import './Navigation.css';
import yelpSmall from '../../images/yelp.png'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className="nav-container">
		<div className="nav-left">
		  <NavLink exact to="/">
			<img className='small-logo' src={yelpSmall} alt="" />
		  </NavLink>
		</div>
		<div className='searchbar'>< SearchBar /></div>
		{isLoaded && (
		  <div>
			<ProfileButton user={sessionUser} />
		  </div>
		)}
	  </div>
	);
}

export default Navigation;
