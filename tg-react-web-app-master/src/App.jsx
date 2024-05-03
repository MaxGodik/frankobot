/* eslint-disable react/no-unknown-property */
/* eslint-disable no-unused-vars */
import { useState, Suspense, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import { Canvas } from '@react-three/fiber'
import { Environment, OrbitControls } from '@react-three/drei'
import Person from '../public/Untitled'
import Bird from '../public/Birds'

const tele = window.Telegram.WebApp;

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    tele.ready();
  });

  return (
    <div className="container">
      <h1>Наші 3D Моделі</h1>
      <div className="model">
        <Canvas>
          <ambientLight />
          <OrbitControls />
          <Suspense fallback={null}>
            <Person /> 
          </Suspense>
          <Environment preset='sunset'/>
        </Canvas>
      </div>
      <div className="model">
        <Canvas>
            <ambientLight />
            <OrbitControls />
            <Suspense fallback={null}>
              <Bird /> 
            </Suspense>
            <Environment preset='sunset'/>
        </Canvas>
      </div>
      {/* <div className="model">
        <Canvas>
            <ambientLight />
            <OrbitControls />
            <Suspense fallback={null}>
              <Bird /> 
            </Suspense>
            <Environment preset='sunset'/>
        </Canvas>
      </div> */}
    </div>
  )
}

export default App
