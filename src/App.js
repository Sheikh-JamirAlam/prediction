import "./App.css";
import Webcam from "react-webcam";
import { useCallback, useRef, useState } from "react";
import axios from "axios";

function App() {
  const webcamRef = useRef(null);
  const [imgSrc, setImgSrc] = useState(null);
  //const [post, setPost] = useState(null);
  const videoConstraints = {
    width: 500,
    height: 500,
    facingMode: "user",
  };

  const capture = useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImgSrc(imageSrc);

    axios
      .post("http://127.0.0.1:5000/predict", {
        image_data: imageSrc,
      })
      .then((response) => {
        // Get the response here

        console.log(response.data);
      });
  }, [webcamRef]);

  return (
    <div className="container App">
      <div className="video-container">
        <h1>Plant Disease Classifier</h1>
        <Webcam id="videoElement" audio={false} height={500} ref={webcamRef} width={500} screenshotFormat="image/jpeg" videoConstraints={videoConstraints} />
        <button id="captureButton" onClick={capture}>
          Capture
        </button>
      </div>
      <div className="prediction-container">
        <h2>Prediction:</h2>
        <div id="capturedImageContainer">{imgSrc && <img src={imgSrc} alt="webcam" />}</div>
        <p id="predictionText"></p>
      </div>
    </div>
  );
}

export default App;
