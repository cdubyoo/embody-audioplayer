import "./index.css";
import Player from "./Player";
import audiotrack1 from './audiotrack1.wav';

function App() {

  return (
    <div className="container">
      <Player url={audiotrack1} />
    </div>
  );
}

export default App;
