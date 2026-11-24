# Helicopter Endsem Prep — PYQ-driven pack

A PYQ-driven offline helicopter end-semester study pack. The instructor's stated scope is **one forward-flight numerical** (no derivation) and **flapping of blades** for everything else (numericals and derivations). The uploaded older papers are also indexed for short-answer and pattern revision.

## Download / read

- **One-file guide:** open or download [`docs/helicopter-pyq-guide.html`](docs/helicopter-pyq-guide.html). It bundles the notes, topic checklist, persistent study ticks, and KaTeX (including fonts) into one offline HTML file—no server or network required.
- **App reader:** open `index.html` in a browser for the lightweight section reader and formula card.
- **Markdown references:** [full notes](docs/pyq-full-notes.md), [PYQ checklist and crosswalk](docs/pyq-topic-checklist.md), and [2-mark definition bank](docs/two-mark-definition-bank.md).

- `←` / `→` — previous / next section
- `g` — back to the first section
- **Print / PDF** — browser print dialogue (save as PDF)
- **Export view** — one continuous page, no sidebar, for printing
- **Show all** — every section on one scroll

## Flapping derivation reference

The moment balance is explained in [`docs/flapping-moment-balance.md`](docs/flapping-moment-balance.md), using the familiar rotational form `net torque = I × angular acceleration`, with a dimensional check and the centrifugal restoring-torque sign made explicit. The two uploaded papers are indexed as a tickable [`PYQ topic checklist`](docs/pyq-topic-checklist.md), with repeated topics marked and the instructor's current scope called out separately. The complete study reference—with derivations, numerical methods, analogies, exam cues and worked PYQ calculations—is [`docs/pyq-full-notes.md`](docs/pyq-full-notes.md). For the expected short-answer portion, use the quick [`2-mark definition bank`](docs/two-mark-definition-bank.md).

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
docs/helicopter-pyq-guide.html  downloadable, self-contained interactive guide
docs/pyq-full-notes.md          complete topic notes and worked methods
docs/two-mark-definition-bank.md exam-ready short definitions
docs/pyq-topic-checklist.md     PYQ checklist with notes/definition crosswalk
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

- [x] verified numerical engine and corrected damping/reverse-flow checks
- [x] topic-by-topic notes, derivations, analogies, and 2-mark definitions
- [x] PYQ checklist crosswalk to notes and definition entries
- [x] single-file offline interactive HTML guide with rendered equations
- [ ] expand any remaining PYQ numerical into a fully detailed, question-specific solution as needed
