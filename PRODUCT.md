# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
Existing codebase: Python 3.10 tooling (Flask local app, reportlab PDF, openpyxl Excel) and a single self-contained vanilla HTML/CSS/JS dashboard page with no framework or build step. The dashboard is a static file served from GitHub Pages and fetches live data in the browser.

## Users
The owner (Sleeper username `ktob`) plays in roughly 40 Sleeper fantasy football leagues at once and is the primary user. The stated ambition is to share the tools with a wider fantasy-football audience later; no audience beyond the owner and friends who received the share zip is confirmed yet. The dashboard is used on a phone, in quick glances while NFL games are live.

## Product Purpose
Automates and informs a many-league Sleeper fantasy football operation: a bot that sets the projected-best legal lineup in every league (and handles IR moves), plus reporting that tells the owner, per NFL game and per player, how many of their leagues start each player versus how many opponents start him, so they know who to root for and against. Success is correct lineups without manual work, and a Sunday glance that answers "who do I root for in this game?" without opening 40 leagues.

## Positioning
Aggregates exposure across all of one person's leagues into a single net (+/−) per player, game by game, with the matchup perspective built in: leagues where the owner is tanking are listed in `tanking_leagues.txt` and reverse the sign. Stock fantasy apps show one league at a time.

## Operating Context
- Data comes from Sleeper's public API (leagues, rosters, matchups, schedule, projections), ESPN (live box scores; DraftKings player-prop lines hosted by ESPN), all fetched client-side by the dashboard.
- The lineup bot and reports run on the owner's Windows PC via Task Scheduler (Thursday 6 PM, Sunday 12 PM, Tuesday 10 AM analysis) and push summaries to the owner's phone via ntfy.
- The dashboard lives at https://ktobttv.github.io/root-for-against/ (public repo `KtobTTV/root-for-against`, holding only the page and a player-name table, never lineups). A Refresh button reloads lineups and stats.
- Other surfaces: local Flask lineup UI (`ui.py`, `templates/index.html`); HTML, PDF and Excel exposure reports; a team-analysis report.

## Capabilities and Constraints
- Dashboard: Games tab (per-game cards of players to root for / against / even, net counts; collapsed by default so the digest stays glanceable), Players tab (search, Root for / Root against filters, rank by league count or buy-in dollars), Matchups tab (score and projected finish in every league), Settings in the header (league buy-ins, stored on the device). Tap a player for the leagues involved and, in game cards, stat bars (line vs live actual stat).
- Stat bars: QB passing yards, rushing yards, passing TDs; RB receptions, rushing yards, TDs; WR/TE receptions, receiving yards, TDs; plus Fantasy pts. Pale blue backdrop up to the line, solid blue fill showing actual, overflow stub when over. Bars state facts against the line; helps/hurts belongs to swing and points. TD bars use a 0.5 anytime line; where no DraftKings line exists, a Sleeper projection is used and labeled "proj". A missing stat renders as "no ESPN stats", never 0.
- Terminology: "root for" (+) = players the owner starts net of opponents; "root against" (−) is the reverse; "net" = leagues starting him minus opponents starting him; "tank" leagues reverse the sign.
- Technical: cross-origin browser requests only to APIs that allow them (Sleeper, ESPN); no secrets may ship in the public page; Claude's artifact sandbox blocks outbound requests so the page cannot be hosted as an artifact. Sleeper often lacks ESPN ids, so players are matched by name through ESPN rosters.
- Undecided: whether to pursue wider distribution and what that would require.

## Brand Commitments
The product is named **Exposure**: a multi-league player's exposure to each NFL player, net of opponents. "Root for" / "Root against" stay as the in-app labels. The public page is still served from the `root-for-against` repo so existing links and home-screen bookmarks keep working.

## Evidence on Hand
Live data against the owner's real leagues (41 leagues, 14 games in Week 8) was used to verify the dashboard. No testimonials, user counts, or external usage evidence exist; do not invent any.

## Product Principles
- Glanceable first: the answer to "who do I root for in this game?" must read in a second on a phone, mid-game.
- The sign is the signal: +/− and labels carry meaning, never color alone, because red/green is the core cue.
- Never lie about the data: say when a line is a projection, a stat is stale, or a player could not be matched.
- Live and accurate over decorated: the page fetches fresh data; anything that could mislead (stale lines, wrong sign in tank leagues) is worse than missing.
- Private by construction: nothing personal or secret goes in the public page.

## Accessibility & Inclusion
Phone-first, used one-handed and in glances; follows the OS light/dark setting. No further accessibility needs were stated; the principle above (meaning not carried by color alone) is a product choice, not a stated user requirement.
