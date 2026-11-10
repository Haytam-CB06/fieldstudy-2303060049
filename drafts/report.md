<!-- WORKING TEMPLATE. Fill your own findings, delete guidance/comments, export to report.pdf at repository root. Max 6 pages before the evidence-log appendix. -->
# Coacheey website field study
**Student:** Haytam CHARAFI | **Number:** 2303060049

**Site:** https://coacheey.com/ | **Organisation:** [FILL: verified name]

**Audit:** [FILL: actual date/time/timezone] | **Browser/device:** [FILL]

**Purpose and scope:** [FILL: 2-3 sentences about users, the site's purpose, and public pages/tasks covered.]

**Method and limitations:** [FILL: briefly state actual browser/network conditions, public-page scope and material limitations; identify any check not completed safely. Procedures are documented in guides/methodology.md.]

> Focus: state what you saw, then what it means. One concise paragraph per checklist item, ending in its evidence reference, e.g. [A4]. Tables may support the paragraph. Do not paste the assignment checklist as your findings. Read guides/fieldwork.md for exact testing steps.

# Part A: Under the hood

## A1: HTTPS and redirects
<!-- Focus: Requested URL; final URL; redirect behaviour; certificate validity. Interpretation: Separate transport security from overall site trustworthiness. Do not claim HTTPS proves the site is safe. -->
[FILL: requested HTTP URL, final URL, and certificate-validity result]. [FILL: connection-security interpretation supported by those observations; distinguish it from overall site trust]. [A1]

## A2: URL structure
<!-- Focus: Five URLs; pass/fail for each of five rules; short justification for failures. Interpretation: Judge readability and practical meaning. Do not call all parameters wrong; explain necessary filters if observed. -->
[FILL: write your own interpretation of the five URLs below. The filtered-coaches URL is long because city and sport values are UUIDs; the two parameters have a useful filtering purpose. Confirm and paste the full URLs, including their schemes, before finalising the table. Assessment below is draft editorial assistance based on your supplied screenshots.] [A2]

| Actual page URL | HTTPS | Short/readable | Lowercase | Hyphens/no underscores | Few query parameters | Reason for any fail |
|---|---|---|---|---|---|---|
| coacheey.com/public-sessions | [FILL: confirm full scheme] | Pass | Pass | Pass | Pass: none | Short hyphenated path; Events label is clearer than public-sessions. |
| coacheey.com/coaches?city=d3e88837-bff6-444e-8ba8-13906ae37e0b&sport=37644da5-c4da-46f2-883a-84da3c98e1c4 | [FILL: confirm full scheme and exact copied URL] | Fail | Pass | Pass: no underscores | Pass: two relevant filters | UUID values make the URL long and difficult to interpret; parameters preserve selected city and sport. |
| coacheey.com/auth | [FILL: confirm full scheme] | Pass: short, though technical | Pass | Pass: no separator needed | Pass: none | auth is concise but less familiar than sign-in to a non-technical visitor. |
| coacheey.com/coach/bee-mindful-3b6ad569 | [FILL: confirm full scheme] | Pass | Pass | Pass | Pass: none | Readable coach name with a short disambiguating identifier. |
| coacheey.com/for-coaches | [FILL: confirm full scheme] | Pass | Pass | Pass | Pass: none | Concise hyphenated audience-specific path. |

## A3: One request, closely
<!-- Focus: Method; HTTP status; Content-Type; request count; total transferred/resource size with exact displayed label; Fetch/XHR URL/method/status if one exists. Interpretation: Explain what the response represents. Record cache/network conditions; distinguish transferred bytes from resource size. Say if no Fetch/XHR was observed. -->
[FILL: document URL, method, HTTP status and Content-Type; request count and size with the exact displayed label; network/cache conditions]. [FILL: one Fetch/XHR request if present, or state none was observed; explain the response and distinguish transfer size from resource size]. [A3]

## A4: A missing page
<!-- Focus: Exact test URL; actual status code; what the visitor sees; recovery links. Interpretation: Distinguish a true 404 from a friendly page returning 200 (soft 404). A screenshot of an error message alone cannot prove the status. -->
With browser caching disabled, https://coacheey.com/no-such-page-123 displayed a 404 heading, the message "Oops! Page not found" and a "Return to Home" link, while the document request returned HTTP 200. This is a soft 404: the page communicates failure to visitors but reports success at the HTTP level, which can mislead search engines and automated link checks. The recovery link gives visitors a clear route back to the homepage. Evidence: evidence/A4-missing-page.png and evidence/A4-status-fresh.png. [A4]

## A5: Caching
<!-- Focus: Both resource URLs; exact header values, or explicitly absent; one plain-language interpretation each. Interpretation: Interpret actual directives. no-cache permits storage with revalidation; no-store prevents storage. Do not assume a missing header proves there is no caching. -->
[FILL: summarise the actual document and asset cache policies in the table]. [FILL: explain the implications for reuse/revalidation without claiming that missing Cache-Control rules out caching]. [A5]

| Resource URL/type | Exact Cache-Control (or absent) | Meaning in one sentence |
|---|---|---|
| [FILL: main document] | [FILL] | [FILL] |
| [FILL: image or script] | [FILL] | [FILL] |

## A6: Where the page is built
<!-- Focus: Text checked; whether present in source; whether present in live DOM; server-rendered/browser-rendered/mixed classification with justification. Interpretation: Base classification on this page's evidence. Script tags alone do not prove browser rendering; do not guess a framework. -->
[FILL: distinctive main text checked and its presence/absence in raw source and live Elements]. [FILL: rendering classification justified by those observations, including uncertainty where relevant]. [A6]

## A7: SEO basics
<!-- Focus: Exact values or missing; h1 count; applicability and values of sponsored/ugc. Interpretation: Judge whether metadata describes this page. If adverts/comments are absent, mark their link attributes not applicable with a reason. -->
[FILL: summarise verified metadata values/missing items and h1 count from the table]. [FILL: judge relevance to this page and explain whether sponsored/ugc attributes apply]. [A7]

| Item | Exact value / count / missing / not applicable | Judgement |
|---|---|---|
| Page title | [FILL] | [FILL] |
| Meta description | [FILL] | [FILL] |
| Canonical link | [FILL] | [FILL] |
| html lang | [FILL] | [FILL] |
| h1 count | [FILL] | [FILL] |
| rel=sponsored / rel=ugc | [FILL] | [FILL] |

# Part B: The experience

## B1: Loading state
<!-- Focus: Elapsed seconds per capture; blank/spinner/placeholders/partial content; whether visitors can understand progress. Interpretation: Describe the loading sequence and task impact, not just that the site is slow. Record cache conditions. -->
[FILL: actual throttling/cache settings and loading sequence at the captured elapsed times]. [FILL: explain whether visitors can understand progress and continue their task; state that normal networking was restored]. [B1]

## B2: Empty state
<!-- Focus: Query; exact page URL; exact no-results wording; next step offered. Interpretation: Is the state clear and helpful? If no search safely produces zero results, explain what you tried without inventing a state. -->
[FILL: public search/filter URL, exact impossible query, exact result wording and offered next step]. [FILL: explain clarity and recovery from no matches; state any limitation]. [B2]

## B3: Error state
<!-- Focus: Action attempted; exact message; retry/recovery options; whether message belongs to the browser or site. Interpretation: Does the visitor know what happened and how to recover? If caching keeps a page working, record that observed result. -->
[FILL: action attempted while Offline, exact outcome, source of message (site/browser), and recovery controls]. [FILL: explain visitor recovery or observed cached behaviour; confirm Online was restored]. [B3]

## B4: Form validation
<!-- Focus: Form URL; missing required fields; error location/exact wording; whether harmless typed input is retained. Interpretation: Judge useful feedback and recovery. Do not send messages, create accounts, book, order or pay. Do not enter personal data. -->
[FILL: form URL, deliberately omitted required inputs, exact validation message/location and whether harmless entered text was retained; otherwise state not tested safely and why]. [FILL: explain feedback usefulness and the safe-testing boundary]. [B4]

## B5: Labels
<!-- Focus: Field-by-field visible label; click-to-focus yes/no; placeholder-only yes/no. Interpretation: Explain whether users can identify each field. Include every field, not just a convenient example. -->
[FILL: summarise field-by-field visible labels, click-to-focus behaviour and placeholder-only cases from the table]. [FILL: explain how the observed behaviour affects identifying and completing fields]. [B5]

| Field | Visible label? | Clicking label focuses field? | Placeholder only? | Comment |
|---|---|---|---|---|
| [FILL: add a row for every field] | [FILL] | [FILL] | [FILL] | [FILL] |

## B6: Keyboard only
<!-- Focus: Task; starting URL; key/action log; completion; visible focus; logical order; trap; skip link. Interpretation: Describe the actual obstacle and its task impact. Do not claim full keyboard accessibility from one task. -->
[FILL: public task, starting point, success criterion, observed focus/order/skip-link/trap behaviour and completion result]. [FILL: explain task-specific keyboard impact without generalising to the entire site]. [B6]

**Task and starting URL:** [FILL.] **Outcome:** [FILL.]

**Key/action log:** [FILL: concise sequence, focus/order/traps/skip link.]

## B7: Automated accessibility audit
<!-- Focus: Exact URLs; dates/times; device mode/settings; both scores; top three flagged issues, indicating affected page(s). Interpretation: If fewer than three issues appear, say so. A 100 score does not prove full accessibility. Keep automated findings separate from manual results. -->
[FILL: both accessibility scores under the recorded comparable settings, and the actual top flagged issues with affected pages]. [FILL: explain visitor implications and limits of automated scoring]. [B7]

| Page URL | Date/time + timezone | Mode/settings | Accessibility score | Exported report |
|---|---|---|---|---|
| [FILL: homepage] | [FILL] | [FILL] | [FILL] | evidence/B7-lighthouse-home.html |
| [FILL: inner page] | [FILL] | [FILL] | [FILL] | evidence/B7-lighthouse-inner.html |

**Top flagged issues:** [FILL: up to three, identifying affected pages and visitor impact; say if fewer than three.]

## B8: Link and button text
<!-- Focus: Current visible text/icon; accessible name if any; page URL; context; proposed clearer wording. Interpretation: An icon-only control may already have an accessible name. Do not call it unnamed without checking. If fewer than five examples exist, report the actual count. -->
[FILL: summarise up to five actual wording/name issues in their page context]. [FILL: explain the proposed clearer wording and distinguish unnamed icons from icons that already have accessible names]. [B8]

| Page/context | Actual text or icon | Accessible name if relevant | Suggested wording |
|---|---|---|---|
| [FILL: add up to five observed examples] | [FILL] | [FILL] | [FILL] |

# Part C: Recommendations
## Two strengths
1. [FILL: strength, evidence IDs and benefit to visitors.]
2. [FILL: strength, evidence IDs and benefit to visitors.]

## Three priorities
**Reason for this order:** [FILL: one sentence comparing task impact, affected visitors and/or effort using evidence.]

### 1. [FILL: concise problem title]
- **Problem:** [FILL: one observed problem in one sentence.]
- **Evidence:** [FILL: A/B IDs and filenames.]
- **Who it affects:** [FILL: visitor group and task.]
- **Fix in plain words:** [FILL: practical change.]
- **Effort:** [FILL: low/medium/high; short rationale, clearly an estimate.]
- **Impact:** [FILL: low/medium/high; evidence-based rationale.]

### 2. [FILL: concise problem title]
- **Problem:** [FILL: one observed problem in one sentence.]
- **Evidence:** [FILL: A/B IDs and filenames.]
- **Who it affects:** [FILL: visitor group and task.]
- **Fix in plain words:** [FILL: practical change.]
- **Effort:** [FILL: low/medium/high; short rationale, clearly an estimate.]
- **Impact:** [FILL: low/medium/high; evidence-based rationale.]

### 3. [FILL: concise problem title]
- **Problem:** [FILL: one observed problem in one sentence.]
- **Evidence:** [FILL: A/B IDs and filenames.]
- **Who it affects:** [FILL: visitor group and task.]
- **Fix in plain words:** [FILL: practical change.]
- **Effort:** [FILL: low/medium/high; short rationale, clearly an estimate.]
- **Impact:** [FILL: low/medium/high; evidence-based rationale.]

<!-- END OF SIX-PAGE MAIN REPORT. Insert a page break before the appendix when exporting. -->
# Appendix: Evidence log
[FILL: paste the completed session details and file-by-file table from drafts/evidence-log.md. The appendix may extend beyond the six-page main-report limit.]




