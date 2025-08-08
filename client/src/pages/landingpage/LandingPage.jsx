import Hero from './sections/Hero'
import Features from './sections/Features'
import CTA from './sections/CTA'
import Footer from './sections/Footer'

export default function LandingPage() {
  return (
    <div className="bg-[#fefefe] text-[#111111]">
      <section className="py-24">
        <Hero />
      </section>

      <section className="py-24">
        <Features />
      </section>

      <section className="py-24">
        <CTA />
      </section>

      <Footer />
    </div>
  )
}
