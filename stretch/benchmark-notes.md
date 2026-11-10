# S1 benchmark - student observations

## A1 - HTTPS and certificate
- Comparable service: Eversports; public fitness-class listings in Luxembourg.
- Captured address: eversports.fr/dcl/fitness/luxembourg. Do not assume the www hostname from the initial suggested URL persisted.
- Student reports entering HTTP returned to HTTPS; no redirect-chain status codes recorded.
- Chrome panel in supplied screenshot says Connection is secure and Certificate is valid.
- Evidence: evidence/S1-A1-eversports-certificate.png.
- Capture time/timezone unrecorded; screenshot supplied 10 November 2026, not asserted as its capture timestamp.
- Comparison: both Coacheey and Eversports have student-observed HTTPS redirects and valid-certificate evidence. This check does not distinguish one as more secure overall.

## A4 - Missing page
- Request: GET https://www.eversports.fr/no-such-page-123.
- Response: 404 Not Found; Disable cache checked; Network preset 3G.
- Visitor sees Chrome-provided This www.eversports.fr page cannot be found, HTTP ERROR 404 and Reload. No branded recovery/home link visible.
- Evidence: evidence/S1-A4-eversports-missing-page.png and evidence/S1-A4-eversports-status.png.
- Compare Coacheey: Coacheey offers a friendly message and Return to Home but responds 200 (soft 404). Eversports communicates the missing resource accurately at HTTP level, while Coacheey offers clearer on-page recovery.
- Lesson: Coacheey should keep its recovery page and change the HTTP response to 404, rather than copy the browser-only experience.
- Actual capture time unrecorded; supplied 10 November 2026.

## B7 - Lighthouse Accessibility
- Actual audited page: https://www.eversports.fr/ (homepage, not Luxembourg listing).
- Score: 100. Export settings: desktop formFactor; screen emulation disabled; Accessibility only. These broad settings match the Coacheey exports, but viewport/browser versions and session conditions are not fully controlled.
- Audit fetchTime: 2026-11-09 22:25:01.133 UTC = 10 November 2026 00:25:01.133 Europe/Bucharest.
- IndexedDB stored-data warning appears in the report. Do not use this report for a loading-performance claim.
- Despite score 100, exported audit label-content-name-mismatch has score 0: Elements with visible text labels do not have matching accessible names. Do not claim no accessibility issues or full accessibility; inspect the affected elements before making a specific recommendation.
- Comparison: Eversports homepage 100 versus Coacheey homepage 94, each one recorded run. Coacheey also flags contrast and missing main landmark; its Events page scores 93. Different pages and conditions limit causal conclusions from score differences.
- Evidence: evidence/S1-B7-eversports-home.html and evidence/S1-B7-eversports-home.png.

## A6 - Rendering (source and Elements compared)
- Raw-source evidence: evidence/S1-A6-eversports-source.png.
- Source contains the main heading Book your yoga and sports activities now, let\'s go! (apostrophe represented as an HTML entity), a closing h1 tag and introductory paragraph.
- This supports substantive initial HTML content and rules out describing the captured source as an empty shell. It does not establish runtime server rendering versus static prerendering or browser-side changes.
- Live Elements evidence: evidence/S1-A6-eversports-elements.png. Selected h1 matches the raw-source heading; supporting paragraph and main landmark are visible. Main content is delivered in initial HTML, consistent with server-supplied/pre-rendered content. The captures do not distinguish runtime server rendering from static prerendering or exclude later browser interactions.
- Browser Find shows 2/2 text occurrences; do not interpret that as the number of h1 elements.
- Capture date/time unrecorded.

- Coacheey comparison: both include substantive source content; Coacheey source/live hero text differs, supporting browser updates. Eversports main heading matches in the captured source/live views. This alone does not prove either whole site is purely server-rendered or faster.

## A7 - Metadata (partial)
Description captured in evidence/S1-A7-eversports-description.png: Find sport studios and facilities throughout France. Search for courses, workshops, events and sports fields that fit you and book easily online. Describes the France-wide homepage. The visible og:title is social metadata, not a verified document title. Other A7 values remain unchecked.
- Actual document title confirmed: Eversports - France - Your click to sport. Evidence: S1-A7-eversports-title-detail.png (cropped supporting detail).
- Student-reported canonical: https://www.eversports.fr (no trailing slash in supplied value).
- Student-reported html lang: en.
- Student-reported XPath //h1 count: 8. Count is not independently captured; multiple h1 elements are not automatically a defect. Context/hierarchy require review.
- rel=sponsored/ugc relevance and matching anchors were not checked; record this A7 limitation.
- Final sixth benchmark check selected as B6 (keyboard task), replacing the earlier planned B8: compare sport discovery shortcut access directly with Coacheey's reported Tab-skipped shortcuts.

## B6 - Keyboard task
Student confirmed all three: Yoga shortcut reachable with Tab; visible focus; Enter opened results. Final clarification: no keyboard trap encountered. A complete key sequence and exact audit time were not recorded.
Compare Coacheey: successful header navigation but sport shortcuts skipped by Tab, while mouse-clicking Yoga opened results. Eversports demonstrated a keyboard-operable Yoga shortcut in this task; this does not establish full keyboard accessibility of the whole site.
Six benchmark IDs now observed: A1, A4, A6, A7, B6, B7. Limitations are retained within each check.
