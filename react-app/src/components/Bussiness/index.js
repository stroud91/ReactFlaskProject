import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import * as businessActions from '../../store/business';
import './Business.css';


function BusinessMainPage() {
    const dispatch = useDispatch();
    const businesses = useSelector(state => state.business.list);
    console.log("BUSSINES:", businesses)
    useEffect(() => {
        dispatch(businessActions.getAllBusinesses());
    }, [dispatch]);



    return (
        <ul className='businessMain__grid'>
            {businesses && businesses.map((business) => (
                <li key={business.id} className='businessMain__item'>
                    <li className="businessMain__image">
                        {/* Image will go here */}
                    </li>
                    <li>Name: {business.name}</li>
                    <p>Category: {business.category}</p>
                    <p>Rating: {business.avg_rating}</p>
                    <p>{business.address}, {business.city}, {business.state} {business.zip_code}</p>
                    <p>{business.phone_number}</p>
                    <Link to={`/business/${business.id}`}>View More</Link>
                </li>
            ))}
        </ul>
    );
}

export default BusinessMainPage;
