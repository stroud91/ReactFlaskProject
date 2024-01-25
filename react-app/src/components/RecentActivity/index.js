import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { allReviewsThunk } from "../../store/review";
import oneStar from "../../images/1star.png";
import twoStar from "../../images/2star.png";
import threeStar from "../../images/3star.png";
import fourStar from "../../images/4star.png";
import fiveStar from "../../images/5star.png";
import "./RecentActivity.css";
import { useHistory } from "react-router-dom/cjs/react-router-dom.min";
function RecentActivity() {
  const dispatch = useDispatch();
  const reviews = useSelector((state) => state.reviews.all);
  const history = useHistory()
  useEffect(() => {
    dispatch(allReviewsThunk());
  }, [dispatch]);
  function star(rating) {
    if (rating === 1) {
      return oneStar
    }
    if (rating === 2) {
      return twoStar
    }
    if (rating === 3) {
      return threeStar
    }
    if (rating === 4) {
      return fourStar
    }
    if (rating === 5) {
      return fiveStar
    }
  }
  if (!reviews) return null;
  const last12Reviews = reviews["Reviews"].slice(-12);
  return (
    <div className="recent_activity">
      <div className="recent_title">Recent Activities</div>
      <div className="review-container">
        {reviews &&
          last12Reviews.map((review) => (
            <div className="review-item" key={review.id}>
              <div className="item-property">
                <div className="user-info-review">
                  {review.profile_image_url ? (
                    <img
                      src={review.profile_image_url}
                      alt={`${review.user_first_name}'s profile pic`}
                      onError={(e) => { e.target.onerror = null; e.target.src = "path_to_default_image.jpg" }}
                      className="profile-pic"
                    />
                  ) : (
                    <i className="far fa-user-circle" />
                  )}
                  <div className="reviewer_name">{`${review.user_first_name} ${review.user_last_name[0]}.`}</div>
                </div>
              </div>
              <div className="item-property">
                <strong className="business-name" onClick={e => { history.push(`/business/${review.business_id}`) }} >
                  {review.business_name}
                </strong>
              </div>
              <div className="star-property">
                <img src={star(review.rating)} className="star-images"></img>
              </div>
              <div className="item-property">
                <div className="review-body">{review.review_body}</div>
                <div className="continue-reading" onClick={e => { history.push(`/business/${review.business_id}`) }}>
                  Continue reading
                </div>
              </div>
            </div>
          ))}
      </div>
    </div >
  );
}
export default RecentActivity;
