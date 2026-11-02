---
target: phone dashboard
total_score: 22
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 3
target_identity: "file:C:\\Users\\Kctob\\OneDrive\\Documents\\Sports Models\\NFL\\sleeper_lineup_bot\\dashboard_template.html"
target_fingerprint: "sha256:9cddd06695afde850be67058fe46dca95cef4637bf0855e314e36336a0263786"
target_path: "C:\\Users\\Kctob\\OneDrive\\Documents\\Sports Models\\NFL\\sleeper_lineup_bot\\dashboard_template.html"
timestamp: 2026-11-02T04-24-16Z
slug: dashboard-template-html
closed: true
---
# Critique: dashboard_template.html

Method: dual-agent. Score 22/40 (Acceptable, 55%).

Heuristics: 1 Status 2 | 2 Match 3 | 3 Control 2 | 4 Consistency 2 | 5 Error prevention 2 | 6 Recognition 3 | 7 Flexibility 2 | 8 Minimalist 3 | 9 Error recovery 2 | 10 Help 1.

Detector: static scan 0 findings; browser overlay 1 finding (search placeholder 3.7:1 in dark mode).

## Priority issues
- [P1] Week-stepper state race and no feedback (harden)
- [P1] Green means both root-for and over-the-line; root-against players get happy green bars (colorize, clarify)
- [P1] Live game is not first on Sunday, no score/clock/kickoff, no auto-poll (layout, clarify)
- [P2] Accessibility: divs not focusable, unlabeled icon buttons and search, bar line label ~1.8-2.0:1 contrast (audit, harden)
- [P2] Small crowded controls: chips 29px, rows 40px, stepper 29x36, header 18-27% of screen (adapt, distill)

## Minor
Preview name uses last word (III/Sr.), MM-DD dates, footnote repeats per player, unlabeled +21/-16 pair, Hide finished vanishes in search, "you/opp" counts mislabel tank leagues.
