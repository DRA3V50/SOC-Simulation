from pathlib import Path
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import random

# =============================
# PATHS
# =============================
ROOT = Path(__file__).parent.parent
ALERTS = ROOT / "alerts"
TICKETS = ROOT / "tickets"
CHARTS = ROOT / "charts"
PLAYBOOKS = ROOT / "playbooks"

for d in [ALERTS, TICKETS, CHARTS, PLAYBOOKS]:
    d.mkdir(exist_ok=True)

# =============================
# TIME (EST)
# =============================
now = datetime.now(ZoneInfo("America/New_York"))
today = now.strftime("%Y-%m-%d")

# =============================
# 1️⃣ CREATE TODAY'S TICKET
# =============================
ticket_path = TICKETS / f"{today}.json"

severity = random.choices(
    ["high", "medium", "low"],
    weights=[3, 4, 3]
)[0]

# ✅ Hybrid Jira + ServiceNow style
ticket_id = f"SOC-INC{now.strftime('%Y%m%d')}-{random.randint(1000,9999)}"

ticket = {
    "ticket_id": ticket_id,
    "created": now.isoformat(),
    "severity": severity,
    "system": f"HOST-{random.randint(10,99)}",
    "event": f"Simulated SOC event ({severity})"
}

with open(ticket_path, "w") as f:
    json.dump(ticket, f, indent=2)

# =============================
# 2️⃣ CREATE ALERT
# =============================
alert_path = ALERTS / f"{today}.json"

# Make alert ID unique
alert_id = f"ALERT-{today}-{random.randint(1000,9999)}"

alert = {
    "alert_id": alert_id,
    "ticket_id": ticket_id,
    "severity": severity,
    "event": ticket["event"],
    "timestamp": now.isoformat()
}

with open(alert_path, "w") as f:
    json.dump(alert, f, indent=2)

# =============================
# 3️⃣ COUNT SEVERITIES
# =============================
counts = {"high": 0, "medium": 0, "low": 0}

for f in ALERTS.glob("*.json"):
    with open(f) as jf:
        a = json.load(jf)
    counts[a["severity"]] += 1

# =============================
# 4️⃣ GENERATE SVG CHART
# =============================
def w(c): 
    return max(c * 30, 10)

svg = f"""
<svg width="320" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="15" width="{w(counts['high'])}" height="20" fill="red"/>
  <text x="{15 + w(counts['high'])}" y="30" fill="red">High ({counts['high']})</text>

  <rect x="10" y="50" width="{w(counts['medium'])}" height="20" fill="orange"/>
  <text x="{15 + w(counts['medium'])}" y="65" fill="orange">Medium ({counts['medium']})</text>

  <rect x="10" y="85" width="{w(counts['low'])}" height="20" fill="green"/>
  <text x="{15 + w(counts['low'])}" y="100" fill="green">Low ({counts['low']})</text>
</svg>
"""

chart_path = CHARTS / "severity_chart.svg"
with open(chart_path, "w") as f:
    f.write(svg.strip())

# =============================
# 5️⃣ UPDATE README (DYNAMIC SECTION ONLY)
# =============================
xp = counts["high"]*10 + counts["medium"]*5 + counts["low"]*2
badge = f"https://img.shields.io/badge/XP:{xp}%20H:{counts['high']}%20M:{counts['medium']}%20L:{counts['low']}-blue"

readme_path = ROOT / "README.md"

# Read current README
with open(readme_path, "r") as f:
    lines = f.readlines()

# Split into static & dynamic
start_idx = 0
end_idx = len(lines)
for i, line in enumerate(lines):
    if line.startswith("## 🎟️ Recent Tickets / Alerts"):
        start_idx = i
        break

# Keep static lines, replace everything from 'Recent Tickets / Alerts' onwards
readme_static = lines[:start_idx]

dynamic_section = [
    "## 🎟️ Recent Tickets / Alerts\n\n",
    "| Date       | Ticket ID 🎟️   | Alert ID 🚨        | Severity | Event                       |\n",
    "|------------|----------------|------------------|----------|-----------------------------|\n"
]

# Add latest 5 tickets/alerts (most recent first)
for f in sorted(ALERTS.glob("*.json"), reverse=True)[:5]:
    a = json.load(open(f))
    t = json.load(open(TICKETS / f"{f.stem}.json"))
    dynamic_section.append(
        f"| {f.stem} | {t['ticket_id']} | {a['alert_id']} | "
        f"{'🔴 High' if a['severity']=='high' else '🟠 Medium' if a['severity']=='medium' else '🟢 Low'} | {a['event']} |\n"
    )

# Write back updated README
with open(readme_path, "w") as f:
    f.writelines(readme_static + dynamic_section)

print("✅ SOC daily simulation completed with hybrid ticketing!")

