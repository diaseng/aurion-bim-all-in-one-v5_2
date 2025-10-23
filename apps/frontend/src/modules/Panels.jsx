
import React, { useState } from 'react'
const modules = ['minerva','vulcano','netuno','jupiter','saturno','flora','apolo','topos','hermes','diana','cef','stadium']
export default function Panels({ api }){
  const [log, setLog] = useState('')
  const call = async (m) => {
    const r = await fetch(`${api}/${m}/ping`)
    setLog(`${m}: ` + await r.text())
  }
  const mockSaturno = async () => {
    const r = await fetch(`${api}/saturno/mock/load`, {method:'POST'})
    setLog('saturno mock: ' + await r.text())
  }
  const listSaturno = async () => {
    const r = await fetch(`${api}/saturno/items`)
    setLog('saturno list: ' + await r.text())
  }
  return (
    <section className="panel">
      <h2>Módulos</h2>
      <div className="btns">
        {modules.map(m => (<button key={m} onClick={()=>call(m)}>{m.toUpperCase()}</button>))}
      </div>
      <div className="btns" style={{marginTop:12}}>
        <button onClick={mockSaturno}>SATURNO — carregar mock SINAPI</button>
        <button onClick={listSaturno}>SATURNO — listar itens</button>
      </div>
      <pre className="log">{log}</pre>
    </section>
  )
}
