import PostReviewModal from "../PostReviewModal";
import OpenModalButton from "../OpenModalButton";
import { useParams } from "react-router-dom";

function TestComponent () {
    const { id } = useParams();
    return (
        <div className="Post your review">
            <OpenModalButton 
            buttonText={ "Post your review"}
            modalComponent={ <PostReviewModal id={id} />}
            />
        </div>
    )
}

export default TestComponent;