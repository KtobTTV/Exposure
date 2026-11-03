---
target: phone dashboard
total_score: 26
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:C:\\Users\\Kctob\\OneDrive\\Documents\\Sports Models\\NFL\\sleeper_lineup_bot\\dashboard_template.html"
target_fingerprint: "sha256:f732185b0348cc3cf5b6b53f8c654fd270d517183f37d9f945f82ad70aa68a65"
target_path: "C:\\Users\\Kctob\\OneDrive\\Documents\\Sports Models\\NFL\\sleeper_lineup_bot\\dashboard_template.html"
timestamp: 2026-11-02T05-14-10Z
slug: dashboard-template-html
---
# Critique: dashboard_template.html (run 3)

Method: dual-agent. Score 26/40 (Acceptable, 65%), down from 28/40 because of the new outcome tag.

Heuristics: 1 Status 3 | 2 Match 3 | 3 Control 3 | 4 Consistency 3 | 5 Error prevention 2 | 6 Recognition 2 | 7 Flexibility 2 | 8 Minimalist 3 | 9 Error recovery 3 | 10 Help 2.

Detector: CLI 1 warning (LIVE pulse dot, mitigated); browser overlay clean in dark and light. No control under 44px, no horizontal scroll at 375/320, bar track outline 3.03/3.57:1, all text AA.

Outcome tag check: arithmetic correct vs its definition, but sign disagreed with an approximate fantasy-points swing in 6 of 13 games; headline 3 your way / 10 against vs about 7 / 6 by points.

## Priority issues
- [P1] Outcome tag and "This week" summary overstate what they know (clarify)
- [P1] Live games: team-level chips only, no per-player live stats, long first screen (layout)
- [P2] One green/red pill vocabulary means three things; lean chips can both be green (distill)
- [P2] Invisible affordances and help: no chevrons, help marker missing, tooltips on touch (onboard)
- [P2] Players tab doesn't serve a Sunday glance: finals first, no status filter, filters not sticky (adapt)

## Minor
"updated N min ago" for stale cache, hard-coded "This week", meta wrap, unused team colors.
