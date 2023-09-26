import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import * as imageActions from "../../store/images";
import "./ImagesForm.css";


function ImagesModal({ bus_id }) {
    const dispatch = useDispatch();
    const images = useSelector(state => state.images);
    const business = useSelector(state => state.business)
    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();

    useEffect(() => {
        dispatch(imageActions.images(bus_id))
        dispatch()
        setShowMenu(false)
    }, [dispatch, setShowMenu]);

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
