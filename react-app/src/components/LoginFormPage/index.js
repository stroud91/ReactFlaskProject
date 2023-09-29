import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch, useSelector } from "react-redux";
import { Redirect } from "react-router-dom";
import './LoginForm.css';
import { useHistory } from "react-router-dom/"
import { NavLink } from 'react-router-dom';

function LoginFormPage() {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const history = useHistory();

  if (sessionUser) return <Redirect to="/" />;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      history.push("/")
    }
  };

  const demoUser = async (e) => {
    e.preventDefault()
    let email = "demo@aa.io"
    let password = "password"
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      history.push("/business/all")
    }
  }

  return (
    <>
      <h1>Log In</h1>
      <form onSubmit={handleSubmit} className="logIn-Form">
        
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <label>
          <p>What's your email and password?</p>
         
          <input
          className="input"
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            placeholder="Enter Email"
            
          />
        </label>
        <label>
        
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            placeholder="Enter Password"
            className="input"
          />
        </label>
        <button type="submit" className="logIn-form-button">Continue</button>
        <p className="or">or</p>
        <div className="log-in-buttons">
        {/* <button type="submit">Log In</button> */}
        <button onClick={demoUser}>Log In as Demo User</button>
        </div>
        <NavLink exact to="/signup" className="logIn-form-button">
         Sign up
        </NavLink>
        
      </form>
     
    </>
  );
}

export default LoginFormPage;