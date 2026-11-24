/* ------------------------------------------------------------------
   Content for the reader.  Deliberately small: this pack is built
   around the PYQs, not around theory notes.  Each past-paper question
   will become one section with a methodical worked solution.
   Use String.raw so LaTeX backslashes survive.
------------------------------------------------------------------- */
const R = String.raw;

window.SECTIONS = [

/* ================================================================ 1 */
{
  id: 'start',
  part: 'Start here',
  title: 'How this pack works',
  tags: ['mem'],
  html: R`
  <h2>Built around your question papers</h2>
  <p class="lead">No theory dump. Every section below will be <em>one past-paper question</em>, solved the way you would write it in the exam: given data, formula, substitution, answer with units.</p>

  <div class="card">
    <div class="ch">The plan</div>
    <ol class="steps">
      <li><b>You send the PYQs</b> — photos, PDF, or typed. Repeated questions get solved first, because they are the ones most likely to come back.</li>
      <li><b>Each question gets one page</b> with the full method: what is given, which formula, why that formula, the substitution, and the final answer with units.</li>
      <li><b>Number-identical twins get a template</b> — one solved page plus the variants the examiner usually twists (different μ, different rpm, hover vs forward flight).</li>
      <li><b>Last hour:</b> the formula card only. That is the page to re-read in the corridor.</li>
    </ol>
  </div>

  <div class="card cb">
    <div class="ch">Scope you confirmed</div>
    <div class="kv">
      <span class="k">forward flight</span><span>exactly one question — <b>numerical only</b>, no derivation</span>
      <span class="k">flapping</span><span>everything else — <b>numericals and derivations</b></span>
      <span class="k">source</span><span>whatever was covered in class (the 39-page notes)</span>
    </div>
  </div>

  <h3>What is already checked and waiting</h3>
  <p class="small muted">So that the moment a question lands, the arithmetic is already verified rather than done by hand in a hurry.</p>
  <table class="t">
    <thead><tr><th>Block</th><th>Status</th></tr></thead>
    <tbody>
      <tr><td>Forward-flight numerical engine (C<sub>T</sub>, v<sub>i</sub>, λ, α<sub>T</sub>, θ₀, a₀, a₁, b₁, power split)</td><td><span class="pill g">verified</span></td></tr>
      <tr><td>Flapping coefficients and hinge-offset quantities (γ, a₀, a₁, b₁, ω<sub>β</sub>, η, ξ)</td><td><span class="pill g">verified</span></td></tr>
      <tr><td>Coning numerical (W, N, R, rpm → β₀)</td><td><span class="pill g">verified</span></td></tr>
      <tr><td>Per-question worked solutions</td><td><span class="pill a">waiting for PYQs</span></td></tr>
    </tbody>
  </table>

  <div class="callout">
    <div>
      <b>How to send a paper.</b> A photo is enough — straight-on, whole page, even if the handwriting is rough. If it is a PDF scan, send the file. I read the question text, solve it, and add it here.
    </div>
  </div>

  <p class="tiny">Navigation: <kbd>←</kbd> <kbd>→</kbd> for previous/next, <kbd>g</kbd> to come back here. “Export view” puts everything on one page for printing or saving as PDF.</p>
  `
},

/* ================================================================ 2 */
{
  id: 'formulas',
  part: 'Reference',
  title: 'Formula card',
  tags: ['num', 'der'],
  html: R`
  <h2>Formula card</h2>
  <p class="lead">Only the relations the past-paper questions actually use. Every line here has already been checked against your class notes.</p>

  <div class="card">
    <div class="ch">Definitions</div>
    <div class="fx key">$$\mu=\frac{V}{\Omega R}\qquad \lambda=\frac{v_i}{\Omega R}\qquad C_T=\frac{T}{\rho A(\Omega R)^2}\qquad \sigma=\frac{Nc}{\pi R}\qquad \gamma=\frac{\rho a c R^4}{I_\beta}$$</div>
    <div class="fx">$$\lambda=\mu\sin\alpha+\lambda_i\;\approx\;\mu\alpha+\lambda_i$$</div>
  </div>

  <div class="card">
    <div class="ch">Hover and climb</div>
    <div class="fx key">$$T=2\rho A\,v_i\sqrt{V^2+v_i^2}\qquad v_h=\sqrt{\frac{T}{2\rho A}}$$</div>
    <div class="fx key">$$\left(\frac{v_i}{v_h}\right)^4+\left(\frac{V}{v_h}\right)^2\left(\frac{v_i}{v_h}\right)^2-1=0$$</div>
    <div class="fx">$$C_T=\tfrac12\sigma a\left[\theta_0\left(\tfrac13+\tfrac{\mu^2}{2}\right)-\frac{\lambda}{2}\right]$$</div>
  </div>

  <div class="card">
    <div class="ch">Forward-flight flapping</div>
    <div class="fx key">$$a_0=\frac{\gamma}{8}\left[\theta_0(1+\mu^2)-\tfrac43\lambda\right]$$</div>
    <div class="fx key">$$a_1=\frac{\mu\left(\tfrac83\theta_0-2\lambda\right)}{1-\mu^2/2}\qquad b_1=\frac{\tfrac43\,\mu\,a_0}{1+\mu^2/2}$$</div>
  </div>

  <div class="card">
    <div class="ch">H-force and power</div>
    <div class="fx">$$C_{H_0}=\frac{\sigma C_{D_0}\mu}{4}$$</div>
    <div class="fx key">$$C_Q=\tfrac18\sigma C_{D_0}(1+K_1\mu^2)+k\lambda_iC_T+\mu\frac{D_p}{W}C_T$$</div>
    <div class="fx">$$P=C_Q\,\rho A(\Omega R)^3$$</div>
  </div>

  <div class="card">
    <div class="ch">Coning</div>
    <div class="fx">$$C_F=m\Omega^2R^2/2\qquad \beta_0=\frac{L}{C_F}$$</div>
    <div class="fx">$$\text{static stability: }\frac{\mathrm{d}M_{C_F}}{\mathrm{d}\beta}<0\qquad \text{damping: }\mathrm{d}\alpha=-\frac{\dot\beta}{\Omega}$$</div>
  </div>

  <div class="card">
    <div class="ch">Hinge offset</div>
    <div class="fx key">$$\dot\beta+\Omega^2(1+\varepsilon)\beta=\frac{M_a}{I_\beta}\qquad \varepsilon=\frac{3e}{2(1-e)}\qquad \omega_\beta=\Omega\sqrt{\frac{2+e}{2(1-e)}}$$</div>
    <div class="fx key">$$\eta=\frac{(1-e)^3(3+e)}{3}\qquad \xi=\frac{\gamma\,\eta}{16\,\omega_\beta}$$</div>
    <div class="fx">$$\beta''+\omega_\beta^2\beta=\frac{\gamma}{8}\left(C_1\theta-C_2\beta'\right)\qquad C_1=1-\tfrac43e,\;\; C_2=1-\tfrac83e$$</div>
  </div>

  <div class="card">
    <div class="ch">Limits</div>
    <div class="fx">$$\text{reversed-flow area fraction}=\frac{\mu^2}{4}\qquad r_{\text{rev}}=\mu R$$</div>
    <div class="kv">
      <span class="k">no reverse flow</span><span>μ ≤ 0</span>
      <span class="k">practical limit</span><span>μ ≤ 0.4</span>
      <span class="k">tip Mach</span><span>M<sub>tip</sub> ≈ 0.85 max</span>
    </div>
  </div>

  <p class="tiny">Ask for a symbol and I will add it — nothing goes on this card that a paper has not used.</p>
  `
}

];
