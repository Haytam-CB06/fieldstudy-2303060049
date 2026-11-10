# Coacheey website field study

AI-assisted review draft; verify and revise before submission.

## A1 - HTTPS and certificate
The supplied redirect and certificate captures support an HTTP entry ending on HTTPS and a valid certificate in Chrome. HTTPS protects the connection; it does not establish that every part of the service is trustworthy. The redirect chain and certificate validity dates were not transcribed, and some address bars hide the scheme. [A1]

## A2 - URL structure
Five captured paths are assessed below. All use lowercase and have no underscores. Four have no query parameters; the coaches URL has two useful filters but long UUID values. HTTPS is explicit for Events in the Lighthouse result; the full schemes of the other four captured addresses need confirmation. No authentication attempt is part of this assessment. [A2]

## A3 - Document and data requests
The homepage document request is GET https://coacheey.com/, returning 200 OK with Content-Type text/html; charset=utf-8. One overview capture shows 131 requests, 337 kB transferred and 7.2 MB resources, with No throttling and browser caching enabled. These are one-session totals, not a repeatable cold-load benchmark: cached resources explain part of the difference between transferred bytes and resource size. A separate Fetch/XHR capture shows a GET to public_coach_profiles returning 200, supporting browser-side retrieval of coach data; its full query is not transcribed here. [A3]

## A4 - Missing-page response
The made-up path /no-such-page-123 displays "404", "Oops! Page not found" and "Return to Home", but its fresh document response is 200 with Disable cache checked. This is a soft 404: visitors see a missing-page message while software receives a success status. The recovery link is helpful, but the HTTP status should agree with the page. The separate cached 304 capture is supporting context, not the fresh-response result. [A4]

## A5 - Cache policies
The main document has Cache-Control: no-cache. It may be stored but must be revalidated before reuse. The inspected JavaScript asset has Cache-Control: public, max-age=31536000, immutable, allowing shared/browser caching for one year without routine freshness revalidation while fresh. This can reduce repeat transfers; changed long-lived assets should use a new URL. The asset header is visible, but its complete request URL was not captured in the supplied header view. [A5]

## A6 - Initial HTML and live content
The raw source includes "Find Your Perfect Coach in Luxembourg", descriptive text and links. The live Elements capture instead shows the hero heading "Find Your Perfect Coach" with different surrounding markup. This supports a mixed delivery model: substantive initial HTML plus browser-side modification. It does not distinguish runtime server rendering from static prerendering, and script filenames alone do not establish the rendering method. [A6]

## A7 - SEO basics
The source includes a descriptive title and description, a homepage canonical URL and lang=en. The live heading search shows one h1. A source/live title difference is recorded without assuming its cause. No anchors matching sponsored or ugc were found in the inspected DOM; that absence alone is not a defect, because the applicability and type of advertising or user content need checking. [A7]

## B1 - Loading feedback
With the actual Chrome preset labelled 3G and Disable cache unchecked, the MEC Movement profile first shows image, avatar and text skeletons, then populated coach information. The student confirmed both MEC screenshots came from one reload. The document returned 304, indicating cache revalidation. The placeholders give visible structure while content arrives. Elapsed capture times were not recorded, so this is qualitative sequence evidence, not a timed Slow 3G or cold-load speed measurement. [B1]

## B2 - Empty results
On Events, searching zzzqqq returns "0 events found", "No events found" and "Try adjusting your search criteria or location filter." This identifies the empty state and suggests recovery. However, the same capture retains "$62 avg", "Most popular: Fitness" and "4 top-rated". Their scope is unclear when zero events match, so these statistics could confuse visitors; no calculation error is claimed. [B2]

## B3 - Offline reload
Reloading Events with Network set to Offline produces Chrome's dinosaur page and ERR_INTERNET_DISCONNECTED, with failed/cancelled document requests. The advice belongs to the browser, not Coacheey; no site-specific retry control is visible. This establishes full-page offline behaviour only, not how an already loaded search handles a lost connection. Later site/Lighthouse captures show online activity resumed, although the exact restoration step was not recorded. [B3]

