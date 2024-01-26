import { useOktaAuth } from "@okta/okta-react";
import ReviewModel from "../../models/ReviewModel";
import { StarsReview } from "./StarsReview";

export const Review: React.FC<{ review: ReviewModel, deleteReview: any }> = (props) => {
    
    const date = new Date(props.review.date);

    const longMonth = date.toLocaleString('en-us', { month: 'long' });
    const dateDay = date.getDate();
    const dateYear = date.getFullYear();

    const dateRender = longMonth + ' ' + dateDay + ', ' + dateYear;

    console.log(props.review)
    
    return (
        <div>
            <div className='col-sm-8 col-md-8'>
                <h5>{props.review.userEmail}</h5>
                <div className='row'>
                    <div className='col'>
                        {dateRender}
                    </div>
                    <div className='col'>
                        <StarsReview rating={props.review.rating} size={16} />
                    </div>
                    <div className='col'>
                        <button className='btn btn-success btn-sm'>Edit</button>
                    </div>
                    <div className='col'>
                        <button onClick={() => props.deleteReview()} className='btn btn-success btn-sm'>Delete</button>
                    </div>
                </div>
                <div className='mt-2'>
                    <p>
                        {props.review.reviewDescription}
                    </p>
                </div>
            </div>
            <hr/>
        </div>
    );
}