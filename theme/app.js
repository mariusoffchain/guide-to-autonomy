/*
 * A Guide to Autonomy, browser script.
 * Copyright (C) 2026 the contributors of A Guide to Autonomy. AGPL-3.0-or-later, see LICENSE.
 *
 * Every page arrives complete from build.py. This script only enhances it in
 * place: ticks and read marks kept in the browser's local storage, progress
 * counts, the contents drawer, the search (index loaded on first use), the
 * "On this page" menu on narrow screens, keyboard shortcuts and, when the
 * edition enables it, the offline copy through a service worker. No network
 * request is made except for the search index and the service worker, both on
 * the same site. Nothing is sent anywhere.
 */
(function () {
  'use strict';

  const MAIN = document.getElementById('main');
  const SITE = window.GUIDE_SITE;
  if (!SITE || !MAIN) return;
  const T = SITE.strings || {};
  const t = (key, vars) => String(T[key] || key).replace(/\{(\w+)\}/g, (m, k) => (vars && k in vars ? vars[k] : m));
  const plural = (key, n) => t(key + (n === 1 ? '_one' : '_many'), { n });

  const chapters = SITE.chapters.slice().sort((a, b) => a.number - b.number);
  const byId = new Map(chapters.map((c) => [c.id, c]));
  const totalActions = chapters.reduce((n, c) => n + c.actions.length, 0);

  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.from((root || document).querySelectorAll(sel));
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fold = (s) => String(s).normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();

  /* ---------- browser-local storage ---------- */

  const store = (function () {
    const prefix = SITE.storageKey || 'guide-autonomy.v1';
    const memory = {};
    let persistent = true;
    try {
      localStorage.setItem(prefix + '.probe', '1');
      localStorage.removeItem(prefix + '.probe');
    } catch (e) {
      persistent = false;
    }
    return {
      prefix,
      persistent,
      get(name) {
        if (!persistent) return Object.assign({}, memory[name]);
        try {
          const v = JSON.parse(localStorage.getItem(prefix + '.' + name));
          return v && typeof v === 'object' ? v : {};
        } catch (e) {
          return {};
        }
      },
      set(name, value) {
        memory[name] = value;
        if (!persistent) return;
        try { localStorage.setItem(prefix + '.' + name, JSON.stringify(value)); } catch (e) { /* quota or private mode */ }
      },
      remove(name) {
        delete memory[name];
        if (!persistent) return;
        try { localStorage.removeItem(prefix + '.' + name); } catch (e) { /* ignore */ }
      }
    };
  })();

  function toggleKey(name, key, on) {
    const v = store.get(name);
    if (on) v[key] = true; else delete v[key];
    store.set(name, v);
  }

  /* ---------- progress ---------- */

  function chapterDone(id, done) {
    const c = byId.get(id);
    return c ? c.actions.filter((a) => done[a]).length : 0;
  }

  function refresh() {
    if (!SITE.progress) return;
    const done = store.get('actions');
    const read = store.get('read');
    let doneTotal = 0;
    let readTotal = 0;
    chapters.forEach((c) => {
      doneTotal += chapterDone(c.id, done);
      if (read[c.id]) readTotal += 1;
    });
    $$('[data-stat]').forEach((el) => {
      const s = el.dataset.stat;
      if (s === 'ch-done') el.textContent = chapterDone(el.dataset.ch, done);
      else if (s === 'actions-done') el.textContent = doneTotal;
      else if (s === 'chapters-read') el.textContent = readTotal;
    });
    $$('[data-bar]').forEach((el) => {
      let v = 0;
      if (el.dataset.bar === 'ch') {
        const c = byId.get(el.dataset.ch);
        v = c && c.actions.length ? chapterDone(el.dataset.ch, done) / c.actions.length : 0;
      } else if (el.dataset.bar === 'actions') v = totalActions ? doneTotal / totalActions : 0;
      else if (el.dataset.bar === 'read') v = chapters.length ? readTotal / chapters.length : 0;
      el.style.setProperty('--p', v.toFixed(3));
    });
    $$('[data-read-label]').forEach((el) => { el.textContent = read[el.dataset.readLabel] ? t('read_mark') : ''; });
    $$('[data-read-state]').forEach((el) => { el.textContent = read[el.dataset.readState] ? t('marked_as_read') : ''; });
    $$('[data-ch-item]').forEach((el) => el.classList.toggle('is-read', !!read[el.dataset.chItem]));
    $$('.action-cb').forEach((cb) => {
      cb.checked = !!done[cb.dataset.action];
      const li = cb.closest('.action');
      if (li) li.classList.toggle('is-done', cb.checked);
    });
    $$('.read-cb').forEach((cb) => { cb.checked = !!read[cb.dataset.read]; });
  }

  // The confirmation lasts 6 seconds and as long as the button keeps the focus.
  let resetTimer = null;
  function disarmReset(btn) {
    if (!btn.dataset.armed) return;
    clearTimeout(resetTimer);
    delete btn.dataset.armed;
    btn.textContent = btn.dataset.label;
    const status = $('#progress-status');
    if (status) status.textContent = '';
  }
  function onReset(btn) {
    const status = $('#progress-status');
    if (btn.dataset.armed) {
      clearTimeout(resetTimer);
      store.remove('actions');
      store.remove('read');
      store.remove('last');
      const resume = $('[data-resume]');
      if (resume) resume.hidden = true;
      delete btn.dataset.armed;
      btn.textContent = btn.dataset.label;
      refresh();
      if (status) status.textContent = t('progress_cleared');
      return;
    }
    btn.dataset.armed = '1';
    btn.dataset.label = btn.textContent;
    btn.textContent = t('confirm_clear');
    if (status) status.textContent = t('press_again');
    resetTimer = setTimeout(function wait() {
      if (document.activeElement === btn) resetTimer = setTimeout(wait, 6000);
      else disarmReset(btn);
    }, 6000);
    btn.addEventListener('blur', () => disarmReset(btn), { once: true });
  }

  /* ---------- search ---------- */

  const TYPE_WEIGHT = { chapter: 8, term: 7, tool: 7, section: 6, page: 5, step: 4, action: 4 };
  let searchIndex = [];
  let searchLoading = false;
  const searchInput = $('#search-input');
  const searchResults = $('#search-results');
  const searchStatus = $('#search-status');
  let statusTimer = null;

  function alignedFold(s) {
    let out = '';
    for (let i = 0; i < s.length; i++) {
      const f = fold(s[i]);
      out += f.length === 1 ? f : s[i];
    }
    return out;
  }

  function prepareIndex() {
    searchIndex = (window.GUIDE_SEARCH || []).map((e) => Object.assign({}, e, { ft: alignedFold(e.title), fx: alignedFold(e.text || '') }));
  }

  function loadSearch() {
    if (window.GUIDE_SEARCH) { prepareIndex(); renderResults(searchInput.value); return; }
    if (searchLoading || !SITE.search) return;
    searchLoading = true;
    searchStatus.textContent = t('search_loading');
    const s = document.createElement('script');
    s.src = SITE.search;
    s.onload = () => { searchLoading = false; prepareIndex(); renderResults(searchInput.value); };
    s.onerror = () => {
      searchLoading = false;
      s.remove();
      searchResults.innerHTML = '<p class="results-empty">' + esc(t('search_error')) + '</p>';
      searchStatus.textContent = t('search_error');
    };
    document.head.appendChild(s);
  }
  const searchReady = () => searchIndex.length > 0;

  function search(query) {
    const terms = fold(query).split(/\s+/).filter(Boolean);
    const hits = [];
    if (!terms.length) return { hits, terms, total: 0 };
    searchIndex.forEach((e) => {
      let score = 0;
      for (const term of terms) {
        const inTitle = e.ft.indexOf(term) !== -1;
        if (!inTitle && e.fx.indexOf(term) === -1) return;
        score += inTitle ? 10 : 1;
        if (inTitle && e.ft.indexOf(term) === 0) score += 3;
      }
      hits.push({ e, score: score + (TYPE_WEIGHT[e.type] || 0) });
    });
    hits.sort((a, b) => b.score - a.score);
    return { hits: hits.slice(0, 40), total: hits.length, terms };
  }

  function highlight(text, terms) {
    const f = alignedFold(text);
    const ranges = [];
    terms.forEach((term) => {
      for (let i = f.indexOf(term); i !== -1; i = f.indexOf(term, i + term.length)) ranges.push([i, i + term.length]);
    });
    if (!ranges.length) return esc(text);
    ranges.sort((a, b) => a[0] - b[0]);
    const merged = [];
    ranges.forEach((r) => {
      const last = merged[merged.length - 1];
      if (last && r[0] <= last[1]) last[1] = Math.max(last[1], r[1]); else merged.push(r.slice());
    });
    let out = '';
    let pos = 0;
    merged.forEach((r) => {
      out += esc(text.slice(pos, r[0])) + '<mark>' + esc(text.slice(r[0], r[1])) + '</mark>';
      pos = r[1];
    });
    return out + esc(text.slice(pos));
  }

  function snippet(text, terms) {
    if (!text) return '';
    const f = alignedFold(text);
    let at = -1;
    terms.forEach((term) => { const i = f.indexOf(term); if (i !== -1 && (at === -1 || i < at)) at = i; });
    if (at === -1) at = 0;
    let start = Math.max(0, at - 60);
    if (start > 0) { const sp = text.indexOf(' ', start); if (sp !== -1 && sp < at) start = sp + 1; }
    let end = Math.min(text.length, start + 180);
    if (end < text.length) { const sp = text.lastIndexOf(' ', end); if (sp > at) end = sp; }
    return (start > 0 ? '… ' : '') + highlight(text.slice(start, end), terms) + (end < text.length ? ' …' : '');
  }

  function renderResults(q) {
    const query = q.trim();
    clearTimeout(statusTimer);
    if (!query) {
      searchStatus.textContent = '';
      const sugg = SITE.searchSuggestions || [];
      searchResults.innerHTML = sugg.length
        ? '<div class="search-suggest"><p class="search-suggest-title">' + esc(t('search_try')) + '</p><ul>' +
          sugg.map((s) => '<li><button type="button" class="chip" data-suggest="' + esc(s) + '">' + esc(s) + '</button></li>').join('') + '</ul></div>'
        : '';
      return;
    }
    const r = search(query);
    searchResults.innerHTML = r.hits.length
      ? '<ol class="results" aria-label="' + esc(t('results_label')) + '">' + r.hits.map((h) => {
          const e = h.e;
          const snip = e.text ? snippet(e.text, r.terms) : '';
          return '<li><a class="result' + (e.part ? ' part-' + e.part : '') + '" href="' + esc(e.href) + '">' +
            '<span class="r-kind">' + esc(e.kicker) + '</span><span class="r-title">' + highlight(e.title, r.terms) + '</span>' +
            (snip ? '<span class="r-snip">' + snip + '</span>' : '') + '</a></li>';
        }).join('') + '</ol>'
      : '<p class="results-empty">' + esc(t('search_none')) + '</p>';
    const msg = plural('search_results', r.total) + (r.total > r.hits.length ? t('search_first_shown', { n: r.hits.length }) : '') + '.';
    statusTimer = setTimeout(() => { searchStatus.textContent = msg; }, 450);
  }

  /* ---------- dialogs, menus ---------- */

  const dialogs = {};
  if ($('#search-dialog')) dialogs.search = $('#search-dialog');
  if ($('#contents-dialog')) dialogs.contents = $('#contents-dialog');
  const langBtn = $('#lang-btn');
  const langPanel = $('#lang-panel');

  function openDialog(name, opener) {
    const d = dialogs[name];
    if (!d || d.open) return;
    closeDialogs(false);
    setLang(false);
    setToc(false);
    if (name === 'contents') refresh();
    d._opener = opener || document.activeElement;
    d._restore = true;
    if (typeof d.showModal === 'function') d.showModal(); else d.setAttribute('open', '');
    if (name === 'search') {
      searchInput.focus();
      searchInput.select();
      if (searchReady()) renderResults(searchInput.value); else loadSearch();
    } else {
      (d.querySelector('[aria-current="page"]') || d.querySelector('.dialog-close')).focus();
    }
  }

  function closeDialog(d, restore) {
    if (!d || !d.open) return;
    d._restore = restore !== false;
    if (typeof d.close === 'function') d.close();
    else { d.removeAttribute('open'); d.dispatchEvent(new Event('close')); }
  }
  function closeDialogs(restore) { Object.keys(dialogs).forEach((k) => closeDialog(dialogs[k], restore)); }

  Object.keys(dialogs).forEach((k) => {
    const d = dialogs[k];
    d.addEventListener('close', () => {
      const o = d._opener;
      d._opener = null;
      if (d._restore && o && document.contains(o)) o.focus({ preventScroll: true });
    });
    d.addEventListener('click', (e) => { if (e.target === d) closeDialog(d); });
    d.querySelector('[data-close]').addEventListener('click', () => closeDialog(d));
  });

  if (dialogs.search) {
    dialogs.search.addEventListener('keydown', (e) => {
      if (e.key !== 'ArrowDown' && e.key !== 'ArrowUp') return;
      const items = [searchInput].concat($$('a.result, [data-suggest]', searchResults));
      const i = items.indexOf(document.activeElement);
      if (i === -1) return;
      e.preventDefault();
      items[e.key === 'ArrowDown' ? Math.min(i + 1, items.length - 1) : Math.max(i - 1, 0)].focus();
    });
    searchInput.addEventListener('input', () => { if (searchReady()) renderResults(searchInput.value); else loadSearch(); });
    $('#search-form').addEventListener('submit', (e) => {
      e.preventDefault();
      const first = $('a.result', searchResults);
      if (first) { closeDialog(dialogs.search, false); location.assign(first.getAttribute('href')); }
    });
  }

  function setLang(open) {
    if (!langBtn) return;
    langBtn.setAttribute('aria-expanded', String(open));
    langPanel.hidden = !open;
  }

  function setToc(open) {
    const aside = $('.toc-aside');
    if (!aside) return;
    aside.classList.toggle('is-open', open);
    $('.toc-toggle', aside).setAttribute('aria-expanded', String(open));
  }

  /* ---------- anchors, active section, reading progress ---------- */

  const readBar = $('#read-progress');
  const header = $('.site-header');
  let tocTargets = [];
  let activeTarget = null;

  function markTarget() {
    $$('.is-target').forEach((el) => el.classList.remove('is-target'));
    let id = '';
    try { id = decodeURIComponent(location.hash.slice(1)); } catch (e) { /* malformed */ }
    const target = id ? document.getElementById(id) : null;
    if (target && target.matches('tr, li, .term')) target.classList.add('is-target');
    onScroll();
  }

  function anchorOffset() {
    const toggle = $('.toc-toggle');
    const bar = toggle && toggle.offsetParent !== null ? toggle.offsetHeight : 0;
    return header.offsetHeight + bar + 16;
  }

  let ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => {
      ticking = false;
      updateActive();
      if (readBar && !readBar.hidden) {
        const max = document.documentElement.scrollHeight - window.innerHeight;
        readBar.style.setProperty('--p', max > 0 ? Math.min(1, window.scrollY / max).toFixed(4) : '0');
      }
    });
  }

  function updateActive() {
    if (!tocTargets.length) return;
    // Match the CSS landing position of anchor links, including desktop scroll margin.
    const margin = parseFloat(getComputedStyle(tocTargets[0].el).scrollMarginTop) || 0;
    const offset = Math.max(anchorOffset(), margin) + 4;
    let active = null;
    for (const x of tocTargets) {
      if (x.el.getBoundingClientRect().top - offset <= 0) active = x; else break;
    }
    if (active && window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 2) {
      active = tocTargets[tocTargets.length - 1];
    }
    if (active === activeTarget) return;
    if (activeTarget) activeTarget.a.removeAttribute('aria-current');
    activeTarget = active;
    if (active) active.a.setAttribute('aria-current', 'true');
    const current = $('.toc-current');
    if (current) current.textContent = active ? $('.toc-label', active.a).textContent : '';
  }

  function measureTables() {
    $$('.compare').forEach((fig) => {
      const s = $('.table-scroll', fig);
      if (s) fig.classList.toggle('is-scrollable', s.scrollWidth > s.clientWidth + 1);
    });
  }

  /* ---------- "Continue reading" on the cover ---------- */

  function showResume() {
    const slot = $('[data-resume]');
    const ch = slot && byId.get(store.get('last').chapter);
    if (!ch || !SITE.routes.chapter[ch.id]) return;
    slot.innerHTML = esc(t('continue_reading')) + '<a href="' + esc(SITE.routes.chapter[ch.id]) + '">' +
      esc(t('chapter_n', { n: ch.number })) + ' · ' + esc(ch.title) + '</a>';
    slot.hidden = false;
  }

  /* ---------- offline copy (optional service worker) ---------- */

  function offlineState(reg) {
    const slot = $('[data-offline]');
    if (!slot) return;
    const say = (key) => { slot.textContent = t('offline_' + key); slot.hidden = false; };
    if (!reg || !window.caches) { say('none'); return; }
    const check = async (miss) => {
      const worker = reg.active;
      if (!worker || worker.state !== 'activated') { say(miss || 'saving'); return; }
      const required = $$('script[src], link[rel="stylesheet"]').map((el) => el.src || el.href);
      if (SITE.search) required.push(SITE.search);
      const status = await new Promise((resolve) => {
        const channel = new MessageChannel();
        const timer = setTimeout(() => { channel.port1.close(); resolve(null); }, 3000);
        channel.port1.onmessage = (e) => { clearTimeout(timer); channel.port1.close(); resolve(e.data); };
        worker.postMessage({ type: 'GUIDE_OFFLINE_STATUS' }, [channel.port2]);
      });
      if (!status || !status.ready || !status.cache) { say(miss || 'failed'); return; }
      try {
        const cache = await caches.open(status.cache);
        const hits = await Promise.all(required.map((u) => cache.match(u)));
        say(hits.every(Boolean) ? 'ready' : miss || 'saving');
      } catch (e) { say('none'); }
    };
    const watch = () => {
      const worker = reg.installing || reg.waiting;
      if (!worker) { check(); return; }
      say('saving');
      worker.addEventListener('statechange', () => {
        if (worker.state === 'activated') check();
        else if (worker.state === 'redundant' && !reg.installing && !reg.waiting) check('failed');
      });
    };
    navigator.serviceWorker.addEventListener('controllerchange', () => check());
    reg.addEventListener('updatefound', watch);
    watch();
  }

  /* ---------- events ---------- */

  document.addEventListener('click', (e) => {
    const target = e.target;
    if (!target.closest('.lang')) setLang(false);
    if (!target.closest('.toc-aside')) setToc(false);

    const opener = target.closest('[data-open]');
    if (opener && dialogs[opener.dataset.open]) {
      if (opener.tagName === 'A') {
        if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
        e.preventDefault();
      }
      openDialog(opener.dataset.open, opener);
      return;
    }
    if (target.closest('.toc-toggle')) {
      const btn = target.closest('.toc-toggle');
      setToc(btn.getAttribute('aria-expanded') !== 'true');
      return;
    }
    if (langBtn && target.closest('#lang-btn')) { setLang(langBtn.getAttribute('aria-expanded') !== 'true'); return; }

    const reset = target.closest('[data-reset]');
    if (reset) { onReset(reset); return; }

    const sugg = target.closest('[data-suggest]');
    if (sugg) {
      searchInput.value = sugg.dataset.suggest;
      renderResults(searchInput.value);
      searchInput.focus();
      return;
    }
    if (target.closest('.skip-link')) {
      e.preventDefault();
      (document.getElementById('page-title') || MAIN).focus();
      return;
    }
    const link = target.closest('a[href]');
    if (link && e.button === 0 && !e.metaKey && !e.ctrlKey && !e.shiftKey && !e.altKey) {
      const d = link.closest('dialog');
      if (d) closeDialog(d, false);
      if (link.closest('.toc-aside')) setToc(false);
    }
  });

  document.addEventListener('change', (e) => {
    const el = e.target;
    if (el.matches('.action-cb')) { toggleKey('actions', el.dataset.action, el.checked); refresh(); }
    else if (el.matches('.read-cb')) { toggleKey('read', el.dataset.read, el.checked); refresh(); }
  });

  document.addEventListener('keydown', (e) => {
    const anyDialog = Object.keys(dialogs).some((k) => dialogs[k].open);
    if (e.key === 'Escape') {
      if (langPanel && !langPanel.hidden) { setLang(false); langBtn.focus(); return; }
      const aside = $('.toc-aside.is-open');
      if (aside) { setToc(false); $('.toc-toggle', aside).focus(); return; }
      if (anyDialog && typeof HTMLDialogElement !== 'function') closeDialogs();
      return;
    }
    if (anyDialog || !dialogs.search) return;
    const tag = (e.target.tagName || '').toLowerCase();
    const typing = tag === 'input' || tag === 'textarea' || tag === 'select' || e.target.isContentEditable;
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) { e.preventDefault(); openDialog('search', document.activeElement); return; }
    if (e.key === '/' && !typing && !e.metaKey && !e.ctrlKey && !e.altKey) { e.preventDefault(); openDialog('search', document.activeElement); }
  });

  window.addEventListener('hashchange', markTarget);
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', () => { measureTables(); onScroll(); });
  window.addEventListener('storage', (e) => { if (!e.key || e.key.indexOf(store.prefix) === 0) refresh(); });

  /* ---------- start ---------- */

  $$('[data-js-only]').forEach((el) => { el.hidden = false; });
  if (SITE.progress) {
    $$('.action-cb, .read-cb').forEach((cb) => { cb.disabled = false; });
    const key = MAIN.dataset.page || '';
    if (key.indexOf('chapter/') === 0 && byId.has(key.slice(8))) store.set('last', { chapter: key.slice(8) });
    showResume();
  }
  if (!store.persistent) {
    const note = $('.cl-hint');
    if (note) note.insertAdjacentHTML('beforeend', ' ' + esc(t('storage_unavailable')));
  }
  tocTargets = $$('#page-toc a').map((a) => ({ a, el: document.getElementById(a.dataset.target) })).filter((x) => x.el);
  refresh();
  measureTables();
  markTarget();
  if (SITE.sw && 'serviceWorker' in navigator) {
    navigator.serviceWorker.register(SITE.sw, { scope: SITE.swScope }).then(offlineState, () => offlineState(null));
  } else offlineState(null);
})();
