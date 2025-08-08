import { Bug, Target } from 'lucide-react'

export default function Hero() {
  return (
    <section className="py-20 px-6 text-center">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-5xl font-extrabold mb-4">Welcome to <span className="text-[#facc15]">BugBase</span></h1>
        <p className="text-lg text-gray-700 mb-6">A bug-hunting tool for developers. Find 'em. Fix 'em. Ship faster.</p>
        <div className="flex justify-center gap-4">
          <a href="/register" className="bg-[#1e293b] text-white px-6 py-3 rounded-xl font-semibold hover:bg-[#334155] transition">Register</a>
          <a href="/login" className="bg-[#e2e8f0] text-[#111111] px-6 py-3 rounded-xl font-semibold hover:bg-gray-300 transition">Login</a>
        </div>
        <div className="flex justify-center mt-8 gap-4 text-[#facc15]">
          <Bug size={32} />
          <Target size={32} />
        </div>
      </div>
    </section>
  )
}
