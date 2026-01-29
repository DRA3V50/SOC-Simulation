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
run_id = now.strftime("%Y%m%d%H%M%S")

# =============================
# 1️⃣ CREATE TODAY'S TICKET
# =============================
ticket_path = TICKETS / f"{today}_{run_id}.json"

ticket_id_num = random.randint(1000, 9999)
ticket_id = f"SOC-INC{today.replace('-', '')}-{ticket_id_num}"

severity = random.choices(
    ["high", "medium", "low"],
    weights=[3, 4, 3]
)[0]

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
alert_path = ALERTS / f"{today}_{run_id}.json"

alert_id_num = random.randint(1000, 9999)
alert_id = f"ALERT-{today.replace('-', '')}-{alert_id_num}"

alert = {
    "alert_id": alert_id,
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
# 4️⃣ GENERATE SVG CHART (PROPORTIONAL)
# =============================
MAX_BAR_WIDTH = 160
BAR_START_X = 120
LABEL_X = 10

max_count = max(counts.values()) or 1

def w(c):
    return int((c / max_count) * MAX_BAR_WIDTH)

svg = f"""
<svg width="320" height="120" xmlns="http://www.w3.org/2000/svg">

  <!-- High -->
  <text x="{LABEL_X}" y="32" fill="red">High</text>
  <rect x="{BAR_START_X}" y="15" width="{w(counts['high'])}" height="25" fill="red"/>
  <text x="{BAR_START_X + w(counts['high']) + 5}" y="32" fill="red">{counts['high']}</text>

  <!-- Medium -->
  <text x="{LABEL_X}" y="67" fill="orange">Medium</text>
  <rect x="{BAR_START_X}" y="50" width="{w(counts['medium'])}" height="25" fill="orange"/>
  <text x="{BAR_START_X + w(counts['medium']) + 5}" y="67" fill="orange">{counts['medium']}</text>

  <!-- Low -->
  <text x="{LABEL_X}" y="102" fill="green">Low</text>
  <rect x="{BAR_START_X}" y="85" width="{w(counts['low'])}" height="25" fill="green"/>
  <text x="{BAR_START_X + w(counts['low']) + 5}" y="102" fill="green">{counts['low']}</text>

</svg>
"""

chart_path = CHARTS / "severity_chart.svg"
with open(chart_path, "w") as f:
    f.write(svg.strip())

# =============================
# 5️⃣ GENERATE README
# =============================
xp = counts["high"] * 10 + counts["medium"] * 5 + counts["low"] * 2
badge = f"https://img.shields.io/badge/XP:{xp}%20H:{counts['high']}%20M:{counts['medium']}%20L:{counts['low']}-blue"

readme = f"""
# 🛡️ SOC Detection & Incident Data Automation

![XP Badge]({badge})

## 📈 Alert Analytics

| Severity | Count |
|----------|-------|
| 🔴 High  | {counts['high']} |
| 🟠 Medium| {counts['medium']} |
| 🟢 Low   | {counts['low']} |

<img src="charts/severity_chart.svg" width="320" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
"""

for f in sorted(ALERTS.glob("*.json"), reverse=True)[:5]:
    a = json.load(open(f))
    sev = a["severity"]
    emoji = "🔴 High" if sev == "high" else "🟠 Medium" if sev == "medium" else "🟢 Low"
    readme += f"| {f.stem} | {a['ticket_id']} | {a['alert_id']} | {emoji} | {a['event']} |\n"

# =============================
# 6️⃣ DETECTION RULES
# =============================
readme += "\n## 🧰 Detection Rules\n\n"
readme += "| Rule ID | Name | Severity | Description |\n"
readme += "|---------|------|---------|-------------|\n"

for f in DETECTIONS.glob("*.yml"):
    with open(f) as yf:
        d = yaml.safe_load(yf)
        readme += f"| {d.get('rule_id')} | {d.get('name')} | {d.get('severity').capitalize()} | {d.get('description')} |\n"

# =============================
# 7️⃣ SAVE README
# =============================
with open(ROOT / "README.md", "w") as f:
    f.write(readme.strip())

print("✅ SOC daily simulation updated successfully")
