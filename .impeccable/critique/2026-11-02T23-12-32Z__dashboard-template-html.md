---
target: dashboard
total_score: 32
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:/home/user/sleeper-lineup-bot/dashboard_template.html"
target_fingerprint: "sha256:e662aea30fb38e2898b7b30345b2847c0d7b73e9e5644735fcac62139a57f221"
target_path: /home/user/sleeper-lineup-bot/dashboard_template.html
timestamp: 2026-11-02T23-12-32Z
slug: dashboard-template-html
---
Method: dual-agent (A: design review · B: detector + overlay, 22 populated views). Target @ 561fa57. Total 32/40 (H1 4, H2 3, H3 3, H4 3, H5 3, H6 3, H7 3, H8 3, H9 4, H10 3).
Detector: pulsing-dot only (false positive, live-bound).
Priority: [P1] game-level answer is the quietest text and comes as three numbers (team lean, game total, nets); [P1] open matchup sticky header truncates the verdict; [P2] matchup rows don't connect to root for/against; [P2] sort silently live-first / Rank disappears in $ mode; [P3] overflow stub doesn't show magnitude, "Over by" wraps.
Minor: invalid buy-in silently keeps old value in total; two clocks in meta.
