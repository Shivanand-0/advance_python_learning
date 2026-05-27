import React,{ useEffect, useState } from "react";
import axios from "axios";

export default function App(){
  const [prompt,setPrompt]= useState("");
  const [response,setResponse]= useState("");
  const [ln,setLn]=useState(false);

  function handleChange(event){
    setPrompt(event.target.value)
  }

  async function handleSubmit(event){
    setLn(true);
    const res=await axios.post("http://localhost:8000/generate",{prompt:prompt})
    setResponse(res.data.response);
    setLn(false);
  }

  return(
    <>
    <div className="container">
      <h1>
        Full Stack AI Application
      </h1>
      <textarea onChange={handleChange} placeholder="Enter your prompt"></textarea>
      <br /><button onClick={handleSubmit}>{ln?"Generating.....":"Generate"}</button>
      <br /><br /><br />
      <div className="responce-box">
        <h2>AI responce</h2>
        <p>{response?response: "Waiting..."}</p>
      </div>
    </div>
    </>
  )
}
