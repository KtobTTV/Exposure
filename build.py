"""Build Exposure: one self-contained phone page that pulls your live lineups from
Sleeper and shows, game by game, who to root for / against across every league.

    python build.py <sleeper-username>      # writes index.html (the published page)

Only the player-name table, your Sleeper user id and your tank-league list are baked
in (so the page loads fast); lineups, scores, lines and stats are fetched live in the
browser. Rebuild when the name table should be refreshed or tanking_leagues.txt
changes, then commit and push index.html to publish.

Standard library only: no other packages or files are needed.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE / "index.html"
CACHE = HERE / ".cache"
API = "https://api.sleeper.app/v1"


def _get(url: str, tries: int = 4):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "exposure-build/1.0 (+personal use)"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # network
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"Sleeper request failed: {url}: {last}")


def resolve_user_id(name_or_id: str) -> str:
    s = (name_or_id or "").strip().lstrip("@")
    if not s:
        raise SystemExit("Give your Sleeper username: python build.py <username> (or set SLEEPER_USERNAME)")
    if s.isdigit():
        return s
    data = _get(f"{API}/user/{s}")
    if not data or "user_id" not in data:
        raise SystemExit(f"Could not find Sleeper user '{s}' (use your @handle, not your email).")
    return data["user_id"]


def load_players(max_age_hours: float = 24.0) -> dict:
    """Sleeper's full NFL player table (~5 MB), cached for a day."""
    CACHE.mkdir(exist_ok=True)
    fp = CACHE / "players_nfl.json"
    if fp.exists() and time.time() - fp.stat().st_mtime < max_age_hours * 3600:
        return json.loads(fp.read_text(encoding="utf-8"))
    data = _get(f"{API}/players/nfl")
    fp.write_text(json.dumps(data), encoding="utf-8")
    return data


def tanking_ids() -> list[str]:
    """League ids listed in tanking_leagues.txt (sign is reversed there: you want to lose)."""
    try:
        text = (HERE / "tanking_leagues.txt").read_text(encoding="utf-8")
    except FileNotFoundError:
        return []
    return sorted({m.group(1) for line in text.splitlines() if (m := re.match(r"\s*(\d{8,})", line))})


def build(uid: str, out: Path = OUT) -> Path:
    table = {}
    for pid, m in load_players().items():
        pos = m.get("position") or ((m.get("fantasy_positions") or [None])[0])
        if pos not in ("QB", "RB", "WR", "TE", "K", "DEF"):
            continue
        team = m.get("team")
        if not team and m.get("status") != "Active":
            continue
        name = f"{team} DEF" if pos == "DEF" else (f"{m.get('first_name', '')} {m.get('last_name', '')}").strip()
        table[pid] = [name or pid, pos, team or "FA", str(m.get("espn_id") or "")]
    html = (HERE / "dashboard_template.html").read_text(encoding="utf-8")
    html = (html.replace("__TANK__", json.dumps(tanking_ids()))
                .replace("__UID__", str(uid))
                .replace("__PLAYERS__", json.dumps(table, separators=(",", ":"))))
    # Build id of this exact page, so an open copy can tell when a newer one is published.
    html = html.replace("__BUILD__", hashlib.sha256(html.encode("utf-8")).hexdigest()[:12])
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    uname = sys.argv[1] if len(sys.argv) > 1 else os.getenv("SLEEPER_USERNAME", "")
    p = build(resolve_user_id(uname))
    print(p.name, f"{p.stat().st_size // 1024} KB")
