// import React, { useState } from "react";
// import axios from "axios";
// import ReactMarkdown from "react-markdown"; 
// import "./App.css"; 

// export default function App() {
//   const [prompt, setPrompt] = useState("");
//   const [response, setResponse] = useState("");
//   const [loading, setLoading] = useState(false);

//   const handleSubmit = async () => {
//     if (!prompt.trim()) return alert("Prompt cannot be empty!");

//     setLoading(true);
//     setResponse("");

//     try {
//       const res = await axios.post("http://localhost:8000/generate", {
//         prompt: prompt,
//       });
//       setResponse(res.data.response);
//     } catch (error) {
//       setResponse("Error connecting to backend server.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="container">
//       <h2>AI Integration Hub</h2>
      
//       <textarea
//         className="text-area"
//         placeholder="Type your AI prompt here..."
//         value={prompt}
//         onChange={(e) => setPrompt(e.target.value)}
//       />

//       <button 
//         className="submit-btn" 
//         onClick={handleSubmit} 
//         disabled={loading}
//       >
//         {loading ? "Processing..." : "Ask AI"}
//       </button>

//       {response && (
//         <div className="response-box">
//           <strong>AI Response:</strong>
//           <div className="markdown-content">
//             <ReactMarkdown>{response}</ReactMarkdown>
//           </div>
//         </div>
//       )}
//     </div>
//   );
// }
