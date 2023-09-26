import React, { useState } from "react";
import { useParams } from 'react-router-dom'
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import * as imageActions from "../../store/images";
import "./ImagesForm.css";

function DeleteImageModal({ id }) {
    const dispatch = useDispatch();
    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();

    const deleteImage = async (e) => {
        const data = await dispatch(imageActions.deleteImage(id));
        if (data.errors) {
            setErrors(data);
        } else {
            closeModal()
        }
    };

    let showConfirmDelete = (
        <>
            <h1>Confirm Delete</h1>
            <h3>Are you sure you want to delete this image?</h3>
            <button onClick={deleteImage} className='deleteButtonYes'>{`Yes (Delete Image)`}</button>
            <button onClick={closeModal()} className='deleteButtonNo'>{`No (Keep Image)`}</button>

        </>
    )

    return (
        <>
            {showConfirmDelete}
        </>
    );
}

export default DeleteImageModal;
