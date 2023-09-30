import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import userIcon from "../../images/user-icon.png"
import "./SignupForm.css";

function SignupFormModal() {
	const dispatch = useDispatch();
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [first_name, setFirstName] = useState("");
	const [last_name, setLastName] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			const data = await dispatch(signUp(username, email, password));
			if (data) {
				setErrors(data);
			} else {
				closeModal();
			}
		} else {
			setErrors([
				"Passwords must match",
			]);
		}
	};

	return (
		<>
			<div className="icon-container">
				<img src={userIcon}
					className="icon"
					alt=""
				/>
			</div>
			<div className="signup_container">
				<div className="title">Sign Up for Yelping</div>
				<form onSubmit={handleSubmit}>
					<div className="business-error__container">
						{errors.map((error, idx) => (
							<div className="error" key={idx}>{error}</div>
						))}
					</div>
					<div className='form__input'>
						{/* <label>Username</label> */}
						<input
							type="text"
							placeholder="Username"
							value={username}
							onChange={(e) => setUsername(e.target.value)}
							required
						/>
					</div>
					<div className='form__input'>
						{/* Email */}
						<input
							type="text"
							placeholder="Email"
							value={email}
							onChange={(e) => setEmail(e.target.value)}
							required
						/>
					</div>
					<div className='form__input'>
						{/* First Name */}
						<input
							type="text"
							placeholder="First Name"
							value={first_name}
							onChange={(e) => setFirstName(e.target.value)}
							required
						/>
					</div>
					<div className='form__input'>
						{/* Last Name */}
						<input
							type="text"
							placeholder="Last Name"
							value={last_name}
							onChange={(e) => setLastName(e.target.value)}
							required
						/>
					</div>
					<div className='form__input'>
						{/* Password */}
						<input
							type="password"
							placeholder="Password"
							value={password}
							onChange={(e) => setPassword(e.target.value)}
							required
						/>
					</div>
					<div className='form__input'>
						{/* Confirm Password */}
						<input
							type="password"
							placeholder="Confirm Password"
							value={confirmPassword}
							onChange={(e) => setConfirmPassword(e.target.value)}
							required
						/>
					</div>
					<div className='form__input button_container'>
						<button className="form__button" type="submit">Sign Up</button>
					</div>
				</form>
			</div >
		</>
	);
}

export default SignupFormModal;