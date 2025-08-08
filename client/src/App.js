import React from 'react'
import LandingPage from './pages/landingpage/LandingPage'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Auth from './components/auth/Auth'
import Error from './components/auth/Error'
function App() {
  return (
    <div>
      <Router>
        <Routes>
          <Route path='/' element={<LandingPage />} />
          <Route path='/auth' element={<Auth />} />
          <Route path='/error' element={<Error />} />
        </Routes>
      </Router>
    </div>
  )
}

export default App