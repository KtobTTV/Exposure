# Exposure

Who to root for, across every Sleeper fantasy league you play, one NFL game at a time.

Exposure adds up every lineup in all your leagues and gives each player one number: **+4** means
he's in 4 more of your lineups than your opponents' lineups (root for him), **−3** is the reverse
(root against him). Leagues you're tanking in are flipped.

Live at **https://ktobttv.github.io/root-for-against/** (open it on your phone and add it to the
home screen).

## What's on it
- **Games:** every game with who to root for and against, team lean, a live "so far" points swing,
  per-player stat bars (DraftKings lines vs. the live ESPN box score), and finished-game results.
- **Players:** every player with his net across your leagues; search, filter, and switch between
  counting leagues (**#**) and counting league buy-ins (**$**).
- **Matchups:** every league's projected finish and live score, with a "your way / not / toss-ups"
  tally, tank leagues handled.

Everything is fetched live in the browser from Sleeper's public API and ESPN. Nothing to log into.

## Build and publish
```
python build.py <your-sleeper-username>
git add index.html && git commit -m "Publish" && git push
```
`build.py` uses only the Python standard library. It downloads Sleeper's player table (cached in
`.cache/` for a day), bakes it into the page with your Sleeper user id and the league ids in
`tanking_leagues.txt`, and writes `index.html`. Rebuild when you change `tanking_leagues.txt` or
want fresh player names; lineups and scores are always live.

Open copies of the page check for a newer build and show "New version available · tap to reload".

## Files
- `dashboard_template.html`: the app (HTML, CSS and JS in one file).
- `build.py`: fills the template and writes `index.html`.
- `index.html`: the published page (generated; commit it to publish).
- `tanking_leagues.txt`: league ids where you want to lose, one per line.
- `PRODUCT.md`, `.impeccable/`: product context and design-critique snapshots.

The automated lineup-setting bot lives separately in `KtobTTV/sleeper-lineup-bot`.
