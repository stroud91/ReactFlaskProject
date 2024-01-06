import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import * as businessActions from '../../store/business';
import './CreateBussinessForm.css';
const API_KEY = process.env.REACT_APP_GOOGLE_MAPS_API_KEY;

function AddBusiness() {

  const dispatch = useDispatch();
  const history = useHistory();


  const [name, setName] = useState('');
  const [address, setAddress] = useState('');
  const [city, setCity] = useState('');
  const [state, setState] = useState('');
  const [zip_code, setZipCode] = useState('');
  const [phone_number, setPhoneNumber] = useState('');
  const [category_id, setCategoryId] = useState(1);
  const [website, setWebsite] = useState('');
  const [about, setAbout] = useState('');
  const [type, setType] = useState('');
  const [isValidAddress, setIsValidAddress] = useState(true);

  const [validationErrors, setValidationErrors] = useState([]);

  const currentUser = useSelector(state => state.session.user);
  const owner_id = currentUser ? currentUser.id : null;

  const isValidURL = (str) => {

    const urlPattern = /^(ftp|http|https):\/\/[^ "]+$/;


    return urlPattern.test(str);
  };

  const validateAddress = async () => {

    const fullAddress = `${address}, ${city}, ${state}, ${zip_code}`;
    const apiKey = API_KEY;
    const url = `https://maps.googleapis.com/maps/api/geocode/json?address=${encodeURIComponent(fullAddress)}&key=${apiKey}`;

    try {
      const response = await fetch(url);

      const data = await response.json();
      return data.status === 'OK';
    } catch (error) {
      console.error('Error:', error);
      return false;
    }
  };

  const handleDemoData = () => {
    setName('Demo Restaurant');
    setAddress('1111 N 9th Street');
    setCity('Stroudsburg');
    setState('PA');
    setZipCode('18360');
    setPhoneNumber('1234567890');
    setCategoryId(1);
    setWebsite('http://www.demorestaurant.com');
    setAbout('This is a demo restaurant for showcasing purposes.');
    setType('Demo Type');
  };


  const validate = () => {
    const errors = {};

    if (!name || name.length < 5 || name.length > 50)  {
      errors.name="Business name must be between 5 and 50 characters.";
    }

    if (!address & validateAddress) {
      errors.address="Invalid address.";
    }

    if (!city || city.length > 50) {
      errors.city="Invalid city.";
    }

    if (!state || state.length != 2) {
      errors.state="Invalid state.";
    }

    if (!zip_code || !/^\d{5}$/.test(zip_code)) {
      errors.zip_code="Invalid ZIP Code.";
    }

    if (!phone_number || !/^\d{10}$/.test(phone_number)) {
      errors.phone_number="Invalid phone number.";
    }

    if (!category_id) {
      errors.category_id="Category is required.";
    }

    if (!website || website.length > 255 || !isValidURL(website)) {
      errors.website = "Invalid website URL.";
    }

    if (!about || about.length > 500) {
      errors.about="Invalid about text.";
    }

    if (!type || type.length > 255) {
      errors.type="Invalid type.";
    }

    return errors;
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = validate();

    if (Object.keys(errors).length > 0) {
      setValidationErrors(errors);
      return;
  }
    const isValid = await validateAddress();
    setIsValidAddress(isValid);

    if (!isValid) {
    setValidationErrors([...errors, 'Invalid address. Please verify your address details.']);
    return;
    }

    const businessData = {
      name,
      address,
      city,
      state,
      zip_code,
      phone_number,
      category_id,
      owner_id,
      // images,
      website,
      about,
      type
    };

    await dispatch(businessActions.createNewBusiness(businessData));

    history.push(`/owned`);
  }



  useEffect(() => {
    async function fetchData() {
      await dispatch(businessActions.getAllBusinesses());
    }
    fetchData();
  }, [dispatch]);

  return (
    <div className='form__container business-edit__form'>
      <div className='business-error__container'>
      </div>
      <form onSubmit={handleSubmit}>
        <div className='input__container'>
          <h2>New Business</h2>
          <div className='form__input'>
            <label>Name
            {validationErrors.name && <div className="error">{validationErrors.name}</div>}
            </label>
            <p>This is the official name of your business as known by your customers.</p>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              required
              placeholder='Enter the business name'
            />
          </div>
          <div className='form__input'>
            <label>Address
            {isValidAddress === false && <p className='error'>Invalid address. Please verify your address details.</p>}
            </label>
            <p>This is the physical address where your business is located.</p>
            <input
              type="text"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
              placeholder='Enter the business address'
            />

          </div>
          <div className='form__input'>
            <label>City
            {validationErrors.city && <div className="error">{validationErrors.city}</div>}
            </label>
            <p>The city where your business is based or operates from.</p>
            <input
              type="text"
              value={city}
              onChange={(e) => setCity(e.target.value)}
              required
              placeholder='Enter the city'
            />
          </div>
          <div className='form__input'>
            <label>State
            {validationErrors.state && <div className="error">{validationErrors.state}</div>}
            </label>
            <p>The state where your business is located or registered.</p>
            <input
              type="text"
              value={state}
              onChange={(e) => setState(e.target.value)}
              required
              placeholder='Enter the state'
            />
          </div>
          <div className='form__input'>
            <label>ZIP Code
            {validationErrors.zip_code && <div className="error">{validationErrors.zip_code}</div>}
            </label>
            <p>The postal code for the area where your business is located.</p>
            <input
              type="text"
              value={zip_code}
              onChange={(e) => setZipCode(e.target.value)}
              required
              placeholder='Enter the ZIP code'
            />
          </div>
          <div className='form__input'>
            <label>Phone Number
            {validationErrors.phone_number && <div className="error">{validationErrors.phone_number}</div>}
            </label>
            <p>This number will be used by customers to contact your business.</p>
            <input
              type="text"
              value={phone_number}
              onChange={(e) => setPhoneNumber(e.target.value)}
              required
              placeholder='Enter the phone number'
            />
          </div>
          <div className='form__input'>
            <label>Category
            {validationErrors.category_id && <div className="error">{validationErrors.category_id}</div>}
            </label>
            <p>Select the category that best describes the nature of your business.</p>
            <select value={category_id} onChange={(e) => setCategoryId(e.target.value)}>
              <option value={1}>Italian</option>
              <option value={2}>Mexican</option>
              <option value={3}>Middle Eastern</option>
              <option value={4}>Japanese</option>
              <option value={4}>American</option>
            </select>
          </div>
          <div className='form__input'>
            <label>Website
            {validationErrors.website && <div className="error">{validationErrors.website}</div>}
            </label>
            <p>If your business has a website, enter the URL here.</p>
            <input
              type="text"
              value={website}
              onChange={(e) => setWebsite(e.target.value)}
              required
              placeholder='Enter the website URL'
            />
          </div>
          <div className='form__input'>
            <label>About
            {validationErrors.about && <div className="error">{validationErrors.about}</div>}
            </label>
            <p>Provide a brief description of your business.</p>
            <textarea
              value={about}
              onChange={(e) => setAbout(e.target.value)}
              required
              placeholder='Please describe the business.'
            />
          </div>
          <div className='form__input'>
            <label>Type
            {validationErrors.type && <div className="error">{validationErrors.type}</div>}
            </label>
            <p>Specify the type of your business (e.g., retail, service, etc.).</p>
            <input
              type="text"
              value={type}
              onChange={(e) => setType(e.target.value)}
              required
              placeholder='Enter the business type'
            />
          </div>
        </div>
        <div className='form__input button__container'>

          <button type="form__button" onClick={handleDemoData} className='form__button'>Fill with Demo Data</button>

          <button className='form__button' type="submit">Add Business</button>

        </div>
      </form>
    </div>
  );
}

export default AddBusiness;
