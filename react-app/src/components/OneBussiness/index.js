import React, { useEffect,useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import PostReviewModal from "../PostReviewModal";
import OpenModalButton from "../OpenModalButton";
import { allReviewsThunk, oneBussinessReviewsThunk } from "../../store/review";
import DeleteReviewModal from "../DeleteReviewModal";
import EditReviewModal from "../EditReviewModal";
import ImagesModal from '../Image/GetImagesModal';
import { fetchOneBusiness } from '../../store/business';
import { useParams, useHistory  } from 'react-router-dom';
import { useModal } from '../../context/Modal';
import * as imageActions from "../../store/images";
import noImage from "../../images/no-image.png"
import './OneBussiness.css';
import '../Image/ImagesForm.css'

function BusinessDetail() {
  const history = useHistory();
  const dispatch = useDispatch();

  const { id } = useParams();
  const business = useSelector((state) => state.business.selectedBusiness);
  const user = useSelector((state) => state.session.user);
  const reviews = useSelector((state) => state.reviews.currentBusinessReviews);
  const currentUser = useSelector(state => state.session.user);
  const { setModalContent, closeModal } = useModal();
  const [showConfirmModal, setShowConfirmModal] = useState(false);
  console.log("THIS IS BUSINESS", business);
  console.log("THIS IS USER", user);
  console.log("THIS IS REVIEWS", reviews);
  useEffect(() => {
    dispatch(fetchOneBusiness(id));
    dispatch(oneBussinessReviewsThunk(id));
    dispatch(allReviewsThunk())
    dispatch(imageActions.images(id))
  }, [dispatch, id]);

  if (!business) return <div>Loading...</div>;
  if (!reviews) {
    return <div>Loading Reviews...</div>;
  }

  const handleDelete = () => {

    setShowConfirmModal(true);
  };

const handleEdit = (e) => {
    e.preventDefault();
    history.push(`/business/${business.id}/edit`);
}


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

                {currentUser.id === business.id &&
                <div className='business-buttons-conditional'>
                    <button className='general-button' onClick={() => handleEdit(business.id)}>Edit</button>
                    <button className='general-button' onClick={() => handleDelete(business.id)}>Delete</button>
                </div>}
            </div>
        </div>
      <div className="postYourReview">
        {user &&
          user.id !== business.owner_Id &&
          !reviews.restaurant_reviews.some(
            (review) => review.user_id === user.id
          ) && (
            <OpenModalButton
              buttonText="Post Your Review"
              modalComponent={<PostReviewModal id={id} user={user} />}
            />
          )}
      </div>

      {reviews &&
        reviews.restaurant_reviews
          .map((review) => (
            // <div className="individualReview" key={`review-${review.id}`}>
            //   {/* <div className="reviewUser">{review.User?.firstName}</div> */}
            //   <div className="createdAt">{(review.created_At)}</div>
            //   <div className="reviewDescription">{review.review_body}</div>
            <div key={review.id} className="individualReview">
  <p className="user-id">User id: {review.user_id}</p>
  <p className="reviewDescription">{review.review_body}</p>
  <p className="rating">Rating: {review.rating}</p>
  <p className="createdAt">Created At: {new Date(review.created_at).toLocaleString()}</p>
  <p className="updatedAt">Updated At: {new Date(review.updated_at).toLocaleString()}</p>
  {user && review.user_id === user.id && (
    <div className="buttonContainer">
      <div className='reviewButtons'>
      <OpenModalButton
        buttonText="Edit"
        modalComponent={<EditReviewModal business_id={id} review={review} />}

      />
      <OpenModalButton
        buttonText="Delete"
        modalComponent={<DeleteReviewModal id={id} review={review.id} />}
      />
      </div>
    </div>
  )}
</div>
          ))
          .reverse()}
    </div>
  );
}

export default BusinessDetail;
