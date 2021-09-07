import React, { useEffect, useState } from "react";
import "./index.css";
import axios from "axios";
import Player from "./Player";
import audiotrack1 from './audiotrack1.wav';
import Comment from "./Comment";

function App() {
  const [audio, setAudio] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios('/api/audios');
      setAudio(result.data); 
    };
    fetchData();
  }, [])

  // turn time stamp seconds into mm:ss
  function timeStampConvert(seconds) {
    return new Date(seconds * 1000).toISOString().substr(14,5);
  }

  return (
    <div className="container">
      <Player url={audiotrack1} />
      <Comment />
      {audio.map(item => (
        <li key={item.id}>
          {item.title} by {item.artist}
          <span>
            {item.comments.map(comment => (
              <li>
                {comment.user} at {timeStampConvert(comment.timestamp_seconds)}
                <br></br>
                <span>{comment.body}</span>
              </li>
            ))}
          </span>
        </li>
      ))}
    </div>
  );
}

export default App;
