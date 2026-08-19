#!/usr/bin/env python3
"""Editorial profile header for mahik504. Facts only. No live stats, snakes, or streaks.

Run from this folder: python generate_card.py
Commit dark.svg + light.svg when the facts change. Do not add a daily Actions job.
"""

from html import escape
from pathlib import Path

NAME = "Mahaveer Singh Gehlot"
HANDLE = "mahik504"
ROLE = "CS student · India"
LINE = "College work that should not die as a screenshot."
NOW = "Hiring flagship in public · 3D operator surface on the side"
STACK = "Python · TypeScript · React · Expo · SQL"
FOCUS = "ML pipelines · honest READMEs · surfaces people can click"

THEMES = {
    "dark": {
        "bg": "#12110f",
        "ink": "#e8e4dc",
        "muted": "#9a958c",
        "rule": "#c9a227",
        "mark_bg": "#1c1b18",
        "mark": "#e8e4dc",
    },
    "light": {
        "bg": "#f4f1ea",
        "ink": "#1a1916",
        "muted": "#5c5850",
        "rule": "#8a7018",
        "mark_bg": "#e7e2d6",
        "mark": "#1a1916",
    },
}

W, H = 1120, 280


def render(theme: str) -> str:
    c = THEMES[theme]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(NAME)}">
  <rect width="{W}" height="{H}" fill="{c['bg']}"/>
  <rect x="36" y="36" width="88" height="88" fill="{c['mark_bg']}"/>
  <text x="80" y="92" text-anchor="middle" fill="{c['mark']}" font-family="ui-serif, Georgia, serif" font-size="28" font-weight="600">MG</text>
  <line x1="148" y1="36" x2="148" y2="244" stroke="{c['rule']}" stroke-width="1"/>
  <text x="176" y="72" fill="{c['ink']}" font-family="ui-serif, Georgia, 'Times New Roman', serif" font-size="28" font-weight="600">{escape(NAME)}</text>
  <text x="176" y="102" fill="{c['muted']}" font-family="ui-sans-serif, system-ui, sans-serif" font-size="15">{escape(ROLE)} · {escape(HANDLE)}</text>
  <text x="176" y="138" fill="{c['ink']}" font-family="ui-sans-serif, system-ui, sans-serif" font-size="16">{escape(LINE)}</text>
  <text x="176" y="176" fill="{c['muted']}" font-family="ui-sans-serif, system-ui, sans-serif" font-size="14">{escape(FOCUS)}</text>
  <text x="176" y="202" fill="{c['ink']}" font-family="ui-sans-serif, system-ui, sans-serif" font-size="14">{escape(NOW)}</text>
  <text x="176" y="236" fill="{c['muted']}" font-family="ui-monospace, Consolas, monospace" font-size="13">{escape(STACK)}</text>
</svg>
"""


def main() -> None:
    out = Path(__file__).parent
    for name in THEMES:
        path = out / f"{name}.svg"
        path.write_text(render(name), encoding="utf-8")
        print(f"wrote {path.name}")


if __name__ == "__main__":
    main()
