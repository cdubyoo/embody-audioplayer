import React, { useEffect, useState } from "react";
import "./index.css";
import axios from "axios";
import Player from "./Player";
import audiotrack1 from './audiotrack1.wav'

function App() {
  const [audio, setAudio] = useState([])

  useEffect(() => {
    const fetchData = async () => {
      const result = await axios('/api/audios');
      setAudio(result.data); 
    };
    fetchData();
  }, [])

  return (
    <div className="container">
      <Player url={audiotrack1} />
      {audio.map(item => (
        <li key={item.id}>
          {item.title} by {item.artist}
        </li>
      ))}
    </div>
  );
}

export default App;
