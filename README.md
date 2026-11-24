# Helicopter Endsem Prep — PYQ-driven pack

A single-page, offline reader for the helicopter end-semester exam. Scope is
fixed by the instructor: **one forward-flight numerical** (no derivation) and
**flapping of blades** for everything else (numericals *and* derivations).

The pack is deliberately thin. Rather than theory notes, each section is one
past-paper question solved the way it is written in the exam — given data,
formula, substitution, answer with units — plus a one-page formula card for
the last hour before the paper.

## Open it

Open `index.html` in a browser. No server, no build step, no network: KaTeX is
vendored under `vendor/katex/`, so equations render offline.

- `←` / `→` — previous / next section
- `g` — back to the first section
- **Print / PDF** — browser print dialogue (save as PDF)
- **Export view** — one continuous page, no sidebar, for printing
- **Show all** — every section on one scroll

## Flapping derivation reference

The moment balance is explained in [`docs/flapping-moment-balance.md`](docs/flapping-moment-balance.md), using the familiar rotational form `net torque = I × angular acceleration`, with a dimensional check and the centrifugal restoring-torque sign made explicit.

## Layout

```
index.html            reader shell: sidebar, router, quiz binding, KaTeX render
site/content.js       all content — one entry per section, raw HTML strings
site/style.css        dark theme + light print stylesheet
site/app.js           router, quiz reveal logic, iframe/parent messaging
vendor/katex/         KaTeX 0.16.11 (min css/js, auto-render, woff2 fonts)
tools/compute.py      verified numerical engine (forward flight, flapping, coning)
tools/charts.py       power curve, induced-velocity, flapping-frequency sweeps
tools/svg.py          generators for the figures used in the pack
```

## Numerical ground truth

Answers in the pack are not hand-arithmetic. `tools/compute.py` and
`tools/charts.py` compute the full chains and print the intermediate values, so
every number in a worked solution can be traced:

- forward flight: `C_T`, `v_i`, `λ`, `α_T`, `θ₀`, `a₀`, `a₁`, `b₁`, `C_Q` split
  into profile / induced / parasite, total power;
- flapping: `γ`, `a₀`, `a₁`, `b₁`, `ω_β/Ω`, damping `η`, `ξ`;
- coning: `C_F`, `β₀`.

Run them with `python3 tools/compute.py` and `python3 tools/charts.py`.

## Status

- [x] verified numerical engine
- [x] formula card
- [x] reader (navigation, print, export)
- [ ] worked solutions added per past-paper question — waiting on the PYQs
