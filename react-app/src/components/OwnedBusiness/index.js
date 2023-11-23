import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';
import noImage from "../../images/no-image.png"
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


    if (ownedBusinesses.length === 0) {
        return <div>Currently you have no businesses created. Will you want to create one?</div>
    }

    let getPrev = (business) => {
        let res
        if (business.images.length) {
            let arr = business.images
            arr.forEach((bus) => {
                if (bus.image_preview) {
                    res = bus.image_url
                }
            })
        } else {
            res = noImage
        }
        return res
    }

    return (
        <ul className='businessMain__grid'>
            {ownedBusinesses && ownedBusinesses.map((business) => (
                <li key={business.id} className='businessMain__item'>
                    <p className="businessMain_name">{business.name}</p>
                    <div className="businessMain__image">
                        <img src={getPrev(business)}
                            className='busImg'
                            alt={business.name}
                            key={business.id}
                        />
                    </div>
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
