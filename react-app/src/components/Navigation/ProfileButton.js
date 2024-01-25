import React, { useState, useEffect, useRef } from "react";
import { useHistory, useLocation } from "react-router-dom/cjs/react-router-dom.min";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import OpenModalButton from "../OpenModalButton";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { NavLink } from 'react-router-dom';

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();
  const location = useLocation()

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current || !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    closeMenu()
    history.push('/')
  };

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");


  return (
    <>
      {user ? (
        <button onClick={openMenu} className="profile-button">
          <img
            src={user.profile_image_id}
            alt={`${user.username}'s profile pic`}
            onError={(e) => { e.target.onerror = null; e.target.src = "path_to_default_image.jpg" }}
            className="profile-picture"
          />
        </button>
      ) : (
        <>
          <div className="login_signup_container">
            <OpenModalButton
              buttonText="Log In"
              onItemClick={closeMenu}
              modalComponent={<LoginFormModal />}
              id={location.pathname !== '/' ? ("login-button2") : ("login-button")}
            />
            <OpenModalButton
              buttonText="Sign Up"
              onItemClick={closeMenu}
              modalComponent={<SignupFormModal />}
              id={'signup-button'}
            />
          </div>
        </>
      )}
      <ul className={ulClassName} ref={ulRef}>
        {user ? (
          <>
            <div className="profile-first-container">
              <div className="profile-first">
                <div className="profile_imgs">
                  <i className="fa-solid fa-house"></i>
                </div>
                <div className="profile-first-name">Welcome, {user.username}</div>
              </div>
              <div className="profile-first">
                <div className="profile_imgs">
                  <i className="fa-solid fa-user"></i>
                </div>
                <div className="profile-first-name">{user.first_name} {user.last_name}</div>
              </div>
              <div className="profile-first">
                <div className="profile_imgs">
                  <i className="fa-solid fa-envelope"></i>
                </div>
                <div className="profile-first-name">{user.email}</div>
              </div>
            </div>
            <div className="view-logout-container">
              <NavLink exact to="/owned" className="view-business-button">
                <div className="bus-buttons">
                  <div className="profile_imgs">
                    <i className="fa-solid fa-store"></i>
                  </div>
                  <div className="bus-button">
                    View Business
                  </div>
                </div></NavLink>
              <NavLink exact to="/business/create-new-business" className="create-business-button">
                <div className="bus-buttons">
                  <div className="profile_imgs">
                    <i className="fa-solid fa-plus"></i>
                  </div>
                  <div className="bus-button">
                    Create a business
                  </div>
                </div>
              </NavLink>
            </div>
            <div className="logout-container">
              <button onClick={handleLogout} className="logout-red-button">
                <div className="bus-buttons">
                  <div className="profile_imgs">
                    <i className="fa-solid fa-right-from-bracket"></i>
                  </div>
                  <div className="bus-button">
                    Log Out
                  </div>
                </div>
              </button>
            </div>
          </>
        ) : (
          <>
            <div className="view-logout-container">
              <OpenModalButton
                buttonText="Log In"
                onItemClick={closeMenu}
                modalComponent={<LoginFormModal />}
                id={'log-in-button'}
              />
              <OpenModalButton
                buttonText="Sign Up"
                onItemClick={closeMenu}
                modalComponent={<SignupFormModal />}
                id={'sign-up-button'}
              />
            </div>
          </>
        )}
      </ul >
    </>
  );
}

export default ProfileButton;
