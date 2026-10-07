(() => {
  const root = document.documentElement;
  let saved;
  try { saved = localStorage.getItem('transformatics-theme'); } catch (_) {}
  root.dataset.theme = saved === 'dark' ? 'dark' : 'light';
  const theme = document.querySelector('.theme');
  const label = () => { theme.textContent = root.dataset.theme === 'dark' ? 'Use light appearance' : 'Use dark appearance'; };
  label();
  theme.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('transformatics-theme', root.dataset.theme); } catch (_) {}
    label();
  });
  // An anchor may point inside an optional derivation or a revealed answer.
  const revealSection = (hash, focus = false) => {
    let id;
    try { id = decodeURIComponent(hash.slice(1)); } catch (_) { return; }
    const target = document.getElementById(id);
    if (!target) return;
    if (target.tagName === 'DETAILS') target.open = true;
    for (let parent = target.parentElement; parent; parent = parent.parentElement) {
      if (parent.tagName === 'DETAILS') parent.open = true;
    }
    if (focus) {
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    }
  };
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link) return;
    revealSection(link.hash, true);
    const outline = link.closest('.chapter-outline');
    if (outline) outline.open = false;
  });
  window.addEventListener('hashchange', () => revealSection(location.hash));
  revealSection(location.hash);

  // Printed lessons include the reasoning hidden by on-screen disclosures.
  let closedBeforePrint = [];
  window.addEventListener('beforeprint', () => {
    closedBeforePrint = [...document.querySelectorAll('article details:not([open]):not(.chapter-outline)')];
    closedBeforePrint.forEach(detail => { detail.open = true; });
  });
  window.addEventListener('afterprint', () => {
    closedBeforePrint.forEach(detail => { detail.open = false; });
    closedBeforePrint = [];
  });

  const searchInput = document.getElementById('book-search');
  if (searchInput) {
    const status = document.getElementById('search-status');
    const results = document.getElementById('search-results');
    let index;
    let failed = false;
    const search = () => {
      results.replaceChildren();
      const query = searchInput.value.trim().toLowerCase();
      if (!query) { status.textContent = 'Enter a search term.'; return; }
      if (failed) { status.textContent = 'The search index could not load. Use the glossary or complete Markdown download.'; return; }
      if (!index) { status.textContent = 'Loading the book index…'; return; }
      const terms = query.split(/\s+/);
      const hits = index.filter(row => terms.every(term => (row.title + ' ' + row.text).toLowerCase().includes(term)));
      status.textContent = `${hits.length} ${hits.length === 1 ? 'chapter' : 'chapters'} found.`;
      for (const row of hits) {
        const item = document.createElement('li');
        const link = document.createElement('a');
        const section = row.sections.find(part => terms.every(term => part.title.toLowerCase().includes(term)));
        link.href = row.url + (section ? '#' + section.id : '');
        link.textContent = row.title + (section ? ' — ' + section.title : '');
        const excerpt = document.createElement('p');
        const start = Math.max(0, row.text.toLowerCase().indexOf(terms[0]) - 60);
        excerpt.textContent = (start ? '…' : '') + row.text.slice(start, start + 240) + '…';
        item.append(link, excerpt); results.append(item);
      }
    };
    searchInput.addEventListener('input', search);
    fetch('search-index.json').then(response => {
      if (!response.ok) throw new Error('Index unavailable');
      return response.json();
    }).then(data => { index = data; search(); }).catch(() => { failed = true; search(); });
  }
})();
