import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import LandingPage from './pages/landingpage/LandingPage'
import Auth from './components/auth/Auth'
import Error from './components/auth/Error'
import OAuthCallback from './components/auth/OAuthCallback'
import Dashboard from './pages/dashboard/Dashboard'
import PrivateRoute from './components/routes/PrivateRoute'
import AuthProvider from './context/AuthContext'

function App() {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/auth" element={<Auth />} />
          <Route path="/error" element={<Error />} />
          <Route path="/oauth/callback" element={<OAuthCallback />} />
          
          {/* Protected Dashboard Route */}
          <Route 
            path="/dashboard" 
            element={
              <PrivateRoute>
                <Dashboard />
              </PrivateRoute>
            } 
          />
        </Routes>
      </Router>
    </AuthProvider>
  )
}

export default App
