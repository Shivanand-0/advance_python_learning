import { useState } from 'react'
import './App.css'

function App() {
  // States for Sentiment Analysis
  const [sentimentText, setSentimentText] = useState('')
  const [sentimentResult, setSentimentResult] = useState(null)
  const [isSentimentLoading, setIsSentimentLoading] = useState(false)

  // States for Text Generation
  const [genText, setGenText] = useState('')
  const [genResult, setGenResult] = useState(null)
  const [isGenLoading, setIsGenLoading] = useState(false)

  const handleSentiment = async () => {
    setIsSentimentLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/sentiment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: sentimentText })
      })
      const data = await response.json()
      setSentimentResult(`Label: ${data.label} (Confidence: ${(data.score * 100).toFixed(2)}%)`)
    } catch (error) {
      setSentimentResult('Error connecting to backend.')
    }
    setIsSentimentLoading(false)
  }

  const handleGeneration = async () => {
    setIsGenLoading(true)
    try {
      const response = await fetch('http://localhost:8000/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: genText })
      })
      const data = await response.json()
      setGenResult(data.generated_text)
    } catch (error) {
      setGenResult('Error connecting to backend.')
    }
    setIsGenLoading(false)
  }

  return (
    <div className="container">
      <h1>AI Model Serving Portal</h1>

      {/* Sentiment Analysis Task */}
      <div className="model-card">
        <h2>1. Sentiment Analysis</h2>
        <p>Enter text to determine if it is positive or negative.</p>
        <textarea 
          value={sentimentText} 
          onChange={(e) => setSentimentText(e.target.value)}
          placeholder="e.g., I absolutely love this new framework!"
        />
        <button onClick={handleSentiment} disabled={isSentimentLoading || !sentimentText}>
          {isSentimentLoading ? 'Analyzing...' : 'Analyze Sentiment'}
        </button>
        {sentimentResult && (
          <div className="result-box">
            <strong>Result:</strong> {sentimentResult}
          </div>
        )}
      </div>

      {/* Text Generation Task */}
      <div className="model-card">
        <h2>2. Text Generation</h2>
        <p>Enter a prompt and the AI will complete it.</p>
        <textarea 
          value={genText} 
          onChange={(e) => setGenText(e.target.value)}
          placeholder="e.g., In the future, artificial intelligence will..."
        />
        <button onClick={handleGeneration} disabled={isGenLoading || !genText}>
          {isGenLoading ? 'Generating...' : 'Generate Text'}
        </button>
        {genResult && (
          <div className="result-box">
            <strong>Result:</strong> {genResult}
          </div>
        )}
      </div>
    </div>
  )
}

export default App