## B4 - Safe validation limitation
The student reported no public contact section was found. No suitable public form was identified for deliberately incomplete submission testing. Login, registration and booking actions were avoided. Result: not tested safely; no claim is made about validation errors or input retention. This is an incomplete check, not evidence that the site has no forms. [B4]

## B5 - Labels and accessible names
The Events search box has no separate visible label; Chrome derives its name "Search sessions..." from the placeholder. Location, sport and language expose role combobox but have empty computed Name fields and no associated label specified. Values such as "All locations" and "Pilates" do not substitute for a stable name identifying purpose. The language detail is cropped and relies on the student's inspection context. The header globe is separately named "Change language". Sort and label click-to-focus remain unverified; no complete field-by-field pass is claimed. [B5]

## B6 - Keyboard task
The student reached Events using Tab and Enter with visible focus, reported the header order logo, Home, Events, Become Coach, and encountered no trap. No skip link appeared in this attempt. Tab skipped the sport icons beneath "What are you looking for?", while clicking Yoga with the mouse opened results. This supports a keyboard-accessibility obstacle for those discovery shortcuts in the tested state, despite successful header navigation. DOM semantics and alternative routes were not inspected; no site-wide pass or failure is claimed. [B6]

## B7 - Lighthouse Accessibility
The homepage scored 94 and Events scored 93. Both student-exported HTML reports confirm Accessibility-only desktop formFactor with screen emulation disabled. The homepage audit ran at 2026-11-09 11:15:54.972 UTC; the Events export ran at 11:42:54.478 UTC that day, a separate run from its earlier screenshot. Exported results flag insufficient colour contrast and a missing main landmark on both pages, plus non-sequential heading order on Events. These can affect reading and navigation. Automated scores cover only a subset of accessibility and do not override the manual label findings. [B7]

## B8 - Control wording
An Events card uses "Read more", which is less specific than the event title; a contextual label such as "Read about this Pilates event" would identify its destination more clearly. The location and sport selectors also need stable accessible names such as "Filter by location" and "Filter by sport" while keeping their current values. These are three supported examples; other icons were not classified as unnamed without inspection. [B8; B5]

## Two strengths
1. Useful recovery from no matches. Events explains that no events were found and suggests adjusting the search, helping visitors recover rather than leaving a blank area. [B2]2. Visible loading structure. Coach-profile skeletons show where images and details will appear, giving visitors feedback while content arrives. This is a usability strength, not a verified loading-speed claim. [B1]

## 1 - Give search filters stable names
Problem: the inspected location and sport comboboxes have empty computed names. Evidence: B5-location-accessibility.png and B5-sport-accessibility.png. Affected visitors: people using assistive technology to find suitable sessions. Fix: add persistent visible labels connected to the controls, preserving selected values; review language and sorting too. Effort: low (estimate: local labelling changes). Impact: high (estimate: essential search controls become easier to identify). Verify through the accessibility tree and manual keyboard/screen-reader use. [B5]

## 2 - Improve text contrast
Problem: Lighthouse flags insufficient foreground/background contrast on both inspected pages. Evidence: B7-lighthouse-home.html and B7-lighthouse-inner.png. Affected visitors: people with low vision and visitors viewing the site in glare. Fix: inspect the flagged elements and adjust shared text/background colours while preserving focus visibility. Effort: medium (estimate: shared styles need checking across states). Impact: high (estimate: reading is fundamental across pages). Rerun both audits and inspect the affected text manually; scores alone are not the acceptance criterion. [B7]

## 3 - Return the correct missing-page status
Problem: an invented page displays a missing-page message but returns HTTP 200. Evidence: A4-status-fresh.png. Affected visitors: people following broken links, and services checking or indexing those links. Fix: keep the friendly message and home link but return HTTP 404 for nonexistent routes. Effort: medium (estimate: hosting/routing configuration needs verification). Impact: medium (estimate: improves broken-link detection and indexing signals). Revisit the same invented URL with caching disabled and confirm 404 in Network. [A4]
