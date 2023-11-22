import { useSelector, useDispatch } from "react-redux";
import { useParams, useHistory } from "react-router-dom";
import { getBusinesses } from "../../store/business";
import React, { useState, useEffect } from "react";
import RecentActivity from "../RecentActivity";
import { Link } from "react-router-dom/cjs/react-router-dom.min";
import SearchBar from "../SearchBar";
import yelgImg from "../../images/yelp_cover_image.jpg";
import "./MainPageView.css";

function MainPage() {
  const [search, setSearch] = useState("");
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [businesses, setBusinesses] = useState([]);
  const history = useHistory();


  const imageUrls = [
    yelgImg,
    "https://static.vecteezy.com/system/resources/previews/004/898/969/large_2x/closeup-view-of-delicious-grilled-beef-medallions-served-on-table-luxury-restaurant-food-on-white-setting-gourmet-meal-banner-view-photo.jpg",
    "https://orangetourism.org/wp-content/uploads/2023/07/Farm-to-Table-OakReed-1315.jpg",

  ];

  const handleSubmit = (e) => {
    e.preventDefault();
  };

  const handleChange = (e) => {
    setSearch(e.target.value);
  };

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCurrentImageIndex((currentImageIndex) =>
        currentImageIndex === imageUrls.length - 1 ? 0 : currentImageIndex + 1
      );
    }, 3000);

    return () => clearInterval(intervalId);
  }, []);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("/api/business/");
      const responseData = await response.json();
      setBusinesses(responseData);
    }
    fetchData();
  }, []);

  return businesses ? (
    <div className="main-page-container">
      <header className="main-header"></header>
      <div
        className="main-page-image-container"
        onClick={() => history.push("/business/all")}
      >
         <img
          src={imageUrls[currentImageIndex]}
          alt="Featured restaurant"
          className="fade-in"
        />
        <div className="image-text">View all restaurants</div>
      </div>
      <RecentActivity />
    </div>
  ) : (
    <div>Loading...</div>
  );
}

export default MainPage;
