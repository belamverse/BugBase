import React from 'react'
import LandingPage from './pages/landingpage/LandingPage'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Auth from './components/auth/Auth'
function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path='/' element={<LandingPage />} />
          <Route path='/auth' element={<Auth />} />
        </Routes>
      </Router>
    </div>
  )
}

export default App