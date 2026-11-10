# S1 - Coacheey and Eversports

Haytam CHARAFI | 2303060049 | Prepared 10 November 2026

## Why this is a useful comparison

Both services help visitors discover sports activities, and Eversports has public fitness listings for Luxembourg. Eversports is more studio/class-focused and operates at a different scale, so this is a comparison of specific public-page behaviours rather than equivalent businesses. A1 used its Luxembourg listing; A6, A7, B6 and B7 used its homepage. A4 used the same invented path as the Coacheey check.

## Conditions and evidence

The screenshots, exports and keyboard results were supplied by the student; AI assisted analysis and drafting. Both Lighthouse exports identify Chrome 156 on 64-bit Windows, desktop formFactor and disabled screen emulation. The runs were separate and their exact viewports were not controlled. Eversports' audit time is 2026-11-09 22:25:01.133 UTC, or 10 November at 00:25:01 in Europe/Bucharest. Its missing-page capture uses 3G with caching disabled. Other capture times and the full browser builds were not recorded.

<!-- widths: 62,151,151,151.28 -->
| Check | Coacheey | Eversports | Interpretation |
|---|---|---|---|
| A1 - HTTPS | HTTP-to-HTTPS destination reported; certificate valid. A1-redirect.png and A1-certificate.png. | Same redirect reported; secure connection and valid certificate shown on the Luxembourg listing. S1-A1-eversports-certificate.png. | Both support encrypted entry in these observations. Neither certificate establishes that the entire service is secure. |
| A4 - Missing page | A friendly 404 message and home link, but a fresh HTTP 200 response. A4-status-fresh.png. | GET https://www.eversports.fr/no-such-page-123 returns 404; Chrome shows its missing-page screen and Reload. S1-A4-eversports-status.png and missing-page.png. | Eversports gets the protocol status right; Coacheey gives clearer on-page recovery. Coacheey should combine both strengths. |
| A6 - Rendering | Main text is present in source; source/live hero wording differs. A6-source.png and A6-elements.png. | Main heading and paragraph are in source; the live h1 matches. S1-A6-eversports-source.png and elements.png. | Neither starts as a content-free shell. Coacheey shows browser modification; the captures do not distinguish runtime server rendering from static prerendering. |

<!-- note -->
All listed evidence is in evidence/. The main report's appendix gives file-by-file page addresses and recorded times. Shorthand paired names share the same prefix.

<!-- pagebreak -->

# S1 - Accessibility and discovery

<!-- widths: 62,151,151,151.28 -->
| Check | Coacheey | Eversports | Interpretation |
|---|---|---|---|
| A7 - Metadata | Service/location title and description, homepage canonical, lang=en and one captured live h1. A7-source-metadata.png and A7-h1-count.png. | Title: Eversports - France - Your click to sport. Description explains France-wide activity discovery. Reported canonical: https://www.eversports.fr; lang=en; eight h1 matches. S1-A7 description/title evidence. | Both descriptions fit their respective pages. Eversports' canonical/lang/count are student-reported rather than captured. Multiple h1 elements alone are not enough to diagnose a hierarchy problem. sponsored/ugc relevance was not checked there. |
| B6 - Keyboard | Header navigation succeeds with visible focus and no trap; sport shortcuts are skipped by Tab, while mouse Yoga opens results. Recorded Core B6 task. | Yoga is reachable with Tab; focus is visible; Enter opens results; no trap encountered. Recorded benchmark task. | Eversports makes that sport-discovery shortcut available to keyboard users. This one task is not a full keyboard audit of either site. |
| B7 - Lighthouse | Homepage 94; Events 93. Contrast and main-landmark flags on both, plus heading order on Events. Original B7 HTML exports. | Homepage 100. Original S1-B7-eversports-home.html still records a visible-label/accessibility-name mismatch and an IndexedDB warning. | The stronger score is useful context, not proof of full accessibility or a controlled improvement measurement. The stored-data warning concerns loading performance; no performance comparison is made. |

## Three lessons for Coacheey

1. Keep the helpful recovery screen but return HTTP 404 for nonexistent addresses, matching the accurate status observed on Eversports.

2. Make sport shortcuts reachable and operable with Tab and Enter, as Yoga was in the Eversports task.

3. Address Coacheey's own contrast and landmark flags, using the benchmark as a comparison rather than treating a score of 100 as an accessibility certificate.

## Limits

Six checklist items have recorded observations, but some page metadata, timestamps and viewport conditions remain unverified. Eversports does not outperform Coacheey in every respect: its missing-page screen offers less useful recovery. The comparison therefore supports specific changes, not a general ranking of the two services.
