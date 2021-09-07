import React, { useEffect, useRef, useState } from "react";
import WaveSurfer from "wavesurfer.js";

// options for the audio player
const formWaveSurferOptions = () => ({
    container: '#waveform',
    waveColor: "#eee",
    progressColor: "OrangeRed",
    cursorColor: "OrangeRed",
    height: 200,
    barWidth: 3,
    barRadius: 3,
    responsive: true,
  });

// audio player that takes in url of audio
function Player({ url }) {
    // set ref to elements to replace old ones when react rerenders
    const waveformRef = useRef(null);
    const wavesurfer = useRef(null);
    // set initial states for play and volume
    const [playing, setPlay] = useState(false);
    const [volume, setVolume] = useState(0.5);

    // create new waveSurfer instance on component mount and when url changes
    useEffect(() => {
        // stops play on reload
        setPlay(false);
        // point back to the option settings
        const options = formWaveSurferOptions(waveformRef.current);
        wavesurfer.current = WaveSurfer.create(options);

        wavesurfer.current.load(url);

        wavesurfer.current.on('ready', function() {
        
        // turn play on when reloading component or playing new song
        // wavesurfer.current.play();
        // setPlay(true);

        // maintain volume settings on reload
        if (wavesurfer.current) {
            wavesurfer.current.setVolume(volume);
            setVolume(volume);
        }
        });

        // remove events, elements and disconnects when component unmount
        return () => wavesurfer.current.destroy();
    }, [url]);

    // toggles play and pause
    const handlePlayPause = () => {
        setPlay(!playing);
        // toggles ref as well
        wavesurfer.current.playPause();
    };

    // changes volume state
    const onVolumeChange = e => {
        const { target } = e;
        const newVolume = +target.value;
        // checks for change in volume, and sets state and points ref
        if (newVolume) {
        setVolume(newVolume);
        wavesurfer.current.setVolume(newVolume);
        }
    };

    return (
        <div>
        <div id="waveform" ref={waveformRef} />
            <div className="controls">
                <button onClick={handlePlayPause}>{!playing ? "Play" : "Pause"}</button>
                <input
                type="range"
                id="volume"
                name="volume"
                // wavesurfer recognize value of 0 same as 1, so silence = 0.01
                min="0.01"
                max="1"
                step=".025"
                onChange={onVolumeChange}
                defaultValue={volume}
                />
                <label htmlFor="volume">Volume</label>
            </div>
        </div>
        );
}

export default Player