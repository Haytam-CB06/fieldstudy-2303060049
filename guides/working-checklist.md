# Coacheey Website Field Study

Assignment 2: review a real website, collect original evidence, explain what works, and recommend improvements.

**Current status:** fieldwork in progress. This README is my work checklist; the report contains my findings.

## My study details

| Item | Details |
|---|---|
| Student name | Haytam CHARAFI |
| Student number | 2303060049 |
| Course | SFWE475-advanced web programming |
| Website | https://coacheey.com/ |
| Repository | https://github.com/Haytam-CB06/fieldstudy-2303060049 |
| Website purpose | [FILL: explain who uses it and what they want to do] |
| Why I chose this website | [FILL: how I or someone I know genuinely uses it] |
| Claimed on LMS | [FILL: date and confirmation] |
| Audit date, time and timezone | [FILL: actual session details] |
| Browser version and device | [FILL] |
| Planned scope | Core + Stretch S1 + Stretch S2 + Challenge |
| Completed scope | [FILL: update only after completing each tier] |
| Submission deadline | [FILL: exact LMS date and time; assignment says Week 6, 23:59] |

## How I will work

Complete the steps below in order, one at a time. After every check:

1. Save my original evidence in `evidence/`, using the checklist ID in the filename.
2. Add one row per evidence file to `drafts/evidence-log.md`, with the exact page URL, date, time and timezone.
3. Fill the matching section of `drafts/report.md`: what I observed, followed by what it means for visitors.
4. End the report paragraph with the evidence reference, such as `[A1]`.
5. Tick the checkbox only after the observation, evidence and report entry are complete.

Detailed test instructions: [guides/fieldwork.md](guides/fieldwork.md).

## Step 1: Prepare

- [ ] Confirm the site is eligible: public without login, several pages, a form or search box, a named organisation, and genuine relevance to me.
- [ ] Claim the site on the LMS. The assignment gives conflicting Week 4/Week 5 claim deadlines; confirm with the instructor if needed.
- [ ] Complete my study details above.
- [ ] Use the repository branch `assignment/field-study`.
- [ ] Open a fresh browser window and record browser/version, device, date, time and timezone in the evidence log.
- [ ] Identify public pages and a realistic task, such as finding a suitable coach, if the site supports it.

## Step 2: Core - Part A, technical checks (25 marks)

### A1: HTTPS and redirects

- [ ] Enter `http://coacheey.com`, record the final URL, and inspect certificate validity.
- Save: `A1-redirect.png` and `A1-certificate.png`.
- Focus: whether HTTP leads to HTTPS and whether the certificate is valid. HTTPS alone does not establish that the whole site is trustworthy.

### A2: URL structure

- [ ] Collect five different real page URLs and assess each against all five rules: HTTPS, short/readable, lowercase, hyphens rather than underscores, and few query parameters.
- Record: the five-row table in the report, with pass/fail judgements and reasons.
- Focus: readability and useful structure; explain necessary search/filter parameters rather than assuming all parameters are bad.

### A3: One network request

- [ ] Open DevTools > Network, reload, and inspect the first document request.
- Record: method, status, Content-Type, request count and total size using the browser's exact label. Inspect one Fetch/XHR request if present; otherwise record that none was observed.
- Save: `A3-document-headers.png`, `A3-network-summary.png`, and `A3-xhr.png` if applicable.
- Focus: explain the request and response; distinguish transferred bytes from resource size.

### A4: Missing page

- [ ] Visit one made-up path such as `/no-such-page-123`, inspect its HTTP status, and describe the page visitors see.
- Save: `A4-missing-page.png` and `A4-status.png`.
- Focus: distinguish a real 404 from an error page that returns 200, known as a soft 404. Do not probe hidden paths.

### A5: Caching

- [ ] Inspect Cache-Control for the main document and one image or script.
- Record: resource URLs, exact headers or their absence, and one sentence explaining each.
- Save: `A5-cache-document.png` and `A5-cache-asset.png`.
- Focus: interpret actual directives; do not assume a missing header means no caching occurs.

### A6: Where the page is built

- [ ] Use Ctrl+U to inspect source, then compare distinctive main-page text with the Elements panel.
- Save: `A6-source.png` and `A6-elements.png`.
- Focus: justify server-rendered, browser-rendered or mixed using the evidence from this page; do not guess the framework.

