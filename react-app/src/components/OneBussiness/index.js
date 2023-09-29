import React, { useEffect,useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { fetchOneBusiness,deleteBusiness } from '../../store/business';
import { useParams, useHistory } from 'react-router-dom';
import DeleteModal from '../DeleteBusinessModal';
import { useModal } from '../../context/Modal';
import './OneBussiness.css';

function BusinessDetail() {
    const history = useHistory();
    const dispatch = useDispatch();
    const { id } = useParams();
    const business = useSelector(state => state.business.selectedBusiness);
    const currentUser = useSelector(state => state.session.user);
    const { setModalContent, closeModal } = useModal();
    const [showConfirmModal, setShowConfirmModal] = useState(false);

    useEffect(() => {
        dispatch(fetchOneBusiness(id));
    }, [dispatch, id]);

    if (!business) return <div>Loading...</div>;

    const handleDelete = () => {

        setShowConfirmModal(true);
      };

    const handleEdit = () => {
        // e.preventDefault();
        history.push(`/business/${business.id}/edit`);
    }

    return (
        <div className='business-detail-container'>
            {/* Side Panel for Contact Info */}
            <div className='business-side-panel'>
                <h2>Contact Information</h2>
                <p>Address: {business.address}</p>
                <p>Phone Number: {business.phone_number}</p>
                <p>City: {business.city}, {business.state} {business.zip_code}</p>
                <p>Website: <a href={business.website} target="_blank" rel="noopener noreferrer">{business.website}</a></p>
            </div>

            {/* Main Business Info */}
            <div className='business-info'>
                <h1>{business.name}</h1>
                <p>Category: {business.category}</p>
                <p>Type: {business.type}</p>
                <div>Average Rating: {business.avg_rating}</div>

                {business?.reviews?.map(review => (
                    <div key={review.id} className="review">
                        <p>{review.review_body}</p>
                        <p>Rating: {review.rating}</p>
                        <p>Review posted at: {new Date(review.created_at).toLocaleString()}</p>
                        {/* <p>Updated At: {new Date(review.updated_at).toLocaleString()}</p> */}
                    </div>
                ))}

                {currentUser.id === business.id &&
                <div className='business-buttons-conditional'>
                    <button className='general-button' onClick={() => handleEdit(business.id)}>Edit</button>
                    <button className='general-button' onClick={() => handleDelete(business.id)}>Delete</button>
                </div>}
            </div>
        </div>
    );
}

export default BusinessDetail;
