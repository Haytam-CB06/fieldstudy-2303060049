# Audit methodology

This document describes the intended method. It is not a claim that the checks have already been performed. Record actual execution and deviations in the report and evidence log.

## Scope and visitor task

Use publicly reachable pages and realistic tasks established by inspecting the site. Identify the home page, an inner page, the form/search used for B4–B5, and a keyboard task with a defined starting point and success criterion. Record exact URLs; do not infer account-only behaviour from public pages.

## Reproducible observations

- Start in a fresh browser window and record browser/version, device, viewport, date, time and timezone.
- Record relevant network and cache conditions. Use normal conditions for baseline checks, Slow 3G for B1 and Offline for B3; restore normal conditions afterwards.
- Keep Lighthouse mode and settings comparable between pages and sites. Preserve both exports.
- Copy exact HTTP headers, status codes, visible error messages and relevant control names. Interpret values separately from recording them.
- State the page and action tested. Avoid statements such as “the entire site is inaccessible” based on one page or task.
- If a result seems inconsistent, repeat the same safe action once and record the difference rather than selecting the preferred result.

## Evidence and traceability

Use the chain: **observation → evidence ID/file → visitor consequence → recommendation → verification criterion**.

Screenshots must be original and include the site address and relevant DevTools. Record timestamps and exact page URLs in the evidence log; include date/time in the captures as required by the assignment FAQ. Preserve original captures. Use one row per file, including Lighthouse reports, and multiple files where one cannot legibly show the page and technical detail.

An evidence reference identifies what was observed; it does not by itself justify an interpretation. For example, the page message establishes what the visitor sees, while the Network status establishes whether it is a true or soft 404.

## Finding structure

For each A/B check, write a short paragraph containing:

1. **Observation:** precise behaviour or values from the audited page.
2. **Interpretation:** technical meaning supported by those values.
3. **Visitor implication:** who or which task is affected, if relevant.
4. **Boundary:** any condition or testing limitation that materially changes the conclusion.
5. **Reference:** the checklist ID, with matching files in the log.

Use tables only when they improve comparison or are requested. Keep the report within six main pages; keep detailed procedures in working notes.

## Selecting the three recommendations

Prioritise a demonstrated task blocker over a cosmetic preference where the evidence supports that distinction. Consider affected tasks, severity, recovery and breadth of exposure. Explain the final order in one sentence instead of inventing a numerical precision unsupported by the study.

| Estimate | Effort interpretation | Impact interpretation |
|---|---|---|
| Low | Local wording, markup or configuration change with limited integration work | Removes a minor inconvenience on a limited task |
| Medium | Component/state changes plus integration and regression checking | Meaningfully improves an important task or removes a recurring obstacle |
| High | Broader architectural or multi-page changes requiring coordinated work | Restores a blocked essential task or addresses substantial exclusion supported by evidence |

These are working definitions, not measured engineering estimates. Unknown access to the production code limits confidence in effort. Describe expected impact qualitatively; do not invent conversion, revenue or user-population figures.

For every selected recommendation, define a simple verification action and expected observable outcome. Carry the same priorities into the owner summary and select the Challenge issue from actual findings.

## Benchmark and volunteer evidence

Compare the same six checks on two genuinely comparable sites. Note differences in pages, task scope, network conditions or settings that limit the comparison. Do not assume the second site is better in every respect.

For the volunteer study, define three tasks and success criteria before starting. Use a consistent timing rule, observe without coaching, and record quotations verbatim. Explain whether the session supports or contradicts at least one Core finding. One participant supplies a case observation, not a representative user study.

## Challenge verification

Choose one documented issue and implement an original standalone React/Vite or Next.js fix. Compare the same task or criterion before and after where possible. Distinguish the original production site from the local demonstration; their hosting, content and architecture differ. Use state screenshots or task results when those directly establish the improvement. Explain one design decision and verify the actual installation/run instructions.

## Known limitations to resolve

- Findings have not yet been collected; templates are not evidence.
- The assignment's site-claim deadline differs between Section 2 and the timeline.
- The course-only report rule and logged-out repository access instruction need instructor-approved handling.
- Four commits across three days require genuine work on three dates; same-day preparation cannot create that history.
- AI assistance is limited by the assignment's integrity rules and must be disclosed accurately.
