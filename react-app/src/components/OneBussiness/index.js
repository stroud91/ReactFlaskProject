import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { fetchOneBusiness } from "../../store/business";
import { useParams } from "react-router-dom";
import "./OneBussiness.css";
import PostReviewModal from "../PostReviewModal";
import OpenModalButton from "../OpenModalButton";
import { allReviewsThunk, oneBussinessReviewsThunk } from "../../store/review";
import DeleteReviewModal from "../DeleteReviewModal";
import EditReviewModal from "../EditReviewModal";

function BusinessDetail() {
  // const history = useHistory();
  const dispatch = useDispatch();
  const { id } = useParams();
  const business = useSelector((state) => state.business.selectedBusiness);
  const user = useSelector((state) => state.session.user);
  const reviews = useSelector((state) => state.reviews.currentBusinessReviews);
  console.log("THIS IS BUSINESS", business);
  console.log("THIS IS USER", user);
  console.log("THIS IS REVIEWS", reviews);
  useEffect(() => {
    dispatch(fetchOneBusiness(id));
    dispatch(oneBussinessReviewsThunk(id));
    dispatch(allReviewsThunk())
  }, [dispatch, id]);

  if (!business) return <div>Loading...</div>;
  if (!reviews) {
    return <div>Loading Reviews...</div>;
  }

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
  // const postReviewButton = (user, business) => {
  //     if (user === null || user === undefined) return false; //=> Need to log in to post a review
  //     for (let review of reviews) {
  //         if (review.userId === user.id) return false; // =>Can't post a second review
  //       }

  //     if (user.id === business.ownerId) return false; // => You can't write a review for your own restaurant
  //     return true;
  // }

  // const deleteReviewButton = (user) => {
  //     if (user === null || user === undefined) return false;
  //     for (let review of reviews) {
  //         if (review.userId === user.id) return true;
  //       }
  //     return false;
  // }
//   console.log(
//     "Condition met:",
//     reviews["restaurant_reviews"].user_Id === user.id
//   );
//   console.log("user:", user.id);
//   console.log("review.user_Id:", reviews.restaurant_reviews.user_id);
//   console.log("this is reviews.restaurant.reviews", reviews.restaurant_reviews);
  return (
    <div>
      <h1>{business.name}</h1>
      <p>Address: {business.address}</p>
      <p>Phone Number: {business.phone_number}</p>
      <p>
        Website:{" "}
        <a href={business.website} target="_blank" rel="noopener noreferrer">
          {business.website}
        </a>
      </p>
      <p>Category: {business.category}</p>
      <p>Type: {business.type}</p>
      <p>
        City: {business.city}, {business.state} {business.zip_code}
      </p>
      <div>Average Rating: {business.avg_rating}</div>

      {/* {business?.reviews?.map(review => (
                <div key={review.id}>
                    <p>{review.review_body}</p>
                    <p>Rating: {review.rating}</p>
                    <p>Created At: {new Date(review.created_at).toLocaleString()}</p>
                    <p>Updated At: {new Date(review.updated_at).toLocaleString()}</p>
                </div>
            ))} */}
      {/* <div className="postYourReview">
            {user && user.id !== business.owner_Id && (!reviews.restaurant_reviews.find((review) => review.user_Id === user.id)) && 
            <OpenModalButton
            buttonText="Post Your Review"
            modalComponent={<PostReviewModal id={id} user={user} />}
            />}
        </div> */}
      <div className="postYourReview">
        {user &&
          user.id !== business.owner_id &&
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
            <div key={review.id}>
              <p>User id: {review.user_id}</p>
              <p>{review.review_body}</p>
              <p>Rating: {review.rating}</p>
              <p>Created At: {new Date(review.created_at).toLocaleString()}</p>
              <p>Updated At: {new Date(review.updated_at).toLocaleString()}</p>
              {user && review.user_id === user.id && (
                 <div>
                  <OpenModalButton
                    buttonText="Edit"
                    modalComponent={<EditReviewModal business_id={id} review={review} />}
                  />
            
                  <OpenModalButton
                    buttonText="Delete"
                    modalComponent={<DeleteReviewModal id={id} review={review.id} />}
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