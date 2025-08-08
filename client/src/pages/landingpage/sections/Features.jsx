export default function Features() {
  const features = [
    { title: 'Real-Time Bug Tracking', desc: 'See bugs as they happen in your projects.' },
    { title: 'Simple Setup', desc: 'Integrate BugBase with just a few lines of code.' },
    { title: 'Team Friendly', desc: 'Collaborate, assign, and conquer bugs together.' },
  ]

  return (
    <section className="py-16 px-6 bg-[#fcfcfc]">
      <div className="max-w-5xl mx-auto text-center">
        <h2 className="text-3xl font-bold mb-10">Why Choose BugBase?</h2>
        <div className="grid md:grid-cols-3 gap-6">
          {features.map((feat, i) => (
            <div key={i} className="p-6 bg-white rounded-xl shadow hover:shadow-md transition">
              <h3 className="text-xl font-semibold mb-2">{feat.title}</h3>
              <p className="text-gray-700">{feat.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