### A7: SEO basics

- [ ] Record title, meta description, canonical link, html lang and h1 count. Check sponsored/ugc link attributes where adverts or user comments make them relevant.
- Save: `A7-seo-01.png` and more numbered captures as needed.
- Focus: found/missing values and page relevance; explain anything marked not applicable.

## Step 3: Core - Part B, visitor experience (25 marks)

### B1: Loading state

- [ ] Set Network throttling to Slow 3G, reload, and capture 2-3 screenshots seconds apart. Restore normal network settings afterwards.
- Save: `B1-loading-01.png`, `B1-loading-02.png`, and optionally `B1-loading-03.png`.
- Focus: what visitors see while waiting, elapsed time per capture, progress feedback and task impact.

### B2: Empty state

- [ ] Search/filter for an impossible value such as `zzzqqq` and record the outcome.
- Save: `B2-empty-search.png`.
- Focus: exact wording, clarity and whether the site offers a useful next step.

### B3: Error state

- [ ] Set DevTools Network to Offline and try a public search or navigation. Restore Online afterwards.
- Save: `B3-offline.png`.
- Focus: exact message, recovery/retry options, and whether the message comes from the site or browser. Record if cached content still works.

### B4: Form validation

- [ ] Select a form and submit only while required fields are deliberately incomplete, so it cannot send. If it could send, stop and record `not tested safely`.
- Save: `B4-form-validation.png`, or explain the safe-testing limitation.
- Focus: error location, useful wording, and whether harmless entered text is retained. Never enter personal data or send anything.

### B5: Form labels

- [ ] Check every field in the B4 form for a visible label. Click the label to test whether focus moves to its field.
- Save: `B5-labels.png`; fill the report's field-by-field table.
- Focus: visible labels, label association and placeholder-only fields.

### B6: Keyboard-only task

- [ ] Complete one real public task using only Tab, Shift+Tab and Enter.
- Save: `B6-keyboard-focus.png`; record task, key/action sequence and outcome.
- Focus: visible focus, logical order, keyboard traps and a skip-to-content link.

### B7: Lighthouse accessibility

- [ ] Run Lighthouse Accessibility on the home page and one inner page; export both reports.
- Save: `B7-lighthouse-home.html` and `B7-lighthouse-inner.html` in `evidence/`.
- Record: URLs, dates/times, settings, both scores and the top three flagged issues, identifying affected pages. If fewer than three appear, say so.
- Focus: visitor impact; an automated score does not prove full accessibility.

### B8: Link and button wording

- [ ] Find up to five actual vague links/buttons or icons without accessible names and suggest clearer wording.
- Save: `B8-link-button-01.png` and further captures as needed; fill the report table.
- Focus: wording in context. Check accessible names before calling an icon unnamed. Report fewer examples honestly if appropriate.

## Step 4: Core - Part C and owner summary (15 marks)

- [ ] Name two things the site does well, supported by evidence.
- [ ] Select the three problems that matter most to visitors and rank them.
- [ ] Explain the ranking in one sentence.
- [ ] For each problem, state: problem, evidence IDs, affected visitors, plain-language fix, estimated effort (low/medium/high), and expected impact (low/medium/high).
- [ ] Complete `drafts/owner-summary.md` for a busy non-technical owner: two strengths, three priority fixes, why they matter, and one simple check for each fix.
- [ ] End the summary with one constructive sentence of thanks.

Focus: evidence and interpretation earn marks. Do not invent faults if the site works well.

## Step 5: Stretch S1 - Benchmark (up to 7 marks)

Working file: [stretch/benchmark.md](stretch/benchmark.md).

- [ ] Choose a comparable public website in the same sector and explain why the comparison is fair.
- [ ] Repeat any six A/B checklist items on it and collect original evidence.
- [ ] Compare both sites in a table using the same six checks.
- [ ] Finish with three sentences explaining what Coacheey could learn.
- [ ] Export the completed file as `stretch/benchmark.pdf`.

Focus: specific observed differences under comparable conditions, not general opinions.

## Step 6: Stretch S2 - One volunteer usability test (up to 8 marks)

Working file: [stretch/usability-test.md](stretch/usability-test.md).

