import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import PostReviewModal from "../PostReviewModal";
import OpenModalButton from "../OpenModalButton";
import { allReviewsThunk, oneBussinessReviewsThunk } from "../../store/review";
import DeleteReviewModal from "../DeleteReviewModal";
import EditReviewModal from "../EditReviewModal";
import ImagesModal from "../Image/GetImagesModal";
import { fetchOneBusiness } from "../../store/business";
import { useParams, useHistory } from "react-router-dom";
import { useModal } from "../../context/Modal";
import * as imageActions from "../../store/images";
import { images } from "../../store/images";
import noImage from "../../images/no-image.png";
import "./OneBussiness.css";
import "../Image/ImagesForm.css";
import DeleteModal from "../DeleteBusinessModal";
import MapContainer from "../MapContainer";
import LoadingAnimation from "../Loading";

function BusinessDetail() {
  const history = useHistory();
  const dispatch = useDispatch();

  let { id } = useParams();
  const business = useSelector((state) => state.business.selectedBusiness);

  const bus_images = useSelector((state) => state.bus_images.images);

  const user = useSelector((state) => state.session.user);
  const reviews = useSelector((state) => state.reviews.currentBusinessReviews);
  const currentUser = useSelector((state) => state.session.user);
  const normalizedImages = bus_images && Object.values(bus_images);
  // const { setModalContent, closeModal } = useModal();
  // const [showConfirmModal, setShowConfirmModal] = useState(false);


  useEffect(() => {
    dispatch(fetchOneBusiness(id));
    dispatch(oneBussinessReviewsThunk(id));
    // dispatch(allReviewsThunk());
    dispatch(images(id));
  }, [dispatch, id]);

  if(!business){
    return <LoadingAnimation />
  }
  if (!reviews) {
    return <div>Loading Reviews...</div>;
  }


  // const handleDelete = () => {
  //   setShowConfirmModal(true);
  // };

  const handleEdit = () => {
    history.push(`/business/${business.id}/edit`);
  };

  let image_gallery;



  if (normalizedImages && normalizedImages.length > 0) {
    image_gallery = normalizedImages.map((image) => {
      const { id, image_url } = image;
      return (
        <img src={image_url} alt={`imageId_${id}`} key={`imageId_${id}`}></img>
      );
    });
  } else {
    image_gallery = <img src={noImage} alt={`imageId_${id}`}></img>;
  }

  const changeDate = (date) => {
    let newDate = new Date(date)
    let options = { day: 'numeric', month: 'long', year: 'numeric' };
    let changedDate = newDate.toLocaleString('en-US', options);
    return changedDate
}

  return (
    <div>
      <h1>{business.name}</h1>
      <div className="scroll-gallery">
        <div className="scroll-container">{image_gallery}</div>
        <span className="see-images">
          <OpenModalButton
            buttonText={`See all ${normalizedImages ? normalizedImages.length : 0} photos`}
            modalComponent={<ImagesModal bus_data={business} />}
            id={"see-img"}
          />
        </span>
      </div>

      <div className="business-detail-container">
        {/* Side Panel for Contact Info */}
        <div className="business-side-panel">
        <div className="contact-container">
        <h2>Contact Information</h2>
        <p>Address: {business.address}</p>
        <p>Phone Number: {business.phone_number}</p>
        <p>City: {business.city}, {business.state} {business.zip_code}</p>
        <p>Website:
            <a href={business.website} target="_blank" rel="noopener noreferrer">
                {business.website}
            </a>
        </p>
        </div>
        <div className="map-container">
            {business && (
                <MapContainer business={business} businessId={business.id} />
            )}
        </div>
    </div>

        {/* Main Business Info */}
        <div className="business-info">

          <h1>{business.name}</h1>
          <p>Category: {business.category}</p>
          <p>Type: {business.type}</p>

          <p>Average Rating: {business.avg_rating}</p>
          <p className="bold-about">About</p>
          <p>{business.about}</p>
          {currentUser && currentUser.id === business.owner_id && (
            <div className="business-buttons-conditional">
              <button
                className="edit-business-button"
                onClick={() => handleEdit(business.id)}
              >
                Edit
              </button>
              <OpenModalButton
                buttonText="Delete"
                modalComponent={<DeleteModal bus_data={business} />}
                id={"delete-business-button"}
              />
            </div>
          )}
        </div>
      </div>




      <div className="postYourReview">
        {user &&
          user.id !== business.owner_id &&
          !reviews.restaurant_reviews.some(
            (review) => review.user_id === user.id
          ) && (
            <OpenModalButton
              buttonText="Post Your Review"
              modalComponent={<PostReviewModal id={id} user={user} />}
              id={"post-review-button"}
            />
          )}
      </div>

      {reviews &&
        reviews.restaurant_reviews.map((review) => (
            // <div className="individualReview" key={`review-${review.id}`}>
            //   {/* <div className="reviewUser">{review.User?.firstName}</div> */}
            //   <div className="createdAt">{(review.created_At)}</div>
            //   <div className="reviewDescription">{review.review_body}</div>
            <div key={review.id} className="individualReview">
              <p className="user-individual-review">

                {review.user_first_name} {review.user_last_name} posted on {changeDate(review.created_at)}:
              </p>
              <p>{review.review_body}</p>
              <p>
                {[...Array(review.rating)].map((_, index) => (
                  <i key={index} className="fa-solid fa-star"></i>
                ))}
              </p>
              {user && review.user_id === user.id && (
                <div className="reviewButtons">
                  <OpenModalButton
                    buttonText="Edit"
                    modalComponent={
                      <EditReviewModal business_id={id} review={review} />
                    }
                    id={"review-edit-button"}
                  />
                  <OpenModalButton
                    buttonText="Delete"
                    modalComponent={
                      <DeleteReviewModal id={id} review={review.id} />
                    }
                    id={"review-delete-button"}
                  />
                </div>
              )}
            </div>
          ))
          .reverse()}
    </div>
  );
}

export default BusinessDetail;
