import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import OpenModalButton from "../OpenModalButton";
import ImagesModal from '../Image/GetImagesModal';
import { fetchOneBusiness } from '../../store/business';
import { useParams } from 'react-router-dom';
import * as imageActions from "../../store/images";
import noImage from "../../images/no-image.png"
import './OneBussiness.css';
import '../Image/ImagesForm.css'
// import LoginFormModal from '../LoginFormModal';

function BusinessDetail() {
    // const history = useHistory();
    const dispatch = useDispatch();
    const { id } = useParams();
    const business = useSelector(state => state.business.selectedBusiness);
    // const currentUser = useSelector(state => state.session.user);
    useEffect(() => {
        dispatch(fetchOneBusiness(id));
        dispatch(imageActions.images(id))
    }, [dispatch, id]);


    if (!business) return <div>Loading...</div>;

    // function handleEdit(businessId) {

    //     history.push(`/business/${business.id}/edit`);
    // }

    // function handleDelete(businessId) {

    //     history.push(`/business/${business.id}/edit`);
    // }
    // let buttons;

    // if (currentUser) {
    //     buttons = (
    //         <div className='business-buttons-conditional'>
    //             <button className='general-button' onClick={() => handleEdit(business.id)}>Edit</button>
    //             <button className='general-button' onClick={() => handleDelete(business.id)}>Delete</button>
    //         </div>
    //     );
    // } else {
    //     buttons = null;
    // }

    let image_gallery

    console.log(business.images)

    if (business.images.length) {
        image_gallery = business.images.map((image) => {
            const { id, image_url } = image
            return (
                <img src={image_url} alt={`imageId_${id}`}></img>
            )
        })
    } else {
        image_gallery = (
            <img src={noImage} alt={`imageId_${id}`}></img>
        )
    }


    return (
        <div>
            <h1>{business.name}</h1>
            <div className='scroll-gallery'>
                <div className='scroll-container'>
                    {image_gallery}
                </div>
                <span
                    className="see-images">
                    <OpenModalButton
                        buttonText={`See all ${business.images.length} photos`}
                        modalComponent={<ImagesModal
                            bus_data={business} />}
                        id={'see-img'}
                    />
                </span>
            </div>
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
