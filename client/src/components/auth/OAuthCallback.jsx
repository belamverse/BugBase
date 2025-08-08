import React, { useEffect } from 'react'
import { useAuth } from '../../context/AuthContext'
import { useNavigate, useLocation } from 'react-router-dom'



function OAuthCallback() {
    const {setTokens} = useAuth()
    const navigate = useNavigate()
    const location = useLocation()

    useEffect(()=>{
        const params = new URLSearchParams(location.search)
        const access = params.get('access')
        const refresh = params.get('refresh')

        if(access && refresh){
            setTokens({access, refresh})
            navigate('/dashboard')
        }
        else{
            console.error('OAuthCallback: OAuth tokens missing in URL parameters. Navigating to home');
            navigate('/')
        }
    },[location, setTokens, navigate])

  return (
    <div><p>Logging yu via github.....</p></div>
  )
}

export default OAuthCallback