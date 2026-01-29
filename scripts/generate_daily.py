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
system_host = f"HOST-{random.randint(10,99)}"

ticket = {
    "ticket_id": ticket_id,
    "created": now.isoformat(),
    "severity": severity,
    "system": system_host,
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

total_alerts = sum(counts.values()) or 1

# =============================
# 3a️⃣ ALERT VELOCITY
# =============================
last_24h = now - timedelta(hours=24)
alerts_24h = 0
for f in ALERTS.glob("*.json"):
    a = json.load(open(f))
    if datetime.fromisoformat(a["timestamp"]) >= last_24h:
        alerts_24h += 1

# =============================
# 4️⃣ SVG CHART
# =============================
MAX_BAR_WIDTH = 160
BAR_START_X = 120
LABEL_X = 10
max_count = max(counts.values()) or 1
w = lambda c: int((c / max_count) * MAX_BAR_WIDTH)

svg = f"""
<svg width="320" height="120" xmlns="http://www.w3.org/2000/svg">

  <text x="{LABEL_X}" y="32" style="fill:red;">High</text>
  <rect x="{BAR_START_X}" y="15" width="{w(counts['high'])}" height="25" fill="red"/>
  <text x="{BAR_START_X + w(counts['high']) + 5}" y="32"
        style="fill:red; font-weight:bold;">{counts['high']}</text>

  <text x="{LABEL_X}" y="67" style="fill:orange;">Medium</text>
  <rect x="{BAR_START_X}" y="50" width="{w(counts['medium'])}" height="25" fill="orange"/>
  <text x="{BAR_START_X + w(counts['medium']) + 5}" y="67"
        style="fill:orange; font-weight:bold;">{counts['medium']}</text>

  <text x="{LABEL_X}" y="102" style="fill:green;">Low</text>
  <rect x="{BAR_START_X}" y="85" width="{w(counts['low'])}" height="25" fill="green"/>
  <text x="{BAR_START_X + w(counts['low']) + 5}" y="102"
        style="fill:green; font-weight:bold;">{counts['low']}</text>

</svg>
"""

(CHARTS / "severity_chart.svg").write_text(svg.strip())

# =============================
# 5️⃣ README
# =============================
xp = counts["high"]*10 + counts["medium"]*5 + counts["low"]*2
badge = f"https://img.shields.io/badge/XP:{xp}%20H:{counts['high']}%20M:{counts['medium']}%20L:{counts['low']}-blue"

readme = f"""
# 🛡️ SOC Detection & Incident Automation

![XP Badge]({badge})

---

## 🔹 About This Repository

This repository simulates a **modern Security Operations Center (SOC)** workflow, providing realistic alerting, ticketing, and incident tracking data. It is designed for:

- **SOC Training & Demonstrations** – simulate realistic alert flow for analysts.
- **Automation Testing** – experiment with alert generation, incident correlation, and data-driven dashboards.
- **Data Analytics & Visualization** – produce charts and tables for reporting KPIs.
- **Integration with SIEM/SOAR Tools** – practice automated ticket creation, alert prioritization, and response simulation.

The system **automatically generates alerts and tickets**, tracks their **severity**, calculates **alert velocity**, and identifies the **most frequently triggered hosts**, providing a full end-to-end workflow experience.

---

## 📊 Dashboard Overview

<img src="charts/severity_chart.svg?{run_id}" width="320" />
"""

# =============================
# Helper to make HTML tables with color
# =============================
def make_html_table(title, headers, rows, colors=None):
    html = f"<b>{title}</b><br>"
    html += "<table border='1' cellpadding='5' cellspacing='0'>"
    html += "<tr>" + "".join([f"<th>{h}</th>" for h in headers]) + "</tr>"
    for i, r in enumerate(rows):
        html += "<tr>"
        for j, c in enumerate(r):
            color = f" style='color:{colors[j]}'" if colors and j==1 else ""  # only color count column
            html += f"<td{color}>{c}</td>"
        html += "</tr>"
    html += "</table>"
    return html

# =============================
# Build tables
# =============================

# Severity Overview
sev_rows = []
sev_colors = []
for sev in ["high","medium","low"]:
    pct = round((counts[sev]/total_alerts)*100)
    sev_rows.append([
        "🔴 High" if sev=="high" else "🟠 Medium" if sev=="medium" else "🟢 Low",
        counts[sev],
        f"{pct}%"
    ])
    sev_colors.append("red" if sev=="high" else "orange" if sev=="medium" else "green")

sev_table_html = make_html_table("Severity Overview", ["Severity","Count","% of Total"], sev_rows, sev_colors)

# Alert Velocity
vel_rows = [
    ["Last 24 Hours", alerts_24h],
    ["All Time", total_alerts]
]
vel_table_html = make_html_table("Alert Velocity", ["Window","Alerts"], vel_rows)

# Top Hosts
hosts = {}
for f in ALERTS.glob("*.json"):
    a = json.load(open(f))
    h = a.get("system")
    if not h:
        continue
    hosts[h] = hosts.get(h,0)+1

top_rows = []
for h,c in sorted(hosts.items(), key=lambda x:x[1], reverse=True)[:5]:
    top_rows.append([h, c])

top_table_html = make_html_table("Top 5 Hosts", ["Host","Count"], top_rows)

# =============================
# Layout: 3 tables side by side (Velocity & Hosts swapped)
# =============================
readme += "<table><tr>"
readme += f"<td valign='top'>{sev_table_html}</td>"      # Severity Overview first
readme += f"<td valign='top'>{top_table_html}</td>"      # Top Hosts second
readme += f"<td valign='top'>{vel_table_html}</td>"      # Alert Velocity third
readme += "</tr></table>\n"

# =============================
# Recent Alerts (Markdown table)
# =============================
readme += "\n## 🎟️ Recent Alerts\n\n"
readme += "| Date | Ticket | Alert | Severity | Event |\n"
readme += "|------|--------|-------|---------|-------|\n"
for f in sorted(ALERTS.glob("*.json"), reverse=True)[:5]:
    a = json.load(open(f))
    sev_text = f"<span style='color:red'>🔴 High</span>" if a["severity"]=="high" else \
               f"<span style='color:orange'>🟠 Medium</span>" if a["severity"]=="medium" else \
               f"<span style='color:green'>🟢 Low</span>"
    event_text = a['event'].replace("|", "\\|")
    readme += f"| {f.stem} | {a['ticket_id']} | {a['alert_id']} | {sev_text} | {event_text} |\n"

# =============================
# Detection Rules
# =============================
readme += "\n## 🧰 Detection Rules\n\n"
readme += "| Rule ID | Name | Severity | Description |\n|---|---|---|---|\n"
for f in DETECTIONS.glob("*.yml"):
    d = yaml.safe_load(open(f))
    readme += f"| {d.get('rule_id')} | {d.get('name')} | {d.get('severity').capitalize()} | {d.get('description')} |\n"

(ROOT / "README.md").write_text(readme.strip())
print("✅ SOC daily simulation updated successfully")
