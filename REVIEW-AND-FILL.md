# Remaining student review and missing information

The Core report, owner summary, six-check benchmark and Challenge demo are prepared. The volunteer-test document records the feedback actually supplied. **The assignment is not verified as fully complete, and no grade can be promised.**

The PDFs have no blank answer placeholders. Unknown items are written as **not recorded**, **unverified** or **not tested safely**. This checklist is the only place with fill-in prompts. Keep those statements if you cannot provide real evidence.

## Step 1 - Confirm eligibility and the study details

The purpose is already filled: Coacheey helps people find coaches and book training sessions, with public group-event listings.

- **Genuine use:** the assignment asks for a site you or people you know actually use. Who uses it, and for what real purpose? **[YOUR ANSWER]**
- **LMS claim:** have you claimed this domain, and was it accepted? **[YOUR ANSWER]**
- **Original audit records:** give the actual session dates/times and timezone if you recorded them. Most screenshot capture times are still unknown. **[YOUR ANSWER, or not recorded]**
- **Browser:** original Lighthouse exports establish Chrome 156 on 64-bit Windows for those runs. Supply any separately recorded browser/version for the other sessions; otherwise leave it unknown. **[YOUR ANSWER, or not recorded]**

Do not use file modification times, PDF preparation dates or Lighthouse fetchTime as screenshot capture times. The three original HTML audit times are already recorded in review/evidence-log.csv.

## Step 2 - Close the remaining Core gaps where possible

| Item | What you still need to do | Where the result belongs |
|---|---|---|
| A2 | Copy the full five addresses, including the scheme, from your own browser/records. Only Events has separate HTTPS proof in the current table. | review/report.md A2 and review/evidence-log.csv |
| B1 | Capture a new loading sequence under Slow 3G if available. Record the actual preset, cache setting, date/time and elapsed times for 2-3 screenshots from the same reload. Current images are untimed and use 3G with cache enabled. | evidence/; report B1; evidence log |
| B4 | Keep **not tested safely** unless you identify a form where an incomplete submission cannot send anything. Do not use account creation, booking, payment or messaging to fill this gap. | report B4; optional safe evidence only |
| B5 | Inspect the sort control itself in DevTools Accessibility. Record its computed Name and Role; do not inspect a menu option or header globe instead. | report B5; evidence log if adding a screenshot |
| Evidence | Fill original dates/times only where you actually recorded them. Some supporting crops lack the address bar; a student-taken full-window replacement would meet the evidence rule better. | review/evidence-log.csv and evidence/ |

For B1, a new test is a new observation, not a way to give the old screenshots invented timings. Restore the normal network setting when finished. For B4, an honest safety limitation is preferable to an unsafe submission.

Optional traceability improvements, if already available: the complete A3 Fetch/XHR request URL and the A5 script URL. The required request/header values are already documented, so do not spend time collecting extra screenshots solely for these optional details.

## Step 3 - Complete the volunteer record, or keep it partial

Already filled: non-computing friend; laptop; reported date 6 November 2026; about ten minutes; Kirchberg/EUR15; MEC Movement with Yoga/Pilates and 0 displayed reviews; empty-search recovery; positive feedback; no changes suggested. Your latest clarification that he found no problem is included.

The following are still unknown; a positive overall opinion does not answer them:

- Did all three tasks happen on 6 November? **[YOUR ANSWER]**
- Did he think aloud while you watched without helping? **[YOUR ANSWER]**
- Individual task times and hesitations: **not recorded**. Do not estimate them retrospectively.

To complete S2, repeat a short observed session with the same or another non-computing volunteer. Give the tasks below without coaching. Ask the person to say what they are thinking. Time each task and write down any hesitation and actual words. Use the real date of this repeat session.

| Task | Completion and measured time | Hesitation/actions | Exact words |
|---|---|---|---|
| Find a Pilates event and report its location and price | [YOUR OBSERVATION] | [YOUR OBSERVATION] | [ACTUAL WORDS] |
| Find a coach and report their sports and review information | [YOUR OBSERVATION] | [YOUR OBSERVATION] | [ACTUAL WORDS] |
| Search zzzqqq, then return to the event list | [YOUR OBSERVATION] | [YOUR OBSERVATION] | [ACTUAL WORDS] |

Ask and record exactly: **What was the most frustrating moment?** and **What would you change first?** Write “none” if that is genuinely their response. Replace the partial record in review/usability-test.md only with the real new results. Do not mix dates or present the earlier feedback as a timed session.

## Step 4 - Review the writing and Challenge yourself

- Read review/report.md, review/owner-summary.md, review/benchmark.md and review/usability-test.md. Confirm the facts and revise the language so you understand and can explain every statement.
- The code and local Challenge verification were prepared by AI. The assignment permits help with concepts and English, and requires your own evidence and wording. Disclosure alone does not confirm that this amount of help is permitted. Check the instructor's rules before submitting it as your work.
- Run the demo: in fix/, use npm ci if dependencies are missing, then npm run dev. Follow the six manual steps in fix/README.md. Record your own results separately from the 15 AI-run checks already supplied.
- Your own demo review result: **[YOUR ACTUAL RESULT]**. If required, put your own after screenshots in fix/verification/student/ with real dates and the local URL.

## Step 5 - Update PDFs and submit

Editable sources map directly to outputs:

| Editable file | Exported file |
|---|---|
| review/report.md | report.pdf |
| review/owner-summary.md | owner-summary.pdf |
| review/benchmark.md | stretch/benchmark.pdf |
| review/usability-test.md | stretch/usability-test.pdf |
| review/evidence-log.csv | Appendix in report.pdf |

After updating sources, regenerate with python tools/export-pdfs.py. If needed, install the dependencies using python -m pip install -r tools/requirements.txt. Keep the six main-page limit and the one-page owner summary. Review the PDFs after export; do not submit stale versions.

- **Git history:** the reviewed package is committed locally and merged into main. All local work commits are on 10 November. The required three genuine work days are not met. Keep the real dates and ask the instructor how this will be assessed; it cannot be repaired by backdating.
- **Repository access:** reports must stay within the course, while the instructions also ask for a logged-out repository check. Confirm the instructor-approved access arrangement before uploading reports publicly.
- **Final delivery:** after making your own review changes, commit them on assignment/field-study and merge to main. Then push the approved package, check access, and submit the repository link on LMS. The assistant has not pushed or submitted it.
- **Deadline:** you previously stated 10 November 2026 at 14:00. Verify the actual LMS deadline and timezone.

This file is a working checklist, not evidence of completed tests. You may keep it out of the submitted package after resolving the actions; retain honest limitations in the report where gaps remain.
