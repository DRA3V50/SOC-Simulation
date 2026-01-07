from pathlib import Path
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import random
import re

# =============================
# PATHS
# =============================
ROOT = Path(__file__).parent.parent
ALERTS = ROOT / "alerts"
TICKETS = ROOT / "tickets"
CHARTS = ROOT / "charts"
DETECTIONS = ROOT / "detections"
CORRELATIONS = ROOT / "correlations"

for d in [ALERTS, TICKETS, CHARTS, DETECTIONS, CORRELATIONS]:
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

# Simulate Jira/ServiceNow style ticket ID
ticket_id_prefix = "SOC-INC"  # Example: SOC-INC20260107-5360
ticket_id_suffix = random.randint(1000, 9999)
ticket_id = f"{ticket_id_prefix}{today.replace('-', '')}-{ticket_id_suffix}"

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

alert_id_suffix = random.randint(1000, 9999)
alert = {
    "alert_id": f"ALERT-{today}-{alert_id_suffix}",
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
# 5️⃣ UPDATE README WITHOUT OVERWRITING STATIC SECTIONS
# =============================
readme_path = ROOT / "README.md"

with open(readme_path, "r") as f:
    readme_content = f.read()

# Update XP badge
xp = counts["high"]*10 + counts["medium"]*5 + counts["low"]*2
badge_pattern = r"!\[XP Badge\]\(https://img\.shields\.io/badge/XP:[^\)]+\)"
badge_new = f"![XP Badge](https://img.shields.io/badge/XP:{xp}%20H:{counts['high']}%20M:{counts['medium']}%20L:{counts['low']}-blue)"
readme_content = re.sub(badge_pattern, badge_new, readme_content)

# Update Severity Table
severity_pattern = r"(\| Severity \| Count \|[\s\S]*?)\n##"
severity_table = f"""| Severity | Count |
|----------|-------|
| 🔴 High  | {counts['high']} |
| 🟠 Medium| {counts['medium']} |
| 🟢 Low   | {counts['low']} |
"""
readme_content = re.sub(r"\| Severity \| Count \|[\s\S]*?\n##", severity_table + "\n\n##", readme_content)

# Update Recent Tickets Table (keep top 5 latest)
recent_alerts = sorted(ALERTS.glob("*.json"), reverse=True)[:5]
tickets_table = "| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |\n"
tickets_table += "|------|---------------|------------|---------|-------|\n"
for f in recent_alerts:
    a = json.load(open(f))
    sev_emoji = "🔴" if a["severity"]=="high" else "🟠" if a["severity"]=="medium" else "🟢"
    tickets_table += f"| {f.stem} | {a['ticket_id']} | {a['alert_id']} | {sev_emoji} {a['severity'].capitalize()} | {a['event']} |\n"

readme_content = re.sub(r"\| Date \| Ticket ID 🎟️ \| Alert ID 🚨 \| Severity \| Event \|[\s\S]*?\n## 🧰 Detection Rules", tickets_table + "\n\n## 🧰 Detection Rules", readme_content)

with open(readme_path, "w") as f:
    f.write(readme_content)

print("✅ SOC daily simulation completed without overwriting static sections")


