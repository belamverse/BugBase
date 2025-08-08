import React from 'react'
import { Github } from 'lucide-react'

function Auth() {
  const openGithubLoginForm = () => {
    window.location.href = 'http://localhost:8000/accounts/github/login/'

  }

  return (
    <div className="w-full min-h-screen bg-[#fefefe] text-[#111111] flex items-center justify-center px-4 py-8">
      <div className="max-w-xl w-full text-center bg-white shadow-md rounded-2xl p-10">
        <h1 className="text-3xl font-bold mb-4">Welcome to BugBase</h1>
        <p className="mb-2 text-lg">Join fellow BugBase developers in helping fix other people’s bugs.</p>
        <p className="mb-2 text-sm text-[#555]">This is an active, community-supported platform.</p>
        <p className="mb-6 text-sm text-[#555]">No traditional authentication required.</p>

        <button
          onClick={openGithubLoginForm}
          className="inline-flex items-center justify-center gap-2 bg-[#1e293b] text-[#fefefe] px-6 py-3 rounded-xl font-medium hover:bg-[#334155] transition"
        >
          <Github className="w-5 h-5" />
          Continue with GitHub
        </button>
      </div>
    </div>
  )
}

export default Auth
