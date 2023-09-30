import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import OpenModalButton from "../OpenModalButton";
import ImagesModal from '../Image/GetImagesModal';
import { fetchOneBusiness } from '../../store/business';
import * as imageActions from "../../store/images";
import "./ImagesForm.css";

function DeleteImageModal({ id }) {
    const dispatch = useDispatch();
    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();
    const business = useSelector(state => state.business.selectedBusiness);

    const deleteImage = async (e) => {
        const data = await dispatch(imageActions.deleteImage(id));
        if (data) {
            setErrors(data.error);
        } else {
            closeModal()
            await dispatch(fetchOneBusiness(business.id));
            await dispatch(imageActions.images(business.id))
        }
    };
    let showConfirmDelete = (
        <>
            <div className="modal-container">
                <div className="upload-title">Confirm Delete</div>
                <div className="delete-desc">Are you sure you want to delete this image?</div>
                <div
                    style={{ color: "red" }}>
                    {errors}
                </div>
                <div className="delete-cancel">
                    <button className='upload button cursor' onClick={deleteImage} >{`Yes (Delete Image)`}</button>

                    <div>
                        <OpenModalButton
                            buttonText="Cancel"
                            modalComponent={<ImagesModal
                                bus_data={business} />}
                            id='cancel'
                        />
                    </div>
                </div>
            </div>
        </>
    )

    return (
        <>
            {showConfirmDelete}
        </>
    );
}

export default DeleteImageModal;
