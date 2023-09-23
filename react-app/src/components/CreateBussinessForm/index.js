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
const [zipCode, setZipCode] = useState('');
const [phoneNumber, setPhoneNumber] = useState('');
const [categoryId, setCategoryId] = useState('');
const [website, setWebsite] = useState('');
const [about, setAbout] = useState('');
const [type, setType] = useState('');
const [validationErrors, setValidationErrors] = useState([]);

const currentUser = useSelector(state => state.session.user);
const ownerId = currentUser ? currentUser.id : null;

const categories = [
    {id: 1, name: 'Italian'},
    {id: 2, name: 'Mexican'},
    {id: 3, name: 'Middle Eastern'},
    {id: 4, name: 'Japanese'},
    {id: 5, name: 'American'}
  ];


const validate = (values) => {
    const errors = [];

    if (!values.zip_code || !/^\d{5}$/.test(values.zip_code)) {
      errors.push("Invalid ZIP Code.");
    }

    if (!values.phone_number || !/^\d{10}$/.test(values.phone_number)) {
      errors.push("Invalid phone number.");
    }

    if (!values.name || values.name.length > 50) {
      errors.push("Invalid business name.");
    }

    if (!values.address || values.address.length > 255) {
      errors.push("Invalid address.");
    }

    if (!values.city || values.city.length > 50) {
      errors.push("Invalid city.");
    }

    if (!values.state || values.state.length > 25) {
      errors.push("Invalid state.");
    }

    if (!values.category_id) {
      errors.push("Category ID is required.");
    }

    if (!values.owner_id) {
      errors.push("Owner ID is required.");
    }

    if (!values.website || values.website.length > 255) {
      errors.push("Invalid website URL.");
    }

    if (!values.about || values.about.length > 500) {
      errors.push("Invalid about text.");
    }

    if (!values.type || values.type.length > 255) {
      errors.push("Invalid type.");
    }

    return errors;
};


  const handleSubmit = async (e) => {
    e.preventDefault();
    const errors = validate();

    if(errors.length > 0) return setValidationErrors(errors);


    // const businessExists = await checkBusinessName(name);
    // if (businessExists) {
    //   return setValidationErrors(["Business with this name already exists."]);
    // }

    const businessData = {
      name,
      address,
      city,
      state,
      zipCode,
      phoneNumber,
      categoryId,
      ownerId,
      website,
      about,
      type
    };

    await dispatch(businessActions.addBusiness(businessData));
    history.push(`/business/all`);
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
              value={zipCode}
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
              value={phoneNumber}
              onChange={(e) => setPhoneNumber(e.target.value)}
              required
              placeholder='Enter the phone number'
            />
          </div>
          <div className='form__input'>
            <label>Category</label>
            <p>Select the category that best describes the nature of your business.</p>
            <select
              value={categoryId}
              onChange={(e) => setCategoryId(e.target.value)}
              required
            >
              {categories.map(category => (
                <option key={category.id} value={category.id}>
                  {category.name}
                </option>
              ))}
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
          <button className='form__button' type="submit">Add Business</button>
        </div>
      </form>
    </div>
  );



}

export default AddBusiness;
