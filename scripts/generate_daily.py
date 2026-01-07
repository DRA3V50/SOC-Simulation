from pathlib import Path
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import random
import yaml

# =============================
# PATHS
# =============================
ROOT = Path(__file__).parent.parent
ALERTS = ROOT / "alerts"
TICKETS = ROOT / "tickets"
CHARTS = ROOT / "charts"
PLAYBOOKS = ROOT / "playbooks"
DETECTIONS = ROOT / "detections"
CORRELATIONS = ROOT / "correlations"

for d in [ALERTS, TICKETS, CHARTS, PLAYBOOKS, DETECTIONS, CORRELATIONS]:
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
    "ticket_id": f"SOC-INC{today.replace('-', '')}-{random.randint(1000,9999)}",
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
    "alert_id": f"ALERT-{today}-{random.randint(1000,9999)}",
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
# 5️⃣ BUILD README
# =============================
xp = counts["high"]*10 + counts["medium"]*5 + counts["low"]*2
badge = f"https://img.shields.io/badge/XP:{xp}%20H:{counts['high']}%20M:{counts['medium']}%20L:{counts['low']}-blue"

readme = f"""
# 🛡️ SOC Detection & Incident Data Automation

![XP Badge]({badge})

⚡ Simulates a professional Security Operations Center workflow with automated ticketing using 🎟️ Jira and ServiceNow, alert escalation 🚨 based on severity, and data-driven analytics 📊 for SIEM, SOAR, and incident response.

## 🔹 Project Focus
🎟️ Automated Ticketing & Alerts – Generates daily tickets in Jira/ServiceNow format and simulates real incident intake.
🚨 Escalation & Prioritization – Automatically classifies alerts High 🔴 / Medium 🟠 / Low 🟢 for analyst prioritization.
📈 Analytics & Visualization – Counts alerts, calculates XP points, and generates severity charts 📊.
🔍 Data Analysis – Identifies patterns, recurring issues, and prioritizes incidents.
⚙️ Automation – Fully automated via GitHub Actions to simulate daily SOC activity.
🔍 Detection and Incident Correlation
📐 SIEM Detection Rules – Structured detection rules identify suspicious activity.
🔄 Incident Lifecycle Tracking – Tracks events from detection to resolution.
🔗 Alert Correlation – Groups related alerts into single incidents to reduce noise.

## 📊 Alert Analytics
Severity Distribution

| Severity | Count |
|----------|-------|
| 🔴 High  | {counts['high']} |
| 🟠 Medium| {counts['medium']} |
| 🟢 Low   | {counts['low']} |

## 📈 Chart Display
<img src="charts/severity_chart.svg" width="320" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
"""

# Add recent alerts
for f in sorted(ALERTS.glob("*.json"), reverse=True)[:5]:
    a = json.load(open(f))
    sev_icon = "🔴" if a["severity"]=="high" else "🟠" if a["severity"]=="medium" else "🟢"
    readme += f"| {f.stem} | {a['ticket_id']} | {a['alert_id']} | {sev_icon} {a['severity'].capitalize()} | {a['event']} |\n"

# =============================
# 6️⃣ ADD DETECTION RULES
# =============================
readme += "\n## 🧰 Detection Rules\n\n"
readme += "| Rule ID | Name | Severity | Description |\n"
readme += "|---------|------|---------|-------------|\n"

for f in sorted(DETECTIONS.glob("*.yml")):
    rule = yaml.safe_load(open(f))
    readme += f"| {rule['rule_id']} | {rule['name']} | {rule['severity'].capitalize()} | {rule['description']} |\n"

# =============================
# WRITE README
# =============================
with open(ROOT / "README.md", "w") as f:
    f.write(readme.strip())

print("✅ SOC daily simulation completed with detections")


