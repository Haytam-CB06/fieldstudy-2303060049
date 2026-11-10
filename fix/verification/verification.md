# AI-run local-demo verification

These are not student-taken website observations or screenshots.

Verified at: 2026-11-10T00:22:11.455Z
Browser: Chrome 156.0.8078.80
URL: http://127.0.0.1:5174/#main

| Check | Result |
|---|---|
| Accessible filter names | PASS |
| Label focuses session-query | PASS |
| Label focuses session-location | PASS |
| Label focuses session-sport | PASS |
| Label focuses session-language | PASS |
| First Tab reaches visible skip link | PASS |
| Skip link moves to main | PASS |
| Yoga reached by Tab | PASS |
| Yoga focus visible | PASS |
| Enter applies Yoga shortcut | PASS |
| Search preserves filters | PASS |
| Recovery clears filters | PASS |
| Impossible query empty state | PASS |
| Mobile layout does not overflow | PASS |
| No runtime page errors | PASS |

## Before and after

| Behaviour | Student baseline | AI-verified local demo |
|---|---|---|
| Names for the three filters | Location, sport and language computed Name empty in B5; language screenshot is cropped | Three named comboboxes: Location, Sport, Session language |
| Label association | No associated labels specified in original inspected controls | All four demo label clicks focused their associated fields |
| Sport shortcut | B6: student reports Tab skipped shortcuts, mouse Yoga opened results | Tab reached Yoga; Enter applied it and returned two invented Yoga examples |
| Empty-state recovery | B2 already provides useful recovery advice | Impossible query produced a clear empty state; Show all sessions restored four invented examples |

Do not interpret local-demo results as an isolated measurement of a production patch or as full accessibility certification.

## Captures

- after-labelled-controls.png: desktop labels and controls.
- after-keyboard-yoga.png: Yoga selected after Tab and Enter; two results.
- after-empty-state.png: Yoga and French retained with no matches and recovery.
- after-mobile.png: 390 CSS px width, all examples restored.

All after screenshots were captured by AI on localhost. Original baseline screenshots remain in the parent evidence folder.

## Verification conditions

Desktop viewport 1280 x 1050; mobile 390 x 844. The harness starts a new navigation before checking the first Tab. A prior reload-based attempt retained Chrome focus from a previous field; resetting navigation corrected the test setup. No passing result is fabricated from that failed harness attempt.

Production build passed: npm run build; Vite 8.3.7, React/React DOM 19.3.1, Node 22.17.0.

See verification-results.json for detailed actual observations.