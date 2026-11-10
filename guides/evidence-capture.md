# Evidence capture guide
**Focus:** collect original proof for your own observations. Do not add empty PNG files or generated screenshots.

## Capture rules
- Every screenshot must show the website address; include the relevant DevTools panel when needed.
- Record actual date/time, timezone, URL and browser in the evidence log. Ensure the capture date/time is also visible on screenshots as required by the assignment FAQ, e.g. include the system clock/date without hiding the URL.
- Preserve originals. Do not alter a screenshot to change what it appears to show.
- Use separate captures when page content and technical details cannot both be read.
- Do not capture personal data, passwords or exposed security information. If found, stop and tell the instructor that day.
- Use IDs in filenames and report references. Multiple evidence files may share one checklist ID with numbered suffixes.

## Capture checklist
| ID | Suggested files | What the evidence must establish |
|---|---|---|
| A1 | A1-redirect.png; A1-certificate.png | Final HTTPS address and certificate validity |
| A2 | A2-url-table in the report | Five actual URLs assessed against all five rules; extra screenshots optional |
| A3 | A3-document-headers.png; A3-network-summary.png; A3-xhr.png if present | Method/status/type; requests/total size; one Fetch/XHR if observed |
| A4 | A4-missing-page.png; A4-status.png | Visitor-facing result and actual HTTP status |
| A5 | A5-cache-document.png; A5-cache-asset.png | Cache-Control for main document and one image/script |
| A6 | A6-source.png; A6-elements.png | Same main text in source versus live page elements |
| A7 | A7-seo.png or multiple numbered captures | Title, description, canonical, lang, h1 count, relevant link attributes |
| B1 | B1-loading-01.png; B1-loading-02.png; optional -03 | Slow 3G loading states seconds apart; record elapsed time |
| B2 | B2-empty-search.png | No-results state and its exact wording |
| B3 | B3-offline.png | What happens offline; distinguish browser error from site message |
| B4 | B4-form-validation.png | Safely triggered errors, or log why not safely tested |
| B5 | B5-labels.png | Visible labels; click behaviour recorded for every field |
| B6 | B6-keyboard-focus.png | Visible keyboard focus; task/order/traps recorded in report |
| B7 | B7-lighthouse-home.html; B7-lighthouse-inner.html | Two exported Lighthouse accessibility reports and scores |
| B8 | B8-link-button-01.png etc. | Up to five actual vague links/buttons or unnamed icons |

Keep exported Lighthouse HTML alongside screenshots of both scores where useful. It is evidence, not the report.

