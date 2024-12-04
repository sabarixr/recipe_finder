import React, { useState, useRef } from "react";

const App = () => {
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState("");
  const [inputText, setInputText] = useState("");
  const [messages, setMessages] = useState([]);
  const mediaRecorderRef = useRef(null);
  const audioChunks = useRef([]);

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorderRef.current = mediaRecorder;

    mediaRecorder.start();
    setRecording(true);

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.current.push(event.data);
    };

    mediaRecorder.onstop = () => {
      const audioBlob = new Blob(audioChunks.current, { type: "audio/wav" });
      const url = URL.createObjectURL(audioBlob);
      setAudioURL(url);
      uploadAudio(audioBlob);
    };
  };

  const stopRecording = () => {
    setRecording(false);
    if (mediaRecorderRef.current) mediaRecorderRef.current.stop();
  };

  const handleRecordingToggle = () => {
    if (recording) {
      stopRecording();
    } else {
      startRecording();
    }
  };

  const uploadAudio = async (audioBlob) => {
    const formData = new FormData();
    formData.append("audio", audioBlob, "recording.wav");

    const response = await fetch("http://localhost:5000/api/audio", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setMessages((prev) => [
      ...prev,
      { type: "user", text: "Audio Message Sent" },
      { type: "bot", text: data.transcription },
    ]);
  };

  const handleTextSubmit = async (e) => {
    e.preventDefault();
    if (!inputText.trim()) return;

    setMessages((prev) => [...prev, { type: "user", text: inputText }]);

    const response = await fetch("http://localhost:5000/api/text", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: inputText }),
    });

    const data = await response.json();
    setMessages((prev) => [...prev, { type: "bot", text: data.response }]);
    setInputText("");
  };

  return (
    <div className="min-h-screen flex flex-col items-center bg-gray-900 text-white p-6">
      <div className="w-full max-w-2xl p-4 bg-gray-800 rounded-lg shadow-lg">
        <h1 className="text-3xl font-bold text-center mb-4">
          GPT Voice & Text
        </h1>

        <div className="h-80 overflow-y-auto bg-gray-700 p-4 rounded-lg">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`p-2 my-2 rounded-lg ${
                msg.type === "user"
                  ? "bg-blue-600 text-right"
                  : "bg-gray-600 text-left"
              }`}
            >
              {msg.text}
            </div>
          ))}
        </div>

        <form
          onSubmit={handleTextSubmit}
          className="mt-4 flex items-center gap-2"
        >
          <input
            type="text"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            placeholder="Type your message..."
            className="flex-1 p-2 rounded-lg bg-gray-600 border border-gray-500 focus:outline-none"
          />
          <button type="submit" className="px-4 py-2 bg-green-500 rounded-lg">
            Send
          </button>
        </form>

        <div className="mt-4 flex items-center justify-between">
          <button
            onClick={handleRecordingToggle}
            className={`px-6 py-2 font-bold rounded-lg shadow-lg ${
              recording
                ? "bg-red-600 hover:bg-red-500"
                : "bg-blue-500 hover:bg-blue-400"
            }`}
          >
            {recording ? "Recording... Click to Stop" : "Record Voice"}
          </button>
        </div>
        {audioURL && (
          <audio src={audioURL} controls className="mt-4 w-full rounded-lg" />
        )}
      </div>
    </div>
  );
};

export default App;
