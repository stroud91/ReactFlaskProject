import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import * as businessActions from "../../store/business";
import "../Bussiness/Business.css";
import MainPage from "../MainPageView";

function QueryBusiness() {
  const dispatch = useDispatch();
  let businesses = useSelector((state) => state.business.search);
  businesses = businesses["queried businesses"];
  console.log("This is the result of the search bar", businesses);

 

  return (
    <div>
      {businesses.length === 0 ? (
        <div>
        <p> No restaurants found. Please try a different search.</p>
        <Link to="/">
        <button>Go back to main page</button>
        </Link>
        </div>
      ) : (
        <ul className="businessMain__grid">
          {businesses &&
            businesses.map((business) => (
              <li key={business.id} className="businessMain__item">
                <li className="businessMain__image">
                  {/* Image will go here */}
                </li>
                <li>Name: {business.name}</li>
                <p>Category: {business.category}</p>
                <p>Rating: {business.avg_rating}</p>
                <p>
                  {business.address}, {business.city}, {business.state}{" "}
                  {business.zip_code}
                </p>
                <p>{business.phone_number}</p>
                <Link to={`/business/${business.id}`}>View More</Link>
              </li>
            ))}
        </ul>
      )}
    </div>
  );
}

export default QueryBusiness;
