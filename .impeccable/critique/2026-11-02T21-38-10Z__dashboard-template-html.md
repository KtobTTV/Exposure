---
target: dashboard_template.html
total_score: 24
max_score: 40
na_heuristics: 
p0_count: 1
p1_count: 3
target_identity: "file:C:\\Users\\Kctob\\OneDrive\\Documents\\Sports Models\\NFL\\sleeper_lineup_bot\\dashboard_template.html"
target_fingerprint: "sha256:aba0a17901933d7ff377dacac4f1cb2ad49ddb7196e1c6fe154a075ffa5bb926"
target_path: "C:\\Users\\Kctob\\OneDrive\\Documents\\Sports Models\\NFL\\sleeper_lineup_bot\\dashboard_template.html"
timestamp: 2026-11-02T21-38-10Z
slug: dashboard-template-html
---
Method: dual-agent (A: design review · B: detector and browser evidence)

## Design Health Score

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | Visibility of system status | 3 | Header shows data age, but Matchups scores refresh with no timestamp |
| 2 | Match with the real world | 3 | Root for/against fits; "lean", "swing" and raw SUPER_FLEX leak through |
| 3 | User control and freedom | 3 | Esc and persisted state good; no collapse-all; typing in search silently switches tabs |
| 4 | Consistency and standards | 2 | "+" means net, game lead, "+4 more", swing and dollars; Settings reachable only through Help or $ Value |
| 5 | Error prevention | 2 | Failed roster fetch is swallowed and cached as empty, producing false zeros |
| 6 | Recognition over recall | 2 | Team chips vs Game total and "1 left · 0 left" have no on-screen legend |
| 7 | Flexibility and efficiency | 2 | Sorts exist, but no path from a game to the leagues it decides |
| 8 | Aesthetic and minimalist design | 2 | Permanent PPR footnote, Game total pills in every head, a note above every list |
| 9 | Error recovery | 2 | Load errors excellent; partial data failures sit inside an expanded row |
| 10 | Help and documentation | 3 | Accurate, but about 1,200px tall, not contextual, and hides the Settings door |
| | Total | 24/40 | Acceptable |

## Design Specificity Verdict

LLM assessment: authored at the core, generic at the shell. The collapsed game card, lean chips, For/Against digest, "Hurt −173 pts" and the tick-and-overflow stat bar belong only to this product. Matchups and $ Value are stock heading/selects/note/list screens, and the five-button bar turns one question into five destinations.

Deterministic scan: one CLI finding, pulsing-dot at dashboard_template.html:72 (false positive: marks real live games, disabled under reduced motion). Browser overlay caught .mrow.dn{opacity:.85} (line 183) at 4.07:1 in light mode, 225 hits from one CSS cause, which the design review missed. No overflow at 320 or 375, all targets at least 44px, no console errors. Advisory only: flat-type-hierarchy, one straggler in Help, line-length on p.sumbar at desktop width only.

## Overall Impression

The collapsed card is the best thing here and the live-Sunday default removes it. Foundations are sturdy; the problems are judgment, not engineering. The biggest opportunity is making the page true and short at 1 PM rather than adding surfaces.

## What's Working

1. Collapsed game card: answers the core question in about a second, 132px tall, four games per screen.
2. Sign and label redundancy: +/− on every number, true minus, labelled For/Against, screen-reader text.
3. Accessibility and resilience base: focus trap, focus restored after re-render, inert, offline copy with last saved view, retry.

## Priority Issues

[P0] Missing stats render as real zeros. Lawrence showed "0 pass yds · 0 TD · 0 INT · 19.4 pts" and "UNDER −249.5 · hurts you"; the only caveat was after expanding, and Parker Washington had none. act defaults to 0 (line 413), so the "stats unavailable" branch (line 392) never runs, and a failed roster fetch is cached as an empty map for the session (lines 347–350). ESPN 404 for Jacksonville was seen once in the review; a later recheck returned 200, so the trigger is intermittent and can hit any team. The code path is confirmed. Matched players with no box entry also show earned zeros (Otton, Ferguson). P0 because misleading is worse than missing, not because the page fails to load. Fix: match names from summary.boxscore before the roster, don't cache failures, make act null when unmatched, show "No ESPN stats", suppress helps/hurts. Command: /impeccable harden

[P1] Live games open by default. S.open[key]??(st==="in") (line 627) opens every live card and line 154 hides the digest. 8 simulated live games: 7,394px, about nine screens, vs 2,135px collapsed. Fix: default collapsed, keep the digest in the head, order live cards by stakes; live loading is gated on open cards at line 850 and must change too. Command: /impeccable distill

[P1] "Hurts you" contradicts the swing. St. Brown reads "Helped most +101" and "swing +101" while all four bars say "UNDER · hurts you". Missing a sportsbook line doesn't hurt the owner; on a final it's wrong. Fix: neutral bar copy ("Under by 0.5"), reserve helps/hurts for swing or points, never on the projection-based Fantasy pts bar. Command: /impeccable clarify

[P1] Matchups doesn't support the decision and its projection overstates. "Down 3.2" red pill beside proj 169.9–159.1 with nothing reconciling them; "1 left · 0 left" unlabelled. more+=Math.max(x.proj-x.pts,0) (line 539) keeps nearly the full pregame total late in a game. Stats and projection queries omit LB/DL/DB (lines 306, 314), so "No Sleeper stats" blames Sleeper for our query. Fix: "You 1 left · them 0", two-part verdict, time-scaled remaining points, IDP in the queries. Command: /impeccable clarify, then /impeccable harden

[P2] Five tabs dilute the question and $ Value isn't earned. "Matchups" has no clearance at 375px because the line 173 fix applies only under 360. $ Value needs 39 manual entries and defaults to an empty result today. Search stays on Matchups and $ Value but searches only Players. Fix: merge $ Value into Players as a sort, four tabs, Settings in the header, search on Players only. Command: /impeccable distill

## Persona Red Flags

Alex: must collapse eight live cards one by one; default sort ranks Swift (net 0) above Odunze (+3).
Sam: .head accessible name is the whole scoreboard; tabs use aria-pressed; input borders about 1.2:1; #meta re-announces "updated N min ago".
Casey: refresh, week arrows, search and Filter all at the top edge; "DEN 28 +2" reads like a spread; sticky chrome about 45% of the screen with Filter open.
Owner with 40 leagues: net weights a blowout the same as a one-point league; nothing links a game to the tight matchups it swings; five wrong Jacksonville rows damage trust in every row.

## Minor Observations

- .row:first-of-type{border-top:0} (line 35) matches every row, so list dividers never show.
- Thu −173 + Sun +114 = −59, but the bar shows −60 (separate rounding).
- .stickyhd.stick{top:57px} hardcodes header height (line 130).
- "Pull ↻" (line 572) implies pull-to-refresh, which doesn't exist.
- Green pills are the tightest passing light contrast at 4.77:1.
- PRODUCT.md says red backdrop with green fill; the bars are blue.

## Questions to Consider

- Should a one-point matchup count more than a 60-point blowout?
- Would one live "Now" list of the five players who can still swing a close league replace three tabs on Sunday?
- If a stat can't be verified, why does a 0 ever render by default?
