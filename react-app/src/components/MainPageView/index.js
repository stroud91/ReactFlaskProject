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
    "https://plymold.com/wp-content/uploads/2022/11/chair-glides-banner.jpg",
    "https://www.timewornusa.com/wp-content/uploads/2019/04/TimeWorn-Restaurant-Tabletops-banner-cropped.jpg",

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
