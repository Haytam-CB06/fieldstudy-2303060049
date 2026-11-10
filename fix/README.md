# Accessible discovery - Challenge demonstration

An original, standalone React/Vite demonstration of clearly named discovery filters and keyboard-operable sport shortcuts. It uses invented classes, places and text. It makes no requests to Coacheey or Eversports and performs no bookings, authentication or submissions to an external service.

## Problem and baseline

- **B5:** Coacheey's location, sport and language combobox inspections have empty computed accessible names. The visible values are not stable field names. See `../evidence/B5-location-accessibility.png`, `B5-sport-accessibility.png` and `B5-language-accessibility-detail.png` (last is a contextual crop).
- **B6:** the student reported that Tab skipped the homepage sport shortcuts, while a mouse click on Yoga opened results. This is a task observation, not a DOM or whole-site conformance audit. See `../drafts/B6-keyboard-notes.md`.

The improvement focuses on the same discovery task: identify each filter, choose a sport with the keyboard, then read matching results.

## Run locally

Prerequisite: a Node.js version supported by the installed Vite version (development used Node 22.17.0). Exact package versions are pinned in `package.json` and `package-lock.json`.

```sh
npm ci
npm run dev
```

Open the localhost URL printed in the terminal. For a production build:

```sh
npm run build
npm run preview
```

The development and preview servers bind to `127.0.0.1`. Do not expose or deploy the demo as the actual service.

## One design decision

Use native `select` elements and explicit `label`/`htmlFor` associations rather than custom comboboxes. This gives every filter a persistent name and familiar platform keyboard behaviour with less interaction code. The trade-off is reduced visual control over the opened options. Sport shortcuts are native buttons, with `aria-pressed` reflecting the applied sport. A visible focus outline and a skip link help keyboard navigation.

Form values are applied on search and remain selected. Results use a polite status message; an impossible query leads to an explanatory empty state and a button to restore all examples. No form validation claim is made: all search fields are optional.

## Before and after

| Check | Original evidence | Demo acceptance criterion |
|---|---|---|
| Location name | Empty computed Name in B5 location capture | Native select's computed name is Location |
| Sport name | Empty computed Name in B5 sport capture | Native select's computed name is Sport |
| Language name | Empty computed Name in cropped B5 language detail | Native select's computed name is Session language |
| Label association | Original inspected controls lack specified associated label | Clicking each demo label focuses its field |
| Sport shortcut | Student reports Yoga skipped by Tab, mouse opens results | Tab reaches Yoga; Enter filters results; focus remains visible |
| Empty query recovery | Coacheey B2 already has explanatory guidance | Demo returns zero results for zzzqqq; Show all sessions restores four |

Original-site observations and local-demo verification have different provenance. AI-run local screenshots/measurements belong in `verification/`, not in the student's original website screenshot evidence. They must not be presented as student-taken captures. A separate verification record states actual checks and results; acceptance criteria above are not proof that a check passed.

This is a small standalone demo, not a production patch. A different whole-page Lighthouse score would not isolate the effect of labels, so no score-based improvement is claimed.

## Manual review to perform yourself

1. Tab from the address bar: the skip link should appear. Activate it to move to main content.
2. Click each visible field label and confirm the matching input/select receives focus.
3. Use Tab to reach Yoga, press Enter and confirm two Yoga examples.
4. Select French and Yoga, then Find sessions: zero examples match. Confirm the selected values remain.
5. Choose Show all sessions: four examples return, with all filters reset.
6. In DevTools Accessibility, confirm the three combobox names and values separately.

Record actual outcomes and capture your own after screenshots if the instructor requires student-created Challenge evidence.

## Authorship and assistance

This implementation and its initial verification were prepared with AI assistance from the student's supplied B5 evidence and B6 observations. It is original demonstration code, not copied from either audited website. The student must inspect, understand and revise it, disclose assistance, and confirm with the instructor that this degree of assistance is permitted for the Challenge. It must not be claimed as unaided student code.

Documentation consulted: [React createRoot](https://react.dev/reference/react-dom/client/createRoot), [Vite guide](https://vite.dev/guide/), [MDN label element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label).


## Verified results

The production build and all 15 local browser checks passed. See [verification record](verification/verification.md) and [machine-readable results](verification/verification-results.json). These checks were run by AI, not by the student.

![AI-captured after view of labelled controls](verification/after-labelled-controls.png)
