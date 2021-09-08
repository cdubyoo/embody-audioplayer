import React, { useEffect, useState } from "react";
import axios from "axios";
import Cookies from 'js-cookie'

const csrftoken = Cookies.get('csrftoken') // Cookies from Django Domain

const Comment = () => {
    const [audio, setAudio] = useState([])
    const [user, setUser] = useState('Anon')
    const [body, setBody] = useState('')
    const [timestamp, setTimestamp] = useState(0)

    useEffect(() => {
        const fetchData = async () => {
            const result = await axios('/api/audios');
            setAudio(result.data); 
        };
        fetchData();
    }, [audio])
    

    // turn time stamp seconds into mm:ss
  function timeStampConvert(seconds) {
    return new Date(seconds * 1000).toISOString().substr(14,5);
  }
    const handleSubmit = (e) => {
        e.preventDefault()
        axios.post('/api/comments/',  
                {
                    audio: 1,
                    user: user,
                    body: body,
                    timestamp_seconds: 30
    
                }, {headers: { 'X-CSRFToken': csrftoken }}) 
    }

    return(
        <div>
             {audio.map(item => (
                 <span>{item.title} by {item.artist}</span>
             ))}
            
            <form onSubmit={handleSubmit}>
                <label type="submit">
                    <input placeholder="Name" type="text" name="name" onChange={e => setUser(e.target.value)}/>
                    <input placeholder="Leave a comment" type="text" name="comment" required onChange={e => setBody(e.target.value)} />
                </label>
                <button type="submit">Add</button>
            </form>
            <div>
                 {audio.map(item => (
          <span>
            {item.comments.map(comment => (
              <li key={item.comments.id}>
                {comment.user} at {timeStampConvert(comment.timestamp_seconds)}
                <br></br>
                <span>{comment.body}</span>
              </li>
            ))}
          </span>
      ))}
            </div>
        </div>
    );
};

export default Comment