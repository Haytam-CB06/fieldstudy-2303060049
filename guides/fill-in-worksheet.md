# Submission fill-in worksheet

This is AI-assisted planning guidance, not a completed report. Fill fields using your own fieldwork, write your final explanations yourself, and follow your instructor's rules on assistance. Do not submit this worksheet as findings.

## 1. Project details — README.md and report title block

- Full name: [YOUR NAME]
- Student number: [YOUR NUMBER]
- Course: [YOUR COURSE]
- Website: [EXACT SITE URL]
- Organisation: [NAME VERIFIED ON THE SITE]
- Purpose and intended users: [YOUR OWN DESCRIPTION]
- Why you chose it: [GENUINE USE BY YOU OR PEOPLE YOU KNOW]
- LMS claim: [DATE AND CONFIRMATION]
- Actual audit dates/times/timezone: [SESSION DETAILS]
- Browser name/version: [BROWSER AND VERSION]
- Device and viewport: [DEVICE; WIDTH x HEIGHT]
- Tiers actually completed: [CORE / S1 / S2 / CHALLENGE]
- Exact submission deadline: [LMS DATE AND TIME]
- Assistance disclosure, if applicable: [ACCURATE DESCRIPTION; FOLLOW INSTRUCTOR RULES]

## 2. Evidence log — drafts/evidence-log.md

Record one row per actual screenshot or exported Lighthouse report. Never infer capture time from a server Date header or assume a file modification time is the capture time.

| ID | Actual relative filename | What this proves | Actual capture date/time + timezone | Exact page URL |
|---|---|---|---|---|
| [A/B/S/C ID] | [evidence/FILE] | [OBSERVATION] | [CONFIRMED TIME] | [FULL URL] |

## 3. Core Part A — drafts/report.md

For each check, write one concise paragraph in your own words: what you observed, what it means and its evidence reference, such as [A4]. Use the requested tables as support.

### A1 — HTTPS

- Address you entered: [HTTP URL]
- Final address: [FINAL URL]
- Certificate-validity message: [EXACT RESULT]
- Interpretation and boundary: [WHAT THIS ESTABLISHES ABOUT THE CONNECTION]
- Evidence: [FILENAMES] [A1]

### A2 — Five URLs

| Actual URL | HTTPS pass/fail | Short/readable pass/fail | Lowercase pass/fail | Hyphens/no underscores pass/fail | Few query parameters pass/fail | Reason for failures |
|---|---|---|---|---|---|---|
| [URL 1] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [REASON] |
| [URL 2] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [REASON] |
| [URL 3] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [REASON] |
| [URL 4] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [REASON] |
| [URL 5] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [RESULT] | [REASON] |

Your interpretation: [WHAT THE SAMPLE SHOWS; ANY LIMITATION] [A2]

### A3 — Network

- Main document URL: [URL]
- Method / status / Content-Type: [EXACT VALUES]
- Request count: [COUNT AT RECORDED POINT]
- Transferred size: [VALUE AND UNITS]
- Resource size, if shown: [VALUE AND UNITS]
- Cache/network conditions: [ACTUAL SETTINGS]
- One Fetch/XHR request URL/method/status: [VALUES OR NONE OBSERVED]
- Interpretation: [WHAT THE OBSERVED REQUESTS MEAN]
- Evidence: [FILENAMES] [A3]

### A4 — Missing page

- Deliberately nonexistent URL: [EXACT URL]
- Fresh HTTP status: [STATUS FROM NETWORK]
- Cache settings used: [SETTING]
- Visible message: [EXACT WORDING]
- Recovery option: [WHAT WAS PRESENT]
- True 404 / soft 404 / other: [CLASSIFICATION AND REASON]
- Visitor/search-engine implication: [YOUR EXPLANATION]
- Evidence: [FILENAMES] [A4]

### A5 — Caching

| Resource | Exact URL | Exact Cache-Control, or absent | Meaning in one sentence |
|---|---|---|---|
| Main document | [URL] | [HEADER] | [INTERPRETATION] |
| One image/script | [URL] | [HEADER] | [INTERPRETATION] |

Evidence: [FILENAMES] [A5]

### A6 — Rendering

- Distinctive visible main text checked: [TEXT]
- Present in raw source? [YES/NO; LOCATION]
- Present in live Elements? [YES/NO; LOCATION]
- Classification: [SERVER / BROWSER / MIXED]
- Justification and uncertainty: [EVIDENCE-BASED REASON]
- Evidence: [SOURCE AND ELEMENTS FILENAMES] [A6]

