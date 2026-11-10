import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';
import './style.css';

// Invented demonstration records; no live website data or network requests.
const sessions = [
  { id: 1, title: 'Steady Start', sport: 'Yoga', location: 'River Studio', language: 'English', duration: 45 },
  { id: 2, title: 'Everyday Strength', sport: 'Strength', location: 'North Hall', language: 'French', duration: 60 },
  { id: 3, title: 'Move With Ease', sport: 'Pilates', location: 'River Studio', language: 'French', duration: 50 },
  { id: 4, title: 'A Quiet Hour', sport: 'Yoga', location: 'North Hall', language: 'English', duration: 60 },
];
const emptyFilters = { query: '', location: '', sport: '', language: '' };
const fields = [
  { key: 'location', label: 'Location', options: ['River Studio', 'North Hall'] },
  { key: 'sport', label: 'Sport', options: ['Yoga', 'Pilates', 'Strength'] },
  { key: 'language', label: 'Session language', options: ['English', 'French'] },
];

function App() {
  const [filters, setFilters] = useState(emptyFilters);
  const [applied, setApplied] = useState(emptyFilters);
  const results = sessions.filter(session =>
    session.title.toLowerCase().includes(applied.query.trim().toLowerCase()) &&
    fields.every(({ key }) => !applied[key] || session[key] === applied[key])
  );

  function change(key, value) {
    setFilters(current => ({ ...current, [key]: value }));
  }

  function submit(event) {
    event.preventDefault();
    setApplied({ ...filters });
  }

  function chooseSport(sport) {
    const next = { ...filters, sport };
    setFilters(next);
    setApplied(next);
  }

  function clear() {
    setFilters({ ...emptyFilters });
    setApplied({ ...emptyFilters });
  }

  return (
    <>
      <a className="skip-link" href="#main">Skip to main content</a>
      <header className="site-header"><span className="brand">Open Sessions<span aria-hidden="true">.</span></span><span className="badge">Standalone study demo</span></header>
      <main id="main" tabIndex={-1}>
        <div className="intro"><p className="eyebrow">A little movement, a little more possibility</p><h1>Find your next session.</h1><p>Choose a place, a sport and a language. Every example below is fictional.</p></div>
        <section className="search-panel" aria-labelledby="filter-heading">
          <h2 id="filter-heading">Choose what works for you</h2>
          <form onSubmit={submit} aria-labelledby="filter-heading">
            <div className="field-grid">
              <div className="field"><label htmlFor="session-query">Session name</label><input id="session-query" type="search" value={filters.query} onChange={event => change('query', event.target.value)} placeholder="For example, Steady Start" /></div>
              {fields.map(({ key, label, options }) => <div className="field" key={key}><label htmlFor={`session-${key}`}>{label}</label><select id={`session-${key}`} value={filters[key]} onChange={event => change(key, event.target.value)}><option value="">Any {key === 'language' ? 'language' : key}</option>{options.map(option => <option key={option} value={option}>{option}</option>)}</select></div>)}
            </div>
            <div className="actions"><button className="primary" type="submit">Find sessions</button><button className="secondary" type="button" onClick={clear}>Clear filters</button><span className="hint">Your selections stay in place when you search.</span></div>
          </form>
        </section>
        <section className="shortcuts" aria-labelledby="sports-heading"><h2 id="sports-heading">Start with a sport</h2><div className="sport-buttons">{['Yoga', 'Pilates', 'Strength'].map(sport => <button type="button" key={sport} aria-pressed={applied.sport === sport} onClick={() => chooseSport(sport)}>{sport}</button>)}</div></section>
        <section className="results" aria-labelledby="results-heading"><div className="results-header"><h2 id="results-heading">Available sessions</h2><p role="status" aria-atomic="true">{results.length} {results.length === 1 ? 'session' : 'sessions'} found</p></div>
          {results.length ? <ul className="session-list">{results.map(session => <li key={session.id}><article><span className="sport-tag">{session.sport}</span><h3>{session.title}</h3><p>{session.location}</p><p className="details">{session.language} · {session.duration} minutes</p></article></li>)}</ul> : <div className="empty-state"><h3>No matching sessions</h3><p>Try another name or clear the filters to see all four examples.</p><button className="secondary" type="button" onClick={clear}>Show all sessions</button></div>}
        </section>
      </main>
      <footer>Original demonstration for a website field study. No booking, accounts or live service connection.</footer>
    </>
  );
}

createRoot(document.getElementById('root')).render(<App />);
