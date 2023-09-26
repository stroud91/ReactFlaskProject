import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import * as imageActions from "../../store/images";
import "./ImagesForm.css";


function ImagesModal({ bus_data }) {
    const dispatch = useDispatch();
    const images = useSelector(state => state.images);
    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();
    const normalizedImages = Object.values(images)

    normalizedImages.sort((a, b) => a.createdAt < b.createdAt ? 1 : -1)

    useEffect(() => {
        dispatch(imageActions.images(bus_data.id))
        setShowMenu(false)
    }, [dispatch, setShowMenu]);

    let show

    if (normalizedImages[0]) {
        if (normalizedImages[0].id) {
            show = normalizedImages.map((image) => {
                const { id, image_url } = image
                return (
                    <img src={image_url}
                        style={{ color: 'black' }}
                        className='business_images'
                        alt={`image_${id}`}
                        key={id}
                    />
                )
            })
        }
    } else {
        show = `${bus_id.name} has no images`
    }

    return (
        <>
            <button onClick={closeModal()} className='closeModal'>{`Close`}</button>
            <h1>Photos for {bus_data.name}</h1>
            {show}
            end of results
        </>
    );
}

export default ImagesModal;