- [ ] Recruit one volunteer who is not a computing student; use an anonymous identifier such as P1.
- [ ] Define three realistic public tasks and success criteria before the test.
- [ ] Ask the volunteer to think aloud. Observe without helping; stop before messages, registration, booking, payment or personal-data entry.
- [ ] Record task completion, time, hesitations and exact words.
- [ ] Ask: "What was the most frustrating moment?" and "What would you change first?" Record the answers verbatim.
- [ ] Link at least one observation to a Core finding, or explain a contradiction.
- [ ] Export as `stretch/usability-test.pdf`.

Focus: actual behaviour from one person; do not generalise to all users or invent quotations.

## Step 7: Challenge - Build one original fix (up to 10 marks)

Working guide: [fix/README.md](fix/README.md).

- [ ] Select one problem I actually documented and cite its evidence ID.
- [ ] Build a small standalone React/Vite or Next.js project inside `fix/`.
- [ ] Choose a suitable scope: an accessible validated form, loading/empty/error states, or a clearer routing example.
- [ ] Use original code, wording and visuals; do not copy the website's code, text or images.
- [ ] Collect relevant before/after screenshots or measurements.
- [ ] Complete `fix/README.md` with the problem/evidence, working run instructions, before/after results and one explained design decision.
- [ ] Verify the project runs and demonstrates the intended improvement without connecting to or sending data to Coacheey.

Focus: one small working fix with evidence of improvement, rather than a large unfinished replacement website.

## Step 8: Export and submit

- [ ] Remove all `[FILL: ...]` placeholders and guidance comments from the final documents.
- [ ] Export `drafts/report.md` to root-level `report.pdf`: maximum six main pages plus an evidence-log appendix.
- [ ] Export `drafts/owner-summary.md` to root-level `owner-summary.pdf`: one page.
- [ ] Include the original screenshots, both Lighthouse exports and completed evidence log.
- [ ] Include both Stretch PDFs and the working Challenge project if completed.
- [ ] Open every final PDF and check page count, readable tables, characters and layout.
- [ ] Update this README's completed scope and AI disclosure accurately.
- [ ] Complete [guides/submission-checklist.md](guides/submission-checklist.md).
- [ ] Merge finished work from `assignment/field-study` into `main` and submit the repository URL on the LMS.

## Final repository layout

```text
fieldstudy-2303060049/
|-- README.md
|-- START-HERE.md
|-- report.pdf                 # Export after completing the report
|-- owner-summary.pdf          # Export after completing the summary
|-- drafts/
|   |-- report.md
|   `-- owner-summary.md
|-- evidence/
|   |-- README.md
|   |-- evidence-log.md
|   |-- A1-redirect.png         # Add actual original captures
|   |-- ...
|   |-- B7-lighthouse-home.html
|   `-- B7-lighthouse-inner.html
|-- guides/
|   |-- fieldwork.md
|   `-- submission-checklist.md
|-- stretch/
|   |-- README.md
|   |-- benchmark.md
|   |-- benchmark.pdf          # Export after S1
|   |-- usability-test.md
|   `-- usability-test.pdf     # Export after S2
`-- fix/
    |-- README.md
    `-- [original standalone project files]
```

The listed evidence files and PDFs must be produced from actual completed work; their presence in this diagram does not mean they exist yet.

## Commit history and course-only access

The assignment requires at least four meaningful commits across at least three genuine days. Finishing today cannot satisfy the three-day requirement unless genuine earlier work already exists. Keep dates honest and explain the limitation to the instructor; do not backdate commits.

Reports and findings must stay inside the course. The repository was public at setup; arrange private instructor access before uploading actual evidence. The assignment also requests a logged-out access check, so clarify this conflict with the instructor.

## Safety and original work

Browse normally and use browser DevTools/Lighthouse only. Do not run scanners, crawlers, load tests or attacks; log in; probe hidden pages; bypass controls; send forms; enter personal data; or contact the site owner. If personal data, leaked credentials or a suspected security hole appear, stop, do not investigate or capture more screenshots, and tell the instructor that day.

All observations, measurements, screenshots and findings must be my own. Use `not observed`, `not applicable` with a reason, or `not tested safely` when accurate.

## AI-use disclosure

AI helped organise the repository and prepare blank templates, this work checklist and testing guidance. [FILL: accurately disclose any further use, such as explaining concepts or polishing English.] I collect and verify the actual observations, measurements, screenshots and findings myself.

