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

ticket = {
    "ticket_id": f"TICKET-{today}",
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

alert = {
    "alert_id": f"ALERT-{today}",
    "ticket_id": ticket["ticket_id"],
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
README = ROOT / "README.md"

# XP calculation for badge
xp = counts["high"]*10 + counts["medium"]*5 + counts["low"]*2
badge = f"https://img.shields.io/badge/XP:{xp}%20H:{counts['high']}%20M:{counts['medium']}%20L:{counts['low']}-blue"

# Generate dynamic content
dynamic_content = f"""
<!-- DYNAMIC-START -->
![XP Badge]({badge})

## 📈 Alert Snapshot

| Severity | Count |
|----------|-------|
| 🔴 High  | {counts['high']}     |
| 🟠 Medium| {counts['medium']}     |
| 🟢 Low   | {counts['low']}     |

**📊 Severity Chart**

<img src="charts/severity_chart.svg" width="320" height="120" />

**🎟️ Recent Tickets / Alerts**

| Date       | Ticket 🎟️ | Alert 🚨 | Severity | Event |
|------------|-----------|----------|----------|-------|
"""

for f in sorted(ALERTS.glob("*.json"), reverse=True)[:5]:
    a = json.load(open(f))
    dynamic_content += f"| {f.stem} | {a['ticket_id']} | {a['alert_id']} | {a['severity'].capitalize()} | {a['event']} |\n"

dynamic_content += "<!-- DYNAMIC-END -->"

# Read existing README
if README.exists():
    content = README.read_text()
    if "<!-- DYNAMIC-START -->" in content and "<!-- DYNAMIC-END -->" in content:
        pre = content.split("<!-- DYNAMIC-START -->")[0]
        post = content.split("<!-- DYNAMIC-END -->")[1]
        new_content = pre + dynamic_content + post
    else:
        # If markers missing, append at end
        new_content = content.strip() + "\n\n" + dynamic_content
else:
    # If README does not exist, create from scratch
    new_content = dynamic_content

with open(README, "w") as f:
    f.write(new_content.strip())

print("✅ SOC daily simulation updated (dynamic section only).")

