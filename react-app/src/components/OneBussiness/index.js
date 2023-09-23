import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchOneBusiness } from '../../store/business';
import { useParams } from 'react-router-dom';
import './OneBussiness.css';

function BusinessDetail() {
    const dispatch = useDispatch();
    const { id } = useParams();
    const business = useSelector(state => state.business.selectedBusiness);

    useEffect(() => {
        dispatch(fetchOneBusiness(id));
    }, [dispatch, id]);

    if (!business) return <div>Loading...</div>;

    return (
        <div>
            <h1>{business.name}</h1>
            <p>Address: {business.address}</p>
            <p>Phone Number: {business.phone_number}</p>
            <p>Website: <a href={business.website} target="_blank" rel="noopener noreferrer">{business.website}</a></p>
            <p>Category: {business.category}</p>
            <p>Type: {business.type}</p>
            <p>City: {business.city}, {business.state} {business.zip_code}</p>
            <div>
                Average Rating: {business.avg_rating}
            </div>

            {business?.reviews?.map(review => (
                <div key={review.id}>
                    <p>{review.review_body}</p>
                    <p>Rating: {review.rating}</p>
                    <p>Created At: {new Date(review.created_at).toLocaleString()}</p>
                    <p>Updated At: {new Date(review.updated_at).toLocaleString()}</p>
                </div>
            ))}
        </div>
    );
}

export default BusinessDetail;
