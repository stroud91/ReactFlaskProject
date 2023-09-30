import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";
import * as sessionActions from "../../store/session";
import { useHistory } from "react-router-dom/";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const [disabled, setDisabled] = useState(true)
  const history = useHistory()

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    } else {
      closeModal()
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
      closeModal()
    }
  }


  return (
    <div className="login-form-container">
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <div className="form-group">
          <label>Email</label>
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn-login">
          Log In
        </button>
      </form>
      <p className="or">or</p>
      <button onClick={demoUser} className="btn-demo">
        Log In as Demo User
      </button>
    </div>
  );
}

export default LoginFormModal;