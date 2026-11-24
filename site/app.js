/* ------------------------------------------------------------------
   Helicopter Endsem Combat Pack — reader shell
   The router runs inside an <iframe> (app.html?sec=..).  The *parent*
   document (index.html) is what renders KaTeX and hosts the quiz logic,
   so the whole thing can be printed / saved as a clean PDF.
------------------------------------------------------------------- */
(function () {
  const S = window.SECTIONS;
  const wrap = document.getElementById('wrap');
  const navlist = document.getElementById('navlist');
  const barttl = document.getElementById('barttl');
  const params = new URLSearchParams(location.search);
  const parentMode = window.parent && window.parent !== window;

  /* ---------- sidebar ---------- */
  const groups = [];
  S.forEach((s, i) => {
    let g = groups.find(x => x.name === s.part);
    if (!g) { g = { name: s.part, items: [] }; groups.push(g); }
    g.items.push([i, s]);
  });
  navlist.innerHTML = groups.map(g =>
    `<div class="grp">${g.name}</div>` + g.items.map(([i, s]) => {
      const tags = (s.tags || []).map(t => `<span class="tag ${t}">${t === 'der' ? 'D' : 'N'}</span>`).join('');
      return `<a class="n" href="#${s.id}" data-i="${i}"><span class="k">${String(i + 1).padStart(2, '0')}</span>${s.title}${tags}</a>`;
    }).join('')
  ).join('');

  /* ---------- router ---------- */
  function idxFromHash() {
    const h = location.hash.replace('#', '');
    const i = S.findIndex(s => s.id === h);
    return i < 0 ? 0 : i;
  }
  let cur = idxFromHash();
  let showAll = false;

  function paintMath() {
    if (window.renderMathInElement) {
      try {
        renderMathInElement(wrap, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$', right: '$', display: false },
            { left: '\\[', right: '\\]', display: true },
            { left: '\\(', right: '\\)', display: false }
          ],
          throwOnError: false,
          trust: true,
          macros: { '\\dd': '\\mathrm{d}', '\\rt': '\\tfrac' }
        });
      } catch (e) { console.warn('katex', e); }
    }
    bindQuizzes();
  }

  function sectionHTML(s, i, single) {
    return `<section class="s" id="${s.id}" data-i="${i}">
      ${s.html}
      ${single ? navHTML(i) : ''}
    </section>`;
  }
  function navHTML(i) {
    const p = S[i - 1], n = S[i + 1];
    return `<div class="secnav">
      ${p ? `<a href="#${p.id}">← ${p.title}</a>` : '<span></span>'}
      ${n ? `<a href="#${n.id}">${n.title} →</a>` : '<span></span>'}
    </div>`;
  }

  function render() {
    if (showAll) {
      wrap.innerHTML = S.map((s, i) => sectionHTML(s, i, false)).join('');
      barttl.textContent = 'All sections';
    } else {
      wrap.innerHTML = sectionHTML(S[cur], cur, true);
      barttl.textContent = `${cur + 1} / ${S.length} — ${S[cur].title}`;
      window.scrollTo({ top: 0, behavior: 'instant' in window ? 'instant' : 'auto' });
    }
    document.querySelectorAll('#navlist a.n').forEach(a => {
      a.classList.toggle('on', +a.dataset.i === cur && !showAll);
      if (+a.dataset.i === cur) a.scrollIntoView({ block: 'nearest' });
    });
    paintMath();
    document.title = showAll ? 'All sections — Helicopter Pack' : `${S[cur].title} — Helicopter Pack`;
  }

  function go(i) {
    cur = Math.max(0, Math.min(S.length - 1, i));
    showAll = false;
    document.getElementById('btn-all').classList.remove('on');
    location.hash = S[cur].id;
    if (parentMode) { try { parent.location.hash = S[cur].id; } catch (e) {} }
    render();
  }

  window.addEventListener('hashchange', () => {
    if (showAll) return;
    const i = idxFromHash();
    if (i !== cur) { cur = i; render(); }
  });

  document.getElementById('btn-prev').onclick = () => go(cur - 1);
  document.getElementById('btn-next').onclick = () => go(cur + 1);
  document.getElementById('btn-all').onclick = (e) => {
    showAll = !showAll;
    e.currentTarget.classList.toggle('on', showAll);
    render();
  };
  document.getElementById('btn-print').onclick = () => {
    if (parentMode) { try { parent.print(); } catch (e) { window.print(); } } else window.print();
  };
  document.getElementById('btn-clean').onclick = () => {
    if (parentMode) { try { parent.postMessage({ t: 'clean' }, '*'); } catch (e) {} }
    else { document.body.classList.add('clean'); showAll = true; render(); }
  };
  document.addEventListener('keydown', e => {
    if (e.target.closest('input,textarea')) return;
    if (e.key === 'ArrowRight' || e.key === 'l') go(cur + 1);
    if (e.key === 'ArrowLeft' || e.key === 'j') go(cur - 1);
    if (e.key === 'g') go(0);
  });

  /* ---------- quiz ---------- */
  function bindQuizzes() {
    document.querySelectorAll('.qz').forEach(qz => {
      if (qz.dataset.bound) return;
      qz.dataset.bound = '1';
      const ans = qz.dataset.answer;
      const sol = qz.querySelector('.sol');
      if (sol) sol.style.display = 'none';
      qz.querySelectorAll('.opt').forEach(o => {
        o.onclick = () => {
          if (qz.dataset.done) return;
          qz.dataset.done = '1';
          const k = o.dataset.k;
          qz.querySelectorAll('.opt').forEach(x => {
            if (x.dataset.k === ans) x.classList.add('ok');
            else if (x === o) x.classList.add('no');
          });
          if (sol) { sol.style.display = ''; paintMath(); }
        };
      });
      const btn = qz.querySelector('button.reveal');
      if (btn) btn.onclick = () => {
        qz.dataset.done = '1';
        qz.querySelectorAll('.opt').forEach(x => { if (x.dataset.k === ans) x.classList.add('ok'); });
        if (sol) { sol.style.display = ''; paintMath(); }
        btn.remove();
      };
    });
  }

  /* ---------- parent messages ---------- */
  window.addEventListener('message', ev => {
    const d = ev.data || {};
    if (d.t === 'hash' && d.id) { const i = S.findIndex(s => s.id === d.id); if (i >= 0 && i !== cur) { cur = i; render(); } }
    if (d.t === 'next') go(cur + 1);
    if (d.t === 'prev') go(cur - 1);
    if (d.t === 'print') { showAll = true; render(); setTimeout(() => window.print(), 120); }
  });

  render();
})();