### A7 — SEO

| Item | Actual value/count, missing or not applicable | Interpretation |
|---|---|---|
| Title | [VALUE] | [JUDGEMENT] |
| Meta description | [VALUE] | [JUDGEMENT] |
| Canonical link | [VALUE] | [JUDGEMENT] |
| html lang | [VALUE] | [JUDGEMENT] |
| h1 count | [COUNT] | [JUDGEMENT] |
| sponsored/ugc links, where relevant | [RESULT] | [REASON/APPLICABILITY] |

Evidence: [FILENAMES] [A7]

## 4. Core Part B — drafts/report.md

| ID | Fill these observed details | Then explain |
|---|---|---|
| B1 | [PAGE]; [ACTUAL THROTTLING/CACHE SETTINGS]; [2–3 CAPTURE TIMES AND VISIBLE STATES]; [FILENAMES] | [WHAT WAITING VISITORS UNDERSTAND AND CAN DO] |
| B2 | [SEARCH/FILTER]; [IMPOSSIBLE QUERY]; [EXACT RESULT MESSAGE]; [NEXT STEP]; [FILE] | [CLARITY AND RECOVERY] |
| B3 | [OFFLINE ACTION]; [EXACT MESSAGE/OUTCOME]; [SITE OR BROWSER MESSAGE]; [RETRY OPTION]; [FILE] | [WHAT A VISITOR CAN DO AFTER FAILURE] |
| B4 | [FORM URL]; [REQUIRED FIELDS LEFT EMPTY]; [ERROR WORDING/LOCATION]; [INPUT RETAINED?]; [FILE] | [FEEDBACK USEFULNESS; OR WHY NOT TESTED SAFELY] |
| B5 | [EVERY FIELD]; [VISIBLE LABEL YES/NO]; [CLICK-TO-FOCUS YES/NO]; [PLACEHOLDER ONLY?]; [FILES] | [ABILITY TO IDENTIFY AND USE FIELDS] |
| B6 | [TASK/START URL]; [SUCCESS CRITERION]; [KEY SEQUENCE]; [FOCUS]; [ORDER]; [TRAPS]; [SKIP LINK]; [OUTCOME]; [FILE] | [TASK-SPECIFIC KEYBOARD EXPERIENCE] |
| B7 | [HOME URL/SCORE]; [INNER URL/SCORE]; [DATES/SETTINGS]; [TOP THREE ACTUAL ISSUES AND AFFECTED PAGES]; [TWO EXPORTED REPORTS] | [VISITOR IMPACT AND AUTOMATION LIMITS] |
| B8 | [UP TO FIVE ACTUAL TEXT/ICON EXAMPLES]; [CONTEXT]; [ACCESSIBLE NAME]; [BETTER WORDING]; [FILES] | [WHY THE WORDING/NAME NEEDS IMPROVEMENT] |

End each report paragraph with the matching ID. For B5 and B8, add one table row per field/example. Restore normal networking after B1/B3. State if fewer than three Lighthouse issues or five wording examples exist.

## 5. Core Part C — drafts/report.md

- Strength 1: [OBSERVED STRENGTH + EVIDENCE + VISITOR BENEFIT]
- Strength 2: [OBSERVED STRENGTH + EVIDENCE + VISITOR BENEFIT]
- Ranking explanation: [ONE SENTENCE EXPLAINING ORDER]

Repeat for priorities 1, 2 and 3:

- Problem: [ONE SENTENCE]
- Evidence: [A/B IDS AND FILES]
- Who/task affected: [SPECIFIC VISITORS AND TASK]
- Practical fix: [PLAIN-LANGUAGE CHANGE]
- Effort: [LOW/MEDIUM/HIGH + ESTIMATE RATIONALE]
- Impact: [LOW/MEDIUM/HIGH + EVIDENCE-BASED REASON]

## 6. Owner summary — drafts/owner-summary.md

- Heading: Website review for [ORGANISATION]
- Author/date: [NAME AND DATE]
- Two strengths: [TWO SHORT EVIDENCE-BACKED POINTS]
- Priority 1: [VISITOR EXPERIENCE]; [WHY IT MATTERS]; [WHAT TO ASK A DEVELOPER TO DO]; [ONE SIMPLE OWNER CHECK]
- Priority 2: [SAME FOUR FIELDS]
- Priority 3: [SAME FOUR FIELDS]
- Closing thanks: [ONE CONSTRUCTIVE SENTENCE]

