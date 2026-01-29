from pathlib import Path
import json
from datetime import datetime, timedelta
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
# 1️⃣ CREATE TICKET
# =============================
ticket_path = TICKETS / f"{today}_{run_id}.json"
ticket_id = f"SOC-INC{today.replace('-', '')}-{random.randint(1000,9999)}"
severity = random.choices(["high","medium","low"], weights=[3,4,3])[0]

ticket = {
    "ticket_id": ticket_id,
    "created": now.isoformat(),
    "severity": severity,
    "system": f"HOST-{random.randint(10,99)}",
    "event": f"Simulated SOC event ({severity})"
}

json.dump(ticket, open(ticket_path, "w"), indent=2)

# =============================
# 2️⃣ CREATE ALERT
# =============================
alert_path = ALERTS / f"{today}_{run_id}.json"
alert = {
    "alert_id": f"ALERT-{today.replace('-', '')}-{random.randint(1000,9999)}",
    "ticket_id": ticket["ticket_id"],
    "severity": severity,
    "event": ticket["event"],
    "timestamp": now.isoformat(),
    "system": ticket["system"]
}

json.dump(alert, open(alert_path, "w"), indent=2)

# =============================
# 3️⃣ COUNT SEVERITIES
# =============================
counts = {"high": 0, "medium": 0, "low": 0}
for f in ALERTS.glob("*.json"):
    a = json.load(open(f))
    counts[a["severity"]] += 1

# =============================
# 3a️⃣ ALERT VELOCITY
# =============================
last_24h = now - timedelta(hours=24)
alerts_24h = 0
alerts_total = 0

for f in ALERTS.glob("*.json"):
    a = json.load(open(f))
    alerts_total += 1
    if datetime.fromisoformat(a["timestamp"]) >= last_24h:
        alerts_24h += 1

# =============================
# 4️⃣ SVG CHART (COLOR FIXED)
# =============================
MAX_BAR_WIDTH = 160
BAR_START_X = 120
LABEL_X = 10
max_count = max(counts.values()) or 1
w = lambda c: int((c / max_count) * MAX_BAR_WIDTH)

svg = f"""
<svg width="320" height="120" xmlns="http://www.w3.org/2000/svg">

  <text x="{LABEL_X}" y="32" fill="red">High</text>
  <rect x="{BAR_START_X}" y="15" width="{w(counts['high'])}" height="25" fill="red"/>
  <text x="{BAR_START_X + w(counts['high']) + 5}" y="32" fill="red">{counts['high']}</text>

  <text x="{LABEL_X}" y="67" fill="orange">Medium</text>
  <rect x="{BAR_START_X}" y="50" width="{w(counts['medium'])}" height="25" fill="orange"/>
  <text x="{BAR_START_X + w(counts['medium']) + 5}" y="67" fill="orange">{counts['medium']}</text>

  <text x="{LABEL_X}" y="102" fill="green">Low</text>
  <rect x="{BAR_START_X}" y="85" width="{w(counts['low'])}" height="25" fill="green"/>
  <text x="{BAR_START_X + w(counts['low']) + 5}" y="102" fill="green">{counts['low']}</text>

</svg>
"""

(CHARTS / "severity_chart.svg").write_text(svg.strip())

# =============================
# 5️⃣ README
# =============================
xp = counts["high"]*10 + counts["medium"]*5 + counts["low"]*2
badge = f"https://img.shields.io/badge/XP:{xp}%20H:{counts['high']}%20M:{counts['medium']}%20L:{counts['low']}-blue"

readme = f"""
# 🛡️ SOC Detection & Incident Data Automation

![XP Badge]({badge})

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?{run_id}" width="320" />
"""

# =============================
# 5a️⃣ SIDE-BY-SIDE TABLES (3)
# =============================
total = sum(counts.values()) or 1

counts_tbl = "| Severity | Count |\n|---|---|\n"
perc_tbl = "| Severity | Count | % |\n|---|---|---|\n"

for sev in ["high","medium","low"]:
    emoji = "🔴 High" if sev=="high" else "🟠 Medium" if sev=="medium" else "🟢 Low"
    counts_tbl += f"| {emoji} | {counts[sev]} |\n"
    perc_tbl += f"| {emoji} | {counts[sev]} | {round((counts[sev]/total)*100)}% |\n"

velocity_tbl = f"""| Window | Alerts |
|---|---|
| Last 24 Hours | {alerts_24h} |
| All Time | {alerts_total} |
"""

readme += f"""
<table>
<tr>
<td>

**Severity Counts**

{counts_tbl}

</td>
<td>

**Severity % of Total**

{perc_tbl}

</td>
<td>

**Alert Velocity**

{velocity_tbl}

</td>
</tr>
</table>
"""

# =============================
# 5b️⃣ RECENT ALERTS
# =============================
readme += "\n## 🎟️ Recent Alerts\n| Date | Ticket | Alert | Severity | Event |\n|---|---|---|---|---|\n"
for f in sorted(ALERTS.glob("*.json"), reverse=True)[:5]:
    a = json.load(open(f))
    sev = "🔴 High" if a["severity"]=="high" else "🟠 Medium" if a["severity"]=="medium" else "🟢 Low"
    readme += f"| {f.stem} | {a['ticket_id']} | {a['alert_id']} | {sev} | {a['event']} |\n"

# =============================
# 5c️⃣ TOP HOSTS
# =============================
hosts = {}
for f in ALERTS.glob("*.json"):
    a = json.load(open(f))
    h = a.get("system","UNKNOWN_HOST")
    hosts[h] = hosts.get(h,0)+1

readme += "\n## 🖥️ Top 5 Hosts by Alerts\n| Host | Count |\n|---|---|\n"
for h,c in sorted(hosts.items(), key=lambda x:x[1], reverse=True)[:5]:
    readme += f"| {h} | {c} |\n"

# =============================
# 6️⃣ DETECTION RULES
# =============================
readme += "\n## 🧰 Detection Rules\n| Rule ID | Name | Severity | Description |\n|---|---|---|---|\n"
for f in DETECTIONS.glob("*.yml"):
    d = yaml.safe_load(open(f))
    readme += f"| {d.get('rule_id')} | {d.get('name')} | {d.get('severity').capitalize()} | {d.get('description')} |\n"

(ROOT / "README.md").write_text(readme.strip())
print("✅ SOC daily simulation updated successfully")
