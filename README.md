# Exposure

Who to root for, across every Sleeper fantasy league you play, one NFL game at a time.

Exposure adds up every lineup in all your leagues and gives each player one number: **+4** means
he's in 4 more of your lineups than your opponents' lineups (root for him), **−3** is the reverse
(root against him). Leagues you mark as tanking are flipped.

Live at **https://ktobttv.github.io/Exposure/**. Open it on your phone, enter your Sleeper username
and add it to the home screen.

## What's on it
- **Games:** every game with team lean, live down, distance and who has the ball (tap a game for who to
  root for and against), a week picker at the top, and on any other week a recap of how much
  that week helped or hurt you against its projection, a live "so far" points swing,
  a Leagues / Buy-in $ switch that ranks who to root for by buy-in dollars, per-player stat bars (DraftKings lines vs. the live ESPN box score), and finished-game results.
- **Players:** every player with his team logo and his net across your leagues; search, filter, and switch between
  counting leagues (**#**) and counting league buy-ins (**$**).
- **Matchups:** every league's projected finish and live score, with a "your way / not / toss-ups"
  tally, tank leagues handled.
- **Settings:** a color theme (Auto, Light, Dark, Sporty, Sunset, Ocean or Daylight), your Sleeper account, plus a Leagues dropdown with a Competing / Tanking switch and
  buy-in for each league. "Copy my setup link" moves all of it to another device (computer, home-screen
  app) without an account.

Everything is fetched live in the browser from Sleeper's public API and ESPN. There's no password;
your username, tank choices and buy-ins stay on your device.

## Build and publish
```
python build.py
git add index.html && git commit -m "Publish" && git push
```
`build.py` uses only the Python standard library. It downloads Sleeper's player table (cached in
`.cache/` for a day), bakes it into the page and writes `index.html`. Rebuild when you change the
template or want fresh player names; lineups and scores are always live.

Open copies of the page check for a newer build and show "New version available · tap to reload".

## Files
- `dashboard_template.html`: the app (HTML, CSS and JS in one file).
- `build.py`: fills the template and writes `index.html`.
- `index.html`: the published page (generated; commit it to publish).
- `PRODUCT.md`, `.impeccable/`: product context and design-critique snapshots.

The automated lineup-setting bot lives separately in `KtobTTV/sleeper-lineup-bot`.
