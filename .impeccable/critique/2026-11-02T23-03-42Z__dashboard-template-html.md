---
target: dashboard
total_score: 31
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 2
target_identity: "file:/home/user/sleeper-lineup-bot/dashboard_template.html"
target_fingerprint: "sha256:d5ca452fb8890270c19ee1ccafd72abd47fe81b7ada7e0bb430e0382ff9fbc6a"
target_path: /home/user/sleeper-lineup-bot/dashboard_template.html
timestamp: 2026-11-02T23-03-42Z
slug: dashboard-template-html
---
Method: dual-agent (A: design review · B: detector + overlay, 20 populated views). Target @ d0878fd. Total 31/40 (H1 4, H2 3, H3 3, H4 3, H5 3, H6 3, H7 3, H8 3, H9 3, H10 3).
Detector: pulsing-dot only (false positive, live-bound).
Priority: [P1] Settings: blank inputs hide counted guess; error text grey (specificity bug), caption stays; [P1] Matchups pill/tally use current margin while sort/toss-up use projection; [P2] Buy-in $ is a units mode hidden in Rank; [P2] open Matchups header sticky at full height; [P3] overflow stub magnitude unreadable, stat lines wrap inside units.
Minor: no Matchups search; matchup pill sr text masked by aria-label; "Tap ↻" glyph copy; dead placeholder style.
