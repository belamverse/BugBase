import React from 'react'

function Error() {
  return (
    <div className="w-full min-h-screen bg-[#fefefe] text-[#111111] flex items-center justify-center px-4 py-8">
      <div className="max-w-md w-full text-center bg-white shadow-md rounded-2xl p-8">
        <h1 className="text-3xl font-bold mb-4 text-red-600">Error 400 – Bad Request</h1>
        <p className="mb-4">
          Authentication via GitHub failed. Something went wrong during the process.
        </p>
        <p className="mb-6 text-sm text-[#555]">
          If this issue persists, feel free to reach out to the BugBase team and we’ll help debug it.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <a
            href="mailto:belammuia0@gmail.com"
            className="px-5 py-2 bg-[#1e293b] text-[#fefefe] rounded-lg hover:bg-[#334155] transition"
          >
            Contact BugBase Team
          </a>
          <a
            href="/"
            className="px-5 py-2 bg-[#e2e8f0] text-[#111111] rounded-lg hover:bg-[#cbd5e1] transition"
          >
            Back to Home
          </a>
        </div>
      </div>
    </div>
  )
}

export default Error
