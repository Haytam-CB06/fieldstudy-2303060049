# Fieldwork guide
**Focus:** use this alongside the browser. All observations and evidence must be your own.

## Safe boundaries
Browse public pages normally. Use DevTools and Lighthouse. Do not log in, probe hidden pages, run scanners/crawlers/load tests, submit real forms, enter personal data, or contact the owner. If exposed personal data or a suspected security hole appears, stop; do not investigate or take further screenshots; tell your instructor that day.

## Coacheey task ideas to verify yourself
Try finding a coach for a sport/location, reading a public profile, and locating public contact/booking information without sending anything. These are test ideas, not claims that each feature exists. Adapt them to the actual public site.

## A1: HTTPS and redirects
**Do:** Type the site's address with http://. Record the final URL and inspect the certificate through the browser's site/security information.

**Record:** Requested URL; final URL; redirect behaviour; certificate validity.

**Focus your judgement:** Separate transport security from overall site trustworthiness. Do not claim HTTPS proves the site is safe.

**Evidence:** A1-redirect.png; A1-certificate.png

## A2: URL structure
**Do:** Collect five different real page URLs. Assess every URL against HTTPS, short/readable, lowercase, hyphens rather than underscores, and few query parameters.

**Record:** Five URLs; pass/fail for each of five rules; short justification for failures.

**Focus your judgement:** Judge readability and practical meaning. Do not call all parameters wrong; explain necessary filters if observed.

**Evidence:** Five-row URL table in report; screenshots optional

## A3: One request, closely
**Do:** Open Network and reload. Select the first document request. Inspect Headers and the Network summary. Look for a Fetch/XHR request.

**Record:** Method; HTTP status; Content-Type; request count; total transferred/resource size with exact displayed label; Fetch/XHR URL/method/status if one exists.

**Focus your judgement:** Explain what the response represents. Record cache/network conditions; distinguish transferred bytes from resource size. Say if no Fetch/XHR was observed.

**Evidence:** A3-document-headers.png; A3-network-summary.png; A3-xhr.png if applicable

## A4: A missing page
**Do:** Visit one deliberately made-up path such as /no-such-page-123. Inspect its document request status. Do not probe hidden paths.

**Record:** Exact test URL; actual status code; what the visitor sees; recovery links.

**Focus your judgement:** Distinguish a true 404 from a friendly page returning 200 (soft 404). A screenshot of an error message alone cannot prove the status.

**Evidence:** A4-missing-page.png; A4-status.png

## A5: Caching
**Do:** Read Cache-Control on the main document and one image or script.

**Record:** Both resource URLs; exact header values, or explicitly absent; one plain-language interpretation each.

**Focus your judgement:** Interpret actual directives. no-cache permits storage with revalidation; no-store prevents storage. Do not assume a missing header proves there is no caching.

**Evidence:** A5-cache-document.png; A5-cache-asset.png

## A6: Where the page is built
**Do:** View raw page source with Ctrl+U. Search for distinctive visible main text, then compare the same text in Elements.

**Record:** Text checked; whether present in source; whether present in live DOM; server-rendered/browser-rendered/mixed classification with justification.

**Focus your judgement:** Base classification on this page's evidence. Script tags alone do not prove browser rendering; do not guess a framework.

**Evidence:** A6-source.png; A6-elements.png

## A7: SEO basics
**Do:** Inspect title, meta description, canonical link, html lang, all h1 elements, and sponsored/ugc links if adverts/comments exist.

**Record:** Exact values or missing; h1 count; applicability and values of sponsored/ugc.

**Focus your judgement:** Judge whether metadata describes this page. If adverts/comments are absent, mark their link attributes not applicable with a reason.

**Evidence:** A7-seo-01.png and further numbered captures

## B1: Loading state
**Do:** Set Network throttling to Slow 3G. Reload and take 2-3 screenshots seconds apart. Restore normal network afterwards.

**Record:** Elapsed seconds per capture; blank/spinner/placeholders/partial content; whether visitors can understand progress.

**Focus your judgement:** Describe the loading sequence and task impact, not just that the site is slow. Record cache conditions.

**Evidence:** B1-loading-01.png; B1-loading-02.png; optional -03

## B2: Empty state
**Do:** Search/filter for an impossible value such as zzzqqq, using an actual public search.

**Record:** Query; exact page URL; exact no-results wording; next step offered.

**Focus your judgement:** Is the state clear and helpful? If no search safely produces zero results, explain what you tried without inventing a state.

**Evidence:** B2-empty-search.png

## B3: Error state
**Do:** Set your own connection to Offline using DevTools. Try a search or another public page. Restore Online afterwards.

**Record:** Action attempted; exact message; retry/recovery options; whether message belongs to the browser or site.

**Focus your judgement:** Does the visitor know what happened and how to recover? If caching keeps a page working, record that observed result.

**Evidence:** B3-offline.png

## B4: Form validation
**Do:** Choose a form and leave required fields deliberately incomplete. Submit only if it cannot send. If it might send, stop and record not tested safely.

**Record:** Form URL; missing required fields; error location/exact wording; whether harmless typed input is retained.

**Focus your judgement:** Judge useful feedback and recovery. Do not send messages, create accounts, book, order or pay. Do not enter personal data.

**Evidence:** B4-form-validation.png or reason in log

## B5: Labels
**Do:** For every field of the B4 form, check visible label and click its text to see whether the field receives focus.

**Record:** Field-by-field visible label; click-to-focus yes/no; placeholder-only yes/no.

**Focus your judgement:** Explain whether users can identify each field. Include every field, not just a convenient example.

**Evidence:** B5-labels.png plus field table

## B6: Keyboard only
**Do:** Choose one real task possible with Tab, Shift+Tab and Enter. Put the mouse aside and complete it, checking skip link, focus, order and traps.

**Record:** Task; starting URL; key/action log; completion; visible focus; logical order; trap; skip link.

**Focus your judgement:** Describe the actual obstacle and its task impact. Do not claim full keyboard accessibility from one task.

**Evidence:** B6-keyboard-focus.png plus short key log

## B7: Automated accessibility audit
**Do:** Run Lighthouse Accessibility separately on the home page and one public inner page. Export both reports.

**Record:** Exact URLs; dates/times; device mode/settings; both scores; top three flagged issues, indicating affected page(s).

**Focus your judgement:** If fewer than three issues appear, say so. A 100 score does not prove full accessibility. Keep automated findings separate from manual results.

**Evidence:** B7-lighthouse-home.html; B7-lighthouse-inner.html; score screenshots optional

## B8: Link and button text
**Do:** Find up to five real vague links/buttons or icon-only controls. Inspect accessible naming where relevant.

**Record:** Current visible text/icon; accessible name if any; page URL; context; proposed clearer wording.

**Focus your judgement:** An icon-only control may already have an accessible name. Do not call it unnamed without checking. If fewer than five examples exist, report the actual count.

**Evidence:** B8-link-button-01.png etc.

