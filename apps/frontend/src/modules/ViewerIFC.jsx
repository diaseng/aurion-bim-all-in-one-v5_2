
import React, { useEffect, useRef } from 'react'
import { IFCLoader } from 'web-ifc-three/IFCLoader.js'
import * as THREE from 'three'

export default function ViewerIFC(){
  const mountRef = useRef(null)

  useEffect(() => {
    const width = mountRef.current.clientWidth
    const height = 420

    const scene = new THREE.Scene()
    scene.background = new THREE.Color('#0b1a2b')

    const camera = new THREE.PerspectiveCamera(60, width/height, 0.1, 1000)
    camera.position.set(5, 4, 7)

    const renderer = new THREE.WebGLRenderer({ antialias: true })
    renderer.setSize(width, height)
    mountRef.current.appendChild(renderer.domElement)

    const light = new THREE.DirectionalLight(0xffffff, 1.2)
    light.position.set(5,10,7)
    scene.add(light)
    scene.add(new THREE.AmbientLight(0xffffff, 0.6))

    const grid = new THREE.GridHelper(50, 50)
    scene.add(grid)

    const loader = new IFCLoader()
    const { OrbitControls } = await import('three/examples/jsm/controls/OrbitControls.js')
    const controls = new OrbitControls(camera, renderer.domElement)

    let model = null
    const animate = () => {
      requestAnimationFrame(animate)
      controls.update()
      renderer.render(scene, camera)
    }
    animate()

    // file input
    const input = document.createElement('input')
    input.type = 'file'
    input.accept = '.ifc'
    input.style.margin = '8px 0'
    input.onchange = async (e) => {
      const file = e.target.files[0]
      if (file) {
        const url = URL.createObjectURL(file)
        if (model) { scene.remove(model); model.geometry?.dispose() }
        loader.load(url, (mesh) => {
          model = mesh
          scene.add(mesh)
        })
      }
    }
    mountRef.current.prepend(input)

    return () => {
      renderer.dispose()
      mountRef.current.innerHTML = ''
    }
  }, [])

  return (
    <section className="viewer">
      <h2>Viewer IFC (IFC.js)</h2>
      <div ref={mountRef} />
      <p style={{opacity:.8, marginTop:8}}>Carregue um arquivo .IFC para visualizar.</p>
    </section>
  )
}
