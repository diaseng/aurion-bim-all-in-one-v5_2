
import React, { useState } from 'react'
import Panels from './modules/Panels.jsx'
import ViewerIFC from './modules/ViewerIFC.jsx'
import './assets/brand/colors.css'

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export default function App(){
  const [status, setStatus] = useState('')
  const ping = async () => {
    const r = await fetch(`${API}/health/ping`)
    setStatus(await r.text())
  }
  return (
    <div className="app">
      <header className="brand">
        <img src="/logo.svg" alt="Aurion BIM" height="28" />
        <h1>Aurion BIM Suite v5.2</h1>
        <button onClick={ping}>Testar API</button>
        <a className="metrics" href={`${API}/metrics`} target="_blank" rel="noreferrer">/metrics</a>
      </header>
      <main className="grid">
        <Panels api={API} />
        <ViewerIFC />
      </main>
      <footer className="foot">© 2025 Cleber Antonio Dias — Aurion BIM Suite v5.2</footer>
      <pre className="log">{status}</pre>
    </div>
  )
}
