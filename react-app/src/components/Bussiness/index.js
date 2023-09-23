import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import * as businessActions from '../../store/business';
import './Business.css';


function BusinessMainPage() {
    const dispatch = useDispatch();

    useEffect(() => {
        dispatch(businessActions.getAllBusinesses());
    }, [dispatch]);

    const businesses = useSelector(state => state.business.list);

    return (
        <div className='businessMain__grid'>
            {businesses && businesses.map((business) => (
                <div key={business.id} className='businessMain__item'>
                    <div className="businessMain__image">
                        {/* Image will go here */}
                    </div>
                    <h2>{business.name}</h2>
                    <p>Category: {business.category}</p>
                    <p>Rating: {business.avg_rating}</p>
                    <p>{business.address}, {business.city}, {business.state} {business.zip_code}</p>
                    <p>{business.phone_number}</p>
                    <Link to={`/business/${business.id}`}>View More</Link>
                </div>
            ))}
        </div>
    );
}

export default BusinessMainPage;
