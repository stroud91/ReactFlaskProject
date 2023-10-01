import React from 'react';
import { useDispatch } from 'react-redux';
import { useHistory } from 'react-router-dom';
import { deleteBusiness } from '../../store/business';
import './DeleteBussinessModal.css';

export default function DeleteModal({ id, closeModal }) {
  console.log('DeleteModal is rendered', id)
  const dispatch = useDispatch();
  const history = useHistory();

  const handleDelete = async (e) => {
    e.preventDefault()
    return dispatch(deleteBusiness(id))
    .then(()=>closeModal())
    // dispatch()
    // alert("Delete button clicked");
    // console.log('handleDelete is called');
    // history.push('/business/all');

  };

  return (
    <div>
        <div id="modal-background" onClick={closeModal} />
       <div id="modal">
        <div id="confirm-delete-modal">
             <h1>Confirm Delete</h1>
             <p>Are you sure you want to remove this business?</p>
             <button className="yes-button" onClick={handleDelete}>Yes (Delete Business)</button>
             <button className="no-button" onClick={closeModal}>No (Keep Business)</button>
        </div>
       </div>
     </div>
  );
}
