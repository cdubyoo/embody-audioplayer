import React, { useEffect, useState } from "react";
import "./index.css";
import axios from "axios";
import Player from "./Player";
import audiotrack1 from './audiotrack1.wav';
import Comment from "./Comment";

function App() {

  return (
    <div className="container">
      <Player url={audiotrack1} />
      <Comment />
    </div>
  );
}

export default App;