Write this yourself in plain language and keep the exported summary to one page.

## 7. Stretch S1 — stretch/benchmark.md

- Second site / organisation / reason comparable: [DETAILS]
- Audit dates and comparable settings: [DETAILS]
- Six selected checklist IDs: [IDS]
- For each: [COACHEEY RESULT + EVIDENCE]; [SECOND SITE RESULT + EVIDENCE]; [WHAT DIFFERENCE MEANS]
- Lessons: [THREE SENTENCES]

## 8. Stretch S2 — stretch/usability-test.md

- Anonymous volunteer ID: [P1]
- Not a computing student: [CONFIRM]
- Date/time/device/browser: [DETAILS]
- Task 1 / success criterion / actual time / outcome / hesitation / exact words: [ACTUAL OBSERVATIONS]
- Task 2: [SAME FIELDS]
- Task 3: [SAME FIELDS]
- “What was the most frustrating moment?”: [VERBATIM ANSWER]
- “What would you change first?”: [VERBATIM ANSWER]
- Connection or contradiction to a Core finding: [EXPLANATION + ID]

Do not help during the tasks or invent quotes. Photographs of the participant are not required.

## 9. Challenge — fix/README.md and your original project

- Documented problem and Core evidence ID: [PROBLEM + ID]
- Standalone framework: [REACT/VITE OR NEXT.JS]
- Working fix: [WHAT YOUR ORIGINAL CODE DOES]
- Prerequisites/install/start/local URL: [ACTUAL VERIFIED INSTRUCTIONS]
- Before: [OBSERVED BASELINE + EVIDENCE]
- After: [VERIFIED DEMO RESULT + EVIDENCE]
- Comparison limitation: [DIFFERENT SITE/LOCAL CONDITIONS, IF RELEVANT]
- One design decision and reason: [YOUR EXPLANATION]
- Verification steps and actual outcomes: [RESULTS]

## 10. Screenshot checklist

This inventory describes what still needs to exist. It does not create evidence. Do not create blank image files for missing checks. Your folder currently contains ten student-supplied screenshots; their adequacy still depends on the required details being legible.

| Check | Your existing files | Still required or to verify |
|---|---|---|
| A1 | A1-redirect.png; A1-certificate.png | Full final HTTPS URL visible; actual date/time logged |
| A2 | No student captures needed by default | Five actual URLs assessed against all five rules; screenshots optional |
| A3 | A3-network-summary.png; A3-document-headers.png; A3-fetch.png | Address bar visible in document-headers capture; exact values/log |
| A4 | A4-missing-page.png; A4-status-fresh.png; A4-status.png | Fresh status is main evidence; 304 capture is optional context |
| A5 | A5-cache-document.png; A5-cache-asset.png | Exact selected asset URL visible, not only its truncated name |
| A6 | Missing | A6-source.png; A6-elements.png |
| A7 | Missing | Readable captures of metadata, lang and h1 count; sponsored/ugc where relevant |
| B1 | Missing | B1-loading-01.png; B1-loading-02.png; optional -03, seconds apart |
| B2 | Missing | B2-empty-search.png |
| B3 | Missing | B3-offline.png |
| B4 | Missing | B4-validation.png if safely testable; otherwise explanation |
| B5 | Missing | B5-labels.png plus field-by-field observations |
| B6 | Missing | B6-keyboard-focus.png plus actual task/key log |
| B7 | Missing | Two Lighthouse HTML exports; score/issue screenshots optional |
| B8 | Missing | Up to five contextual example captures, as actually found |
| S1 | Missing | Supporting captures for the same six selected checks on a second site |
| S2 | No photo required | Actual observation/timing/quote table |
| Challenge | Missing | Relevant before/after captures and working original code |

## 11. Final exports

- report.pdf: [MAXIMUM SIX MAIN PAGES + COMPLETED EVIDENCE-LOG APPENDIX]
- owner-summary.pdf: [ONE PAGE]
- stretch/benchmark.pdf: [COMPLETED S1]
- stretch/usability-test.pdf: [COMPLETED S2]
- fix/: [WORKING ORIGINAL PROJECT + README + BEFORE/AFTER EVIDENCE]
- Git: [4+ MEANINGFUL COMMITS ACROSS 3+ GENUINE DAYS; REQUIRED BRANCH MERGED TO MAIN]

The evidence folder can contain screenshots and the two required Lighthouse exports. Working instructions and the editable log may live elsewhere; include the completed log in the report appendix. Keep attribution accurate for any assistance or outside reference material you use.
