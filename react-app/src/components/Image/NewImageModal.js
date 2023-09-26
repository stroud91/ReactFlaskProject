import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import * as imageActions from "../../store/images";
import "./ImagesForm.css";


function NewImageModal({ bus_id }) {
    const dispatch = useDispatch();
    const [errors, setErrors] = useState([]);
    const [image_url, setImgUrl] = useState("");
    const [image_preview, setPrev] = useState(false)
    const { closeModal } = useModal();


    const imageData = {
        image_url,
        image_preview: image_preview.toString()
    }

    const postImage = async (e) => {
        const data = await dispatch(imageActions.createImage(bus_id, imageData));
        if (data) {
            setErrors(data);
        } else {
            closeModal()
        }
    };


    return (
        <>
            <h1>Upload Image</h1>
            <h3>Upload an image of your business</h3>
            <input
                type="text"
                placeholder="Image URL"
                value={image_url}
                onChange={(e) => setImgUrl({ url: e.target.value }
                )}
            />
            <input
                type="checkbox"
                id="checkbox"
                value={image_preview}
                onChange={(e) => setPrev(!image_preview)}
            />
            <button onClick={postImage} className='deleteButtonYes'>{`Yes (Delete Image)`}</button>
            <button onClick={closeModal()} className='deleteButtonNo'>{`Cancel`}</button>

        </>
    );
}

export default NewImageModal;
