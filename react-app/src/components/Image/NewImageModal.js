import React, { useState } from "react";
import * as imageActions from "../../store/images";
import OpenModalButton from "../OpenModalButton";
import ImagesModal from '../Image/GetImagesModal';
import { fetchOneBusiness } from '../../store/business';
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import "./ImagesForm.css";

function NewImageModal({ bus_id }) {
    const dispatch = useDispatch();
    const [image_url, setImgUrl] = useState("");
    const [imageLoading, setImageLoading] = useState(false);
    const [image_preview, setPrev] = useState(false);
    const [imageFile, setImageFile] = useState(null)
    const [errors, setErrors] = useState({});
    const { closeModal } = useModal();
    const business = useSelector(state => state.business.selectedBusiness);

    // let imageData

    // if (business.images.length) {
    //     imageData = {
    //         "image_url": image_url,
    //         "image_preview": image_preview.toString()
    //     }
    // } else {
    //     imageData = {
    //         "image_url": image_url,
    //         "image_preview": 'true'
    //     }
    // }

    // const handleSubmit = async (e) => {
    //     e.preventDefault();
    //     const data = await dispatch(imageActions.createImage(bus_id, imageData));
    //     if (data) {
    //         setErrors(data);
    //     } else {
    //         await dispatch(imageActions.images(bus_id))
    //         await dispatch(fetchOneBusiness(bus_id));
    //         closeModal()
    //     }
    // };

    const handleSubmit = (e) => {
        e.preventDefault();
    
        const formData = new FormData();
        formData.append('image_url', imageFile);
        // formData.append('image_preview', image_preview.toString());
        const image_preview_value = !business.images.length  ? 'true' : image_preview.toString();
        formData.append('image_preview', image_preview_value.toString());
        console.log("Form Data:", formData)
        console.log("Image File:", imageFile);
        console.log("Image Preview:", image_preview);
    
        setImageLoading(true);

        console.log("Sending image_preview to backend:", formData.get('image_preview'));
    
        dispatch(imageActions.createImage(bus_id, formData))
            .then((data) => {
                console.log("Backend Response:", data)
                if (data) {
                    setErrors(data);
                } else {
                    return Promise.all([
                        dispatch(imageActions.images(bus_id)),
                        dispatch(fetchOneBusiness(bus_id))
                    ]);
                }
            })
            .then(() => {
                closeModal();
            })
            .catch((error) => {
                setErrors(error);
            })
            .finally(() => {
                setImageLoading(false);
            });
    };

    const handleImagePreviewChange = () => {
    setPrev(!image_preview); // Toggle the image_preview state
};




    return (
        <>
            <div className="modal-container">
                <div className="upload-title">Upload Image</div>
                <form onSubmit={handleSubmit} encType="multipart/form-data">
                    <div style={{ fontSize: "10px", color: "grey" }}>
                        <input
                            type="file"
                            accept="image/*"
                            placeholder="Image URL"
                            value={image_url}
                            onChange={(e) => {
                                setImageFile(e.target.files[0]); 
                                setImgUrl(e.target.value); 
                            }}
                            // onChange={handleFileChange}
                            className="imgurl-input"
                            required
                        />
                    </div>
                    <div>
                        {errors.image_url && errors.image_url.map((er) => {
                            return (
                                <div
                                    style={{ color: "red" }}
                                    key={errors.image_url.indexOf(er)}>
                                    {er}
                                </div>
                            )
                        })}
                    </div>
                    <div className="preview-img-desc">
                        <input
                            type="checkbox"
                            id="checkbox"
                            value={image_preview}
                            onChange={() => setPrev(!image_preview)}
                        />
                        Main Image
                    </div>
                    <div className="upload-cancel">
                        <button className='confirm-yes' type="submit">Upload Image</button>
                        <div>
                            <OpenModalButton
                                buttonText="Cancel"
                                modalComponent={<ImagesModal
                                    bus_data={business} />
                                }
                                id={'cancel'}
                            />
                        </div>
                    </div>
                </form>
            </div>
        </>
    )
}

export default NewImageModal;
