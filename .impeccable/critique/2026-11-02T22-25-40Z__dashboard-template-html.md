---
target: dashboard
total_score: 26
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:/home/user/sleeper-lineup-bot/dashboard_template.html"
target_fingerprint: "sha256:a01c20af7fbbd46550b8c0174466deb9e4c3ac66efea0d2a6778ea7e6ebc370a"
target_path: /home/user/sleeper-lineup-bot/dashboard_template.html
timestamp: 2026-11-02T22-25-40Z
slug: dashboard-template-html
---
Method: dual-agent (A: design review · B: detector + overlay, 14 populated views). Target: dashboard_template.html @ d62e12d.
Score note: 26/40 vs prior 30/40 is reviewer variance (stricter on 4/6/7); all five previously fixed issues verified fixed.

## Design Health Score
| # | Heuristic | Score | Key Issue |
|---|---|---|---|
| 1 | Visibility of System Status | 3 | Invisible auto-poll; finished Players rows lack pts unless game opened |
| 2 | Match System / Real World | 3 | Coined terms: Game total, swing, cancels out |
| 3 | User Control and Freedom | 3 | No real gaps |
| 4 | Consistency and Standards | 2 | One pill for four number types; tank "Down 1.4" green |
| 5 | Error Prevention | 3 | Buy-in silently ignores bad input; week arrows live on error |
| 6 | Recognition Rather Than Recall | 2 | Team chips / Game total explained only in help |
| 7 | Flexibility and Efficiency | 2 | No deep links, no Matchups filter, nav last in tab order |
| 8 | Aesthetic and Minimalist Design | 3 | ~12 numbers in live card header |
| 9 | Error Recovery | 3 | "N leagues didn't load" unnamed |
| 10 | Help and Documentation | 3 | Dense help, hard-coded "41 leagues" |
| **Total** | | **26/40** | **Acceptable** |

## Design Specificity
Content authored for product; visual voice generic-careful. Detector: pulsing-dot L71 (false positive, live-bound, labeled, reduced-motion off); flat-type-hierarchy on help sheet at phone width (low). Players/Filter/Matchups clean.

## Priority Issues
- [P1] Tank Matchups green "Down 1.4" — color-only verdict (L578-581, L590). Fix: verdict in words. /impeccable clarify
- [P1] One pill style for player net, team lean, game total, outcome (L677, L685). Fix: pill only for player nets; leans/total as muted text. /impeccable distill
- [P2] Expanded game loses score/context on scroll (L17, L61, L98). Fix: sticky compact head below header. /impeccable layout
- [P2] Players finished rows lack pts unless game opened; By game has no dividers (L465, L881). Fix: use S.pts, lazy-load, dividers. /impeccable harden
- [P3] Final header "FINAL · 1 · 1 HELPED · 0 HURT" (L789). Fix: "1 final game · helped +59 pts", drop zeros. /impeccable clarify

## Persona Red Flags
Alex: no Matchups filter; no deep links; count vs $ sign disagreement unexplained; failed leagues unnamed.
Sam: tank pill color-only; nav last in tab order; rows lack aria-controls; Even chip outline low contrast; settings placeholders look filled.
Casey: refresh/week/settings top-right; invisible auto-poll; expanded card loses score; "2 more" looks tappable; Matchups tight at 320px.

## Minor Observations
"41 leagues" in help; Matchups-only h2; error-state week arrows; buy-in invalid input silent; dark active tab loud; two timestamps in meta; buy-in rank flattens groups.

## Questions
FOR/AGAINST as headline? Tank leagues in "good/bad for you" language? Players as a search inside Games, freeing a "Now" tab?
