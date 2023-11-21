import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import * as businessActions from '../../store/business';
import './CreateBussinessForm.css';

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

  const validateAddress = async () => {

    const fullAddress = `${address}, ${city}, ${state}, ${zip_code}`;
    const apiKey = 'AIzaSyD3F3R77roIM00Av5ekpGLIqivQT_uPSJg';
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
    setAddress('123 Demo St');
    setCity('Demo City');
    setState('DC');
    setZipCode('12345');
    setPhoneNumber('1234567890');
    setCategoryId(1); 
    setWebsite('http://www.demorestaurant.com');
    setAbout('This is a demo restaurant for showcasing purposes.');
    setType('Demo Type');
  };


  const validate = () => {
    const errors = [];

    if (!name || name.length < 5 || name.length > 50)  {
      errors.push("Business name must be between 5 and 50 characters.");
    }

    if (!address & validateAddress) {
      errors.push("Invalid address.");
    }

    if (!city || city.length > 50) {
      errors.push("Invalid city.");
    }

    if (!state || state.length != 2) {
      errors.push("Invalid state.");
    }

    if (!zip_code || !/^\d{5}$/.test(zip_code)) {
      errors.push("Invalid ZIP Code.");
    }

    if (!phone_number || !/^\d{10}$/.test(phone_number)) {
      errors.push("Invalid phone number.");
    }

    if (!category_id) {
      errors.push("Category is required.");
    }

    if (!website || website.length > 255) {
      errors.push("Invalid website URL.");
    }

    if (!about || about.length > 500) {
      errors.push("Invalid about text.");
    }

    if (!type || type.length > 255) {
      errors.push("Invalid type.");
    }

    return errors;
  };


  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = validate();

    if (errors.length > 0) return setValidationErrors(errors);


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
        {validationErrors.map((error, index) => (
          <div className='error' key={index}>{error}</div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <div className='input__container'>
          <h2>New Business</h2>
          <div className='form__input'>
            <label>Name</label>
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
            <label>Address</label>
            <p>This is the physical address where your business is located.</p>
            <input
              type="text"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
              required
              placeholder='Enter the business address'
            />
             {isValidAddress === false && <p className='error'>Invalid address. Please verify your address details.</p>}
          </div>
          <div className='form__input'>
            <label>City</label>
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
            <label>State</label>
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
            <label>ZIP Code</label>
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
            <label>Phone Number</label>
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
            <label>Category</label>
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
            <label>Website</label>
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
            <label>About</label>
            <p>Provide a brief description of your business.</p>
            <textarea
              value={about}
              onChange={(e) => setAbout(e.target.value)}
              required
              placeholder='Please describe the business.'
            />
          </div>
          <div className='form__input'>
            <label>Type</label>
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
          <button type="button" onClick={handleDemoData} className='demo-data-button'>Fill with Demo Data</button>
          <button className='form__button' type="submit">Add Business</button>

        </div>
      </form>
    </div>
  );
}

export default AddBusiness;
