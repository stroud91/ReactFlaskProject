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
    const [image_preview, setPrev] = useState(false);
    const [errors, setErrors] = useState({});
    const { closeModal } = useModal();
    const business = useSelector(state => state.business.selectedBusiness);

    let imageData

    if (business.images.length) {
        imageData = {
            "image_url": image_url,
            "image_preview": image_preview.toString()
        }
    } else {
        imageData = {
            "image_url": image_url,
            "image_preview": 'true'
        }
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        const data = await dispatch(imageActions.createImage(bus_id, imageData));
        if (data) {
            setErrors(data);
        } else {
            await dispatch(imageActions.images(bus_id))
            await dispatch(fetchOneBusiness(bus_id));
            closeModal()
        }
    };
    return (
        <>
            <div className="modal-container">
                <div className="upload-title">Upload Image</div>
                <form onSubmit={handleSubmit}>
                    <div style={{ fontSize: "10px", color: "grey" }}>
                        <input
                            type="text"
                            placeholder="Image URL"
                            value={image_url}
                            onChange={(e) => setImgUrl(e.target.value)}
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
                        <button className='upload button cursor' type="submit">Upload Image</button>
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
