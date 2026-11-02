---
target: dashboard
total_score: 28
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:/home/user/sleeper-lineup-bot/dashboard_template.html"
target_fingerprint: "sha256:373e5b8b451dd918ddaaf89fc34c1b8944ac3adb73b00852b7b7fb9f531368a8"
target_path: /home/user/sleeper-lineup-bot/dashboard_template.html
timestamp: 2026-11-02T22-39-25Z
slug: dashboard-template-html
---
Method: dual-agent (A: design review · B: detector + overlay, 18 populated views). Target @ 9a319a3. Total 28/40 (H1 3, H2 3, H3 3, H4 3, H5 3, H6 2, H7 3, H8 2, H9 3, H10 3).
Detector: pulsing-dot L71 (false positive, live-bound); flat-type-hierarchy in sheets; Settings h3 (17.6px, inline style) larger than sheet h2 (17px) — real.
Priority: [P1] no one-glance verdict on game card (lean + Game total + lead text compete); [P1] Matchups doesn't scale to 40 leagues (no tally, no stake sort, tall cards); [P2] silent 200/100 row caps and muted stale/error state; [P2] By game puts finished above live; [P2] dark-mode selected controls glare.
Minor: expanded state leaks across tabs; next-week next to refresh; tank pill SR redundancy; RB stat separator; help says DEF adds 0; tank proj verdict not annotated; (tank) wraps; title mismatch; inline h3 style.
