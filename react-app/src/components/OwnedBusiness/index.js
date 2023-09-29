import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import * as businessActions from '../../store/business';

function OwnedBusinesses() {
    const dispatch = useDispatch();

    const currentUser = useSelector(state => state.session.user);

    const businesses = useSelector(state => state.business.list);

    useEffect(() => {
        dispatch(businessActions.getAllBusinesses());
    }, [dispatch]);

    const ownedBusinesses = businesses.filter(
        business => business.owner_id === currentUser.id
    );

    if(ownedBusinesses.length === 0){
        return <div>Currently you have no businesses created. Will you want to create one?</div>
    }

    return (
        <ul className='businessMain__grid'>
            {ownedBusinesses && ownedBusinesses.map((business) => (
                <li key={business.id} className='businessMain__item'>
                    <p>Name: {business.name}</p>
                    <li className="businessMain__image">
                        {/* Image will go here */}
                    </li>
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

export default OwnedBusinesses;
