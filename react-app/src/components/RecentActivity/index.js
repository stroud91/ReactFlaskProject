import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { allReviewsThunk } from "../../store/review";
import "./RecentActivity.css";

function RecentActivity() {
  const dispatch = useDispatch();
  const reviews = useSelector((state) => state.reviews.all);
  
  useEffect(() => {
    dispatch(allReviewsThunk())
  }, [dispatch]);

  if (!reviews) return null;

  const last12Reviews = reviews["Reviews"].slice(-12);
  console.log(last12Reviews);

  return (
    <div>
      <h1>Recent Activity</h1>
      <div className="review-container">
        {reviews &&
          last12Reviews.map((review) => (
            <div className="review-item" key={review.id}>
              <div className="item-property">
                <strong></strong> {review.user_first_name}
              </div>
              <div className="item-property">
                <strong className="business-name">
                  {review.business_name}
                </strong>
              </div>
              <div className="item-property">
                <strong>Review:</strong> {review.review_body}
              </div>
              <div className="item-property">
                <strong>Rating:</strong>
                {[...Array(review.rating)].map((_, index) => (
                  <i key={index} className="fa-solid fa-star"></i>
                ))}
              </div>
            </div>
          ))}
      </div>
    </div>
  );
}
export default RecentActivity;
