import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useHistory, useParams } from 'react-router-dom';
import * as businessActions from '../../store/business';
import './UpdateBusinessForm.css';

function UpdateBusiness() {
  const dispatch = useDispatch();
  const history = useHistory();
  const { id } = useParams();
  const business = useSelector(state =>
    state.business.list
      ? state.business.list.find(b => b.id === parseInt(id))
      : null
  );

  const [name, setName] = useState(business ? business.name : '');
  const [address, setAddress] = useState(business ? business.address : '');
  const [city, setCity] = useState(business ? business.city : '');
  const [state, setState] = useState(business ? business.state : '');
  const [zip_code, setZipCode] = useState(business ? business.zip_code : '');
  const [phone_number, setPhoneNumber] = useState(business ? business.phone_number : '');
  const [category_id, setCategoryId] = useState(business ? business.category_id : '');
  const [website, setWebsite] = useState(business ? business.website : '');
  const [about, setAbout] = useState(business ? business.about : '');
  const [type, setType] = useState(business ? business.type : '');
  const [validationErrors, setValidationErrors] = useState([]);

  const currentUser = useSelector(state => state.session.user);
  const owner_id = currentUser ? currentUser.id : null;

  const categories = [
    { id: 1, name: 'Italian' },
    { id: 2, name: 'Mexican' },
    { id: 3, name: 'Middle Eastern' },
    { id: 4, name: 'Japanese' },
    { id: 5, name: 'American' }
  ];

  const validate = (values) => {
    const errors = [];

    if (!values.zip_code || !/^\d{5}$/.test(values.zip_code)) {
      errors.push("Invalid ZIP Code.");
    }

    if (!values.phone_number) {
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
    const errors = validate({
      name,
      address,
      city,
      state,
      zip_code,
      phone_number,
      category_id,
      owner_id,
      website,
      about,
      type
    });

    if (errors.length > 0) return setValidationErrors(errors);

    const businessData = {
      name,
      address,
      city,
      state,
      zip_code,
      phone_number,
      category_id,
      owner_id,
      website,
      about,
      type
    };
    console.log("BUSSINESS DATA", businessData)
    await dispatch(businessActions.editBusiness(id, businessData));
    history.push(`/business/${id}`);
  };

  useEffect(() => {
      dispatch(businessActions.fetchOneBusiness(id));
      console.log("IDDDDDDD", id)
  }, [dispatch, id]);

  return (
    <div className='form__container business-update__form'>
      <div className='business-error__container'>
        {validationErrors.map((error, index) => (
          <div className='error' key={index}>{error}</div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <div className='input__container'>
          <h2>Update Business</h2>
          <div className='form__input'>
            <label>Name</label>
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
            <select
              value={category_id}
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
            <textarea
              value={about}
              onChange={(e) => setAbout(e.target.value)}
              required
              placeholder='Please describe the business.'
            />
          </div>
          <div className='form__input'>
            <label>Type</label>
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
          <button className='form__button' type="submit">Update Business</button>
        </div>
      </form>
    </div>
  );
}

export default UpdateBusiness;
