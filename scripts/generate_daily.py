from pathlib import Path
import json
import random
from datetime import datetime
from zoneinfo import ZoneInfo
import yaml

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
# LOAD DETECTION RULES
# =============================
rules = []
for rule_file in DETECTIONS.glob("*.yml"):
    with open(rule_file, "r") as f:
        rules.append(yaml.safe_load(f))

rule = random.choice(rules) if rules else None

# =============================
# DETECTION TRIGGER
# =============================
triggered = random.choice([True, False])
severity = rule["severity"] if triggered and rule else "low"

# =============================
# INCIDENT LIFECYCLE
# =============================
lifecycle = ["New", "In Progress", "Contained", "Resolved"]
status = random.choice(lifecycle)

# =============================
# HOST / IDS
# =============================
host = f"HOST-{random.randint(10,99)}"
ticket_id = f"SOC-INC{now.strftime('%Y%m%d')}-{random.randint(1000,9999)}"
alert_id = f"ALERT-{today}-{random.randint(1000,9999)}"

# =============================
# CREATE TICKET (ServiceNow / Jira style)
# =============================
ticket = {
    "ticket_id": ticket_id,
    "created": now.isoformat(),
    "severity": severity,
    "status": status,
    "host": host,
    "summary": rule["name"] if triggered and rule else "Low-risk security event",
    "source": "SIEM"
}

with open(TICKETS / f"{today}.json", "w") as f:
    json.dump(ticket, f, indent=2)

# =============================
# CREATE ALERT
# =============================
alert = {
    "alert_id": alert_id,
    "ticket_id": ticket_id,
    "severity": severity,
    "host": host,
    "rule_id": rule["rule_id"] if triggered and rule else None,
    "timestamp": now.isoformat()
}

with open(ALERTS / f"{today}.json", "w") as f:
    json.dump(alert, f, indent=2)

# =============================
# ALERT CORRELATION
# =============================
incident_key = f"{host}-{severity}"
incident_id = f"INC-GRP-{abs(hash(incident_key)) % 10000}"

correlation = {
    "incident_id": incident_id,
    "host": host,
    "severity": severity,
    "alerts": [alert_id],
    "status": status
}

with open(CORRELATIONS / f"{today}.json", "w") as f:
    json.dump(correlation, f, indent=2)

# =============================
# COUNT SEVERITIES
# =============================
counts = {"high": 0, "medium": 0, "low": 0}
for f in ALERTS.glob("*.json"):
    a = json.load(open(f))
    counts[a["severity"]] += 1

# =============================
# GENERATE SVG CHART
# =============================
def bar_width(c):
    return max(c * 30, 10)

svg = f"""
<svg width="320" height="120" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="15" width="{bar_width(counts['high'])}" height="20" fill="red"/>
  <text x="170" y="30" fill="red">High ({counts['high']})</text>

  <rect x="10" y="50" width="{bar_width(counts['medium'])}" height="20" fill="orange"/>
  <text x="170" y="65" fill="orange">Medium ({counts['medium']})</text>

  <rect x="10" y="85" width="{bar_width(counts['low'])}" height="20" fill="green"/>
  <text x="170" y="100" fill="green">Low ({counts['low']})</text>
</svg>
"""

with open(CHARTS / "severity_chart.svg", "w") as f:
    f.write(svg.strip())

print("✅ SOC detection, lifecycle, and correlation automation complete.")

