"""Build the phone dashboard: one self-contained HTML page that pulls your live
lineups from Sleeper and shows, game by game, who to root for / against, plus a
player search with the + / - for each name.

    python dashboard.py            # writes reports/dashboard.html

Only the player-name table is baked in (so the page loads fast); everything else is
fetched live in the browser, so it never goes stale between bot runs. exposure.py
calls build_dashboard() on every run to keep the name table fresh.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import sleeper_api as api

HERE = Path(__file__).parent
OUT = HERE / "reports" / "dashboard.html"


def build_dashboard(uid: str, out: Path = OUT) -> Path:
    players = api.load_players()
    table = {}
    for pid, m in players.items():
        pos = m.get("position") or ((m.get("fantasy_positions") or [None])[0])
        if pos not in ("QB", "RB", "WR", "TE", "K", "DEF"):
            continue
        team = m.get("team")
        if not team and m.get("status") != "Active":
            continue
        name = f"{team} DEF" if pos == "DEF" else (f"{m.get('first_name', '')} {m.get('last_name', '')}").strip()
        table[pid] = [name or pid, pos, team or "FA", str(m.get("espn_id") or "")]
    html = (HERE / "dashboard_template.html").read_text(encoding="utf-8")
    try:
        from exposure import tanking_ids

        tank = sorted(tanking_ids())
    except Exception:
        tank = []
    html = html.replace("__TANK__", json.dumps(tank)).replace("__UID__", str(uid)).replace("__PLAYERS__", json.dumps(table, separators=(",", ":")))
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    return out


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv

        load_dotenv(HERE / ".env")
    except Exception:
        pass
    uname = (sys.argv[1] if len(sys.argv) > 1 else os.getenv("SLEEPER_USERNAME", "")).strip()
    p = build_dashboard(api.resolve_user_id(uname))
    print(p, f"{p.stat().st_size // 1024} KB")
