import { Navigate } from 'react-router-dom'
import { useAuth } from '../../context/AuthContext'

function PrivateRoute({ children }) {
  const { isAuthenticated } = useAuth()

  return isAuthenticated ? children : <Navigate to='/error' replace />
}

export default PrivateRoute
