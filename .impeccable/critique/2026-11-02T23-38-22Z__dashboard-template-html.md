---
target: dashboard
total_score: 33
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 1
target_identity: "file:/home/user/sleeper-lineup-bot/dashboard_template.html"
target_fingerprint: "sha256:d1b695a0109c44e2e4bc07fc4b68e86edaab48b1c85ad4378201223499ac6dbb"
target_path: /home/user/sleeper-lineup-bot/dashboard_template.html
timestamp: 2026-11-02T23-38-22Z
slug: dashboard-template-html
---
Method: dual-agent (A: design review · B: detector + overlay, 22 populated views). Target @ 74bbbf1. Total 33/40 (H1 4, H2 3, H3 4, H4 3, H5 3, H6 3, H7 3, H8 3, H9 4, H10 3).
Detector: CLI clean. Browser: text-overflow on Matchups tally (span.nw / b.tu, 30px under the sort select) — real.
Priority: [P1] Matchups tally truncated under sort select; [P2] opening a game hides its leans/answer; [P2] buy-in $ mode not visible once panel closes, no game dividers; [P3] vocabulary drift (proj / game proj / anytime; present tense on finals); [P3] live stat lines wrap 2-3 lines.
