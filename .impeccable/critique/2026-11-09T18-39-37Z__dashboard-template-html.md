---
target: dashboard_template.html
total_score: 26
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:C:\\Users\\Kctob\\Downloads\\Exposure\\dashboard_template.html"
target_fingerprint: "sha256:8411f693250bdf87797ff1569d828a43abe46d2b7f717f1dc5e6ef42e681617d"
target_path: "C:\\Users\\Kctob\\Downloads\\Exposure\\dashboard_template.html"
timestamp: 2026-11-09T18-39-37Z
slug: dashboard-template-html
---
# Critique: Exposure (dashboard_template.html) — 2026-11-09
Method: dual-agent (A design review with screenshots at 390px as ktob; B detector: 0 findings, overlay unavailable: no JS-capable browser tool)

## Heuristics 26/40
1 Status 3 (silent ESPN failure) · 2 Real world 2 (41-league point sums) · 3 Control 3 (tab switch clears search/details) · 4 Consistency 2 (#/$ vs Leagues/Buy-in $; uppercase label overload) · 5 Prevention 3 · 6 Recognition 2 (collapsed live card lost names) · 7 Flexibility 3 · 8 Minimalist 2 (crowded Games top; recap duplicates Final header) · 9 Recovery 3 · 10 Help 3

## Specificity
Authored vocabulary; generic/layered type system (~11 sizes, many 12px uppercase labels).

## Priority issues
- [P1] Collapsed live card no longer names who to root for (user-requested change; fix: compact possession/down into scoreboard, restore top for/against line) — layout
- [P1] Swing numbers are 41-league sums with no scale; pre-game projections in loud red — clarify
- [P2] Games top crowded (tank nudge, unit toggle), recap duplicates Final header; recap missing on finished current week — distill
- [P2] ESPN failure silent ("CAR – GB", "BUF @ MIN ·") — harden
- [P3] Red zone tag uses --bad; Sporty --info == --warn — colorize

## Personas
Owner mid-Sunday: 7 expand/collapse cycles. Alex: tab switch wipes search, no URL state, two controls one setting. Sam: sign-in no busy state, unlabeled help icon, 11-12px uppercase. Casey: top-right controls, adjacent Not now/Open Settings.

## Minor
Final header orphan wrap; logos compete with net badge; possession dot resembles live dot; past-week Players empty (pfin stays collapsed with byes); Matchups tally wraps.

## Questions
Field state vs what it means for you? Per-league vs total units? Ranked "who matters now" feed?
