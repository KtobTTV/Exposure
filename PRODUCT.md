# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack
Existing codebase: a single self-contained vanilla HTML/CSS/JS page (`dashboard_template.html`) with no framework, plus `build.py` (standard-library Python) that bakes in the player-name table and writes `index.html`. GitHub Pages serves `index.html` from this repo; the page fetches live data in the browser.

## Users
The owner (Sleeper username `ktob`) plays in roughly 40 Sleeper fantasy football leagues at once and is the primary user. Any Sleeper user can now enter a username and use it; the first person beyond the owner is a curious leaguemate who should be exploring every feature within a minute. The stated ambition is a wider fantasy-football audience later, possibly on the App Store; no audience beyond the owner and friends is confirmed yet. The dashboard is used on a phone, in quick glances while NFL games are live.

## Product Purpose
Exposure tells someone in many Sleeper leagues, per NFL game and per player, how many of their leagues start each player versus how many opponents start him, so they know who to root for and against, plus where every matchup is headed. Success is a Sunday glance that answers "who do I root for in this game?" without opening 40 leagues. The automated lineup-setting bot is a separate project (`KtobTTV/sleeper-lineup-bot`).

## Positioning
Aggregates exposure across all of one person's leagues into a single net (+/−) per player, game by game, with the matchup perspective built in: leagues marked Tanking in Settings reverse the sign. Stock fantasy apps show one league at a time.

## Operating Context
- Data comes from Sleeper's public API (leagues, rosters, matchups, schedule, projections), ESPN (live box scores; DraftKings player-prop lines hosted by ESPN), all fetched client-side by the dashboard.
- The owner's lineup bot (separate repo `KtobTTV/sleeper-lineup-bot`) runs on their Windows PC; Exposure does not depend on it.
- Exposure lives at https://ktobttv.github.io/Exposure/ (this repo, `KtobTTV/Exposure`, renamed from `root-for-against`: the source and the published `index.html`, which holds a player-name table, never a user id, tank list or lineups; those stay on each device). A Refresh button reloads lineups and stats; a build id lets an open copy offer a reload when a new version is published.
- Publishing: `python build.py`, then commit and push `index.html`.

## Capabilities and Constraints
- Dashboard: Games tab (per-game cards of players to root for / against / even, net counts; collapsed by default so the digest stays glanceable), Players tab (search, Root for / Root against filters, rank by league count or buy-in dollars), Matchups tab (score and projected finish in every league), Settings in the header (Sleeper account, and a Leagues dropdown with a Competing / Tanking switch and buy-in per league, all stored on the device). Tap a player for the leagues involved and, in game cards, stat bars (line vs live actual stat).
- Stat bars: QB passing yards, rushing yards, passing TDs; RB receptions, rushing yards, TDs; WR/TE receptions, receiving yards, TDs; plus Fantasy pts. Pale blue backdrop up to the line, solid blue fill showing actual, overflow stub when over. Bars state facts against the line; helps/hurts belongs to swing and points. TD bars use a 0.5 anytime line; where no DraftKings line exists, a Sleeper projection is used and labeled "proj". A missing stat renders as "no ESPN stats", never 0.
- Terminology: "root for" (+) = players the owner starts net of opponents; "root against" (−) is the reverse; "net" = leagues starting him minus opponents starting him; "tank" leagues reverse the sign.
- Technical: cross-origin browser requests only to APIs that allow them (Sleeper, ESPN); no secrets may ship in the public page; Claude's artifact sandbox blocks outbound requests so the page cannot be hosted as an artifact. Sleeper often lacks ESPN ids, so players are matched by name through ESPN rosters.
- Undecided: whether to pursue wider distribution and what that would require.

## Brand Commitments
The product is named **Exposure**: a multi-league player's exposure to each NFL player, net of opponents. "Root for" / "Root against" stay as the in-app labels. The repo is `KtobTTV/Exposure` and the page is served at https://ktobttv.github.io/Exposure/ (the old `/root-for-against/` address no longer works).

## Evidence on Hand
Live data against the owner's real leagues (41 leagues, 14 games in Week 8) was used to verify the dashboard. No testimonials, user counts, or external usage evidence exist; do not invent any.

## Product Principles
- Glanceable first: the answer to "who do I root for in this game?" must read in a second on a phone, mid-game.
- The sign is the signal: +/− and labels carry meaning, never color alone, because red/green is the core cue.
- Never lie about the data: say when a line is a projection, a stat is stale, or a player could not be matched.
- Live and accurate over decorated: the page fetches fresh data; anything that could mislead (stale lines, wrong sign in tank leagues) is worse than missing.
- Private by construction: nothing personal or secret goes in the public page.

## Accessibility & Inclusion
Phone-first, used one-handed and in glances; follows the OS light/dark setting by default (Auto), with Light, Dark, Sporty, Sunset, Ocean and Daylight color themes in Settings. Every theme keeps text and the good/bad colors at WCAG AA contrast or better. No further accessibility needs were stated; the principle above (meaning not carried by color alone) is a product choice, not a stated user requirement.
