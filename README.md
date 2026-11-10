# Coacheey website field study

**Student:** Haytam CHARAFI | **Number:** 2303060049  
**Course:** SFWE475 / CPRG201 | **Website:** https://coacheey.com/  
**Organisation/brand:** Coacheey | **Prepared:** 10 November 2026

Status: AI-assisted review package prepared for student review. Evidence gaps and authorship restrictions remain; no full-mark or submission-ready claim is made.

## Purpose and scope

The study examines public coach discovery and group-event browsing: HTTP delivery, URL structure, caching, initial HTML, metadata, search states, labels, keyboard access and automated accessibility checks. No account access, actual booking, payment or message submission is included.

The student's genuine-use basis, LMS site claim and exact course deadline/access arrangements still need confirmation. The fieldwork browser version and most screenshot capture times were not recorded; those values have not been invented.

## Deliverables

| Path | Contents and status |
|---|---|
| `report.pdf` | Core A-C: six main pages with selected screenshots, plus evidence-log appendix. Contains explicit incomplete checks. |
| `owner-summary.pdf` | One-page owner-facing summary of two strengths and three priorities. |
| `evidence/` | Student-supplied website screenshots and original Lighthouse HTML exports, including the benchmark. |
| `stretch/benchmark.pdf` | Six-check comparison with Eversports: A1, A4, A6, A7, B6 and B7; includes limitations and three lessons. |
| `stretch/usability-test.pdf` | Partial one-participant record. Task timings and observation procedure were not documented; chronology needs confirmation. |
| `fix/` | Original React/Vite discovery demo; AI-assisted implementation and verification. Student review and course-policy confirmation required. |
| `fix/verification/` | Clearly labelled AI-run local-demo checks and after screenshots; not student fieldwork evidence. |
| `drafts/` | Original templates, review text and student-reported notes. `*-review.md` files are AI-assisted review drafts. |
| `guides/` | Working procedures and remaining-review checklist. Earlier template guides may describe work subsequently completed. |

The screenshot dates are distinct from Lighthouse audit timestamps. Coacheey Lighthouse scores are 94 (home) and 93 (Events); Eversports home scored 100 but its export still includes a label/name mismatch audit. No score establishes full accessibility.

## Challenge: run locally

```sh
cd fix
npm ci
npm run dev
```

Open the printed localhost URL. See `fix/README.md` for the original problem/evidence, design decision, before/after comparison, verification and production build commands. No site code, text, photos or actual session data was copied.

## Remaining review

1. Review/revise the AI-generated wording against your own observations, and confirm the permitted scope of assistance with the instructor.
2. Confirm original dates/times, browser/version, exact URLs and any missing measurements from genuine records. Unknown values must stay unknown if not recorded.
3. Core limitations include unrecorded loading capture intervals, no safe validation test, unverified sort/label-click behaviour, and incomplete request-resource URL transcription.
4. Confirm whether the volunteer task outcomes came from 6 November or a later follow-up. A retrospective ten-minute browsing session is not a complete timed S2 test.
5. Inspect and understand the Challenge code; perform your own manual checks and capture your own after evidence if required.
6. Git requires four meaningful commits over three genuine days. All newly created commits use real dates; three-day history cannot be fabricated or recovered retrospectively.
7. Submit the repository link only after verifying the files on `main` and instructor-approved access. The assignment prohibits public sharing of the report but also asks for logged-out repository access; clarify that conflict before uploading reports to a public repository. No owner contact is authorised.

## AI assistance disclosure

AI assisted repository organisation, templates, procedural guidance, interpretation of student-supplied evidence, drafting/editing the review text, PDF layout, and the Challenge implementation and local verification. The generated wording and code are not unaided student work. The student must verify, understand and revise them, and use only assistance permitted by the instructor.

Live-site screenshots in `evidence/` were supplied by the student. Earlier AI-captured A2 reference material was kept outside this repository and is excluded from the student's evidence. Local Challenge screenshots in `fix/verification/` were captured by AI and are labelled accordingly. No uncollected timings, participant quotes, observations or historical commits have been invented.
