import React, { useState } from "react";
import { useSelector } from "react-redux";
import OpenModalButton from "../OpenModalButton";
import DeleteImageModal from "./ImageDeleteModal";
import NewImageModal from "./NewImageModal";
// import { useModal } from "../../context/Modal";
import "./ImagesForm.css";


function ImagesModal({ bus_data }) {
    // const dispatch = useDispatch();
    const images = useSelector(state => state.bus_images.images);
    const currentUser = useSelector(state => state.session.user);
    const normalizedImages = Object.values(images)
    const [showDel, setShowDel] = useState(false)
    const [imgId, setImgId] = useState(0)

    normalizedImages.sort((a, b) => a.createdAt < b.createdAt ? 1 : -1)
    // console.log(normalizedImages)

    const handleClick = (event, id) => {
        if (+id === +imgId) {
            setShowDel(!showDel)
        }
        else { setShowDel(true) }
        setImgId(id)
        // 👇️ refers to the image element
    };

    let show

    // if images are loaded
    if (normalizedImages[0]) {
        show = normalizedImages.map((image) => {
            const { id, image_url } = image
            return (
                <>
                    <div className="image-box">
                        <img src={image_url}
                            className={(imgId === id && showDel) && currentUser ? "cursor business_images withBorder" : "cursor business_images noBorder"}
                            alt={`image_${id}`}
                            key={`bus-image-${id}`}
                            onClick={(e) => handleClick(e, id)}
                        />
                    </div>
                </>
            )
        })

    }

    return (
        <div className="modal-container">
            <div className="title">Photos for {bus_data.name}
                <div className="add-delete-button">
                    {currentUser && <span>
                        <OpenModalButton
                            buttonText="Add Image"
                            modalComponent={<NewImageModal
                                bus_id={bus_data.id} />}
                            id={'button'}
                        />

                    </span>}
                    {currentUser &&
                        (showDel && (
                            <span><OpenModalButton
                                buttonText="Delete Image"
                                modalComponent={<DeleteImageModal
                                    id={+imgId} />}

                            />
                            </span>))
                    }
                </div>
            </div>
            <div className="images-container">
                {show}

            </div>
        </div>
    );
}

export default ImagesModal;
