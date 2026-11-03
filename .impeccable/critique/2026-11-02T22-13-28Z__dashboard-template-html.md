---
target: dashboard
total_score: 30
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:/home/user/sleeper-lineup-bot/dashboard_template.html"
target_fingerprint: "sha256:f34af6b518fb7591856b5f59c64a26cdfe06822cd4c4ce6cf992d0f46563210e"
target_path: /home/user/sleeper-lineup-bot/dashboard_template.html
timestamp: 2026-11-02T22-13-28Z
slug: dashboard-template-html
---
Method: dual-agent (A: design review · B: detector + overlay). Target: dashboard_template.html @ 77a8edc.

## Design Health Score
| # | Heuristic | Score | Key Issue |
|---|---|---|---|
| 1 | Visibility of System Status | 4 | Error state leaves no tab highlighted |
| 2 | Match System / Real World | 3 | "BUF +4" lead beside +/- net chips |
| 3 | User Control and Freedom | 3 | Expanded rows lost on reload; confirm() reset, no undo |
| 4 | Consistency and Standards | 3 | Three expand patterns; Rank by + Sort overlap |
| 5 | Error Prevention | 3 | Week arrows live on error screen ("Wk –" → week 2) |
| 6 | Recognition Rather Than Recall | 3 | Team chips / Game total / swing need help sheet |
| 7 | Flexibility and Efficiency | 2 | No live-exposure view, no deep links, nav last in tab order |
| 8 | Aesthetic and Minimalist Design | 3 | Week summary + PPR caveat between Live and Upcoming |
| 9 | Error Recovery | 4 | Plain errors, Try again, last saved view kept |
| 10 | Help and Documentation | 2 | 9-bullet prose help, hard-coded "41 leagues", no inline help |
| **Total** | | **30/40** | **Good** |

## Design Specificity
Content/IA authored for the product (root for/against/even, tank sign flip, Helped +59 pts, honest data labels). Visual layer generic (system font, white cards, black pills); stat bar is the one signature.
Detector: pulsing-dot (L71-72, false positive: tied to live state, labeled, reduced-motion off); straggler in help L216 (nit); flat-type-hierarchy <420px, h1 15px = body (L104) vs help h2 17px (partly real). Players/Matchups clean.

## Priority Issues
- [P1] "+N" overloaded: leadTxt L676 "BUF +4" beside chipN L625 nets. Fix: drop lead or "BUF leads by 4". /impeccable clarify
- [P1] Players default "Most started" puts net-0 first (L745/750). Fix: sort by |net|, or Even bin. /impeccable layout
- [P2] Players Filter panel 11 options, Rank by vs Sort overlap (L731-735). Fix: merge into one Rank select. /impeccable distill
- [P2] Week summary + PPR caveat mid-live (L780-782); "0 hurt you" red. Fix: fold into Final header, neutral zeros. /impeccable layout
- [P3] Collapsed game aria-label drops names (L679). Fix: aria-labelledby scoreboard + .lines. /impeccable audit

## Persona Red Flags
Alex: no live-exposure view; sort fights him; ~40 ungrouped buy-in inputs; expansion lost on reload/45s refresh (L895); "41 leagues" hard-coded.
Sam: card labels lack names; tank-league green "Down 1.4" color-only for sighted users; nav last in tab order; 1.2:1 row borders.
Casey: double "+N"; expanded live player scrolls game header away; refresh top-right; "Matchups" touches edges at 320px.

## Minor Observations
Error state Wk – with live arrows; upcoming time column wastes width; Even group lacks count in finals; duplicate buy-in empty copy; Matchups note repeats meta line.

## Questions
Does Players need to be a tab? Should net-0 ever leave an Even bin? Could live cards lead with one net swing per game?
