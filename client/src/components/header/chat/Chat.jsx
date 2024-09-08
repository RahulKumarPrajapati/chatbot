import React, { useEffect, useState } from "react";
import axios from 'axios';
import './Chat.css';
import {API_URL} from '../../../shared/CONSTANT'

const Chat = () => {

    const [question, setQuestion] = useState("");
    const [answer, setAnswer] = useState([]);
    const [isSearching, setSearching] = useState(false);
    const handleChange = () => {
        if(!isSearching && question != ""){
            const url = API_URL + 'api/chat/getAnswer'
            const chatData = {
                question: question
            }
            setSearching(true);
            axios.post(url, chatData).then(
                (res) => {
                    setAnswer(res.data.answer);
                    setSearching(false);
                },
                (err) => {
                    setAnswer("Some error has occured. Please try again.");
                    setSearching(false);
                }
            )
        }
    }

    const handleQuestion = (event) => {
        setQuestion(event.target.value)
    }

    return (
        <div className="container col-8">
            <div className="d-flex flex-column">
                <h1 className="mt-2">Hello Human</h1>
                <h1 className="mt-2 bard-question">How can I help you today?</h1>
                <textarea className="form-control mr-sm-2 mt-2" rows="5" type="search" placeholder="Enter your prompt here." aria-label="Search" value={question} onChange={(event) => handleQuestion(event)} />
                <div className="d-flex justify-content-end">
                    <button className="btn btn-outline-primary mt-2" onClick={handleChange} disabled={isSearching}>
                        <span>Search</span>
                        {!isSearching && <i className="ms-2 fa fa-paper-plane"></i>}
                        {isSearching && <i className="ms-2 fa fa-solid fa-spinner fa-spin"></i>}
                    </button>
                </div>
                
            </div>
            {!isSearching && answer.length > 0 &&
                <div className="mt-3 mb-3 container">
                    <div className="row d-flex justify-content-start border border-2 output">
                    {answer.map((ans, ind) => (
                         <span key={ind}>{ans}</span>
                        ))
                    }
                    </div>

                </div>
            }
        </div>
    )
}

export default Chat;