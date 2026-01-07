from pathlib import Path
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import random

# -----------------------------
# Paths
# -----------------------------
BASE_DIR = Path(__file__).parent.parent
alerts_folder = BASE_DIR / "alerts"
tickets_folder = BASE_DIR / "tickets"
playbooks_folder = BASE_DIR / "playbooks"
charts_folder = BASE_DIR / "charts"

# Make sure folders exist
alerts_folder.mkdir(exist_ok=True)
tickets_folder.mkdir(exist_ok=True)
playbooks_folder.mkdir(exist_ok=True)
charts_folder.mkdir(exist_ok=True)

# -----------------------------
# Current date
# -----------------------------
today_str = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")

# -----------------------------
# 1️⃣ Generate random ticket
# -----------------------------
ticket_path = tickets_folder / f"{today_str}.json"
if not ticket_path.exists():
    severity = random.choices(["high", "medium", "low"], weights=[2,3,5])[0]
    ticket = {
        "ticket_id": f"TICKET-{today_str}",
        "host": f"HOST-{random.randint(1,100)}",
        "user": f"user{random.randint(1,50)}",
        "process": random.choice(["powershell.exe","cmd.exe","explorer.exe"]),
        "timestamp": datetime.now(ZoneInfo("America/New_York")).isoformat(),
        "event": f"Simulated suspicious activity ({severity})",
        "severity": severity
    }
    with open(ticket_path, "w") as f:
        json.dump(ticket, f, indent=2)

# -----------------------------
# 2️⃣ Generate alert
# -----------------------------
alert_path = alerts_folder / f"{today_str}.json"
if not alert_path.exists():
    with open(ticket_path) as f:
        ticket_data = json.load(f)
    alert = {
        "alert_id": f"ALERT-{today_str}",
        "ticket_id": ticket_data["ticket_id"],
        "host": ticket_data["host"],
        "user": ticket_data["user"],
        "process": ticket_data["process"],
        "timestamp": ticket_data["timestamp"],
        "event": ticket_data["event"],
        "severity": ticket_data["severity"]
    }
    with open(alert_path, "w") as f:
        json.dump(alert, f, indent=2)

# -----------------------------
# 3️⃣ Generate playbook
# -----------------------------
playbook_path = playbooks_folder / f"{today_str}_playbook.yml"
if not playbook_path.exists():
    playbook_content = f"""
playbook:
  id: PB-{today_str}
  linked_ticket: TICKET-{today_str}
  severity: {ticket['severity']}
procedure:
  - step: 1
    action: isolate_host
  - step: 2
    action: collect_process_tree
  - step: 3
    action: memory_snapshot
  - step: 4
    action: analyst_review
decision:
  if_malicious:
    - escalate_to_ir
    - open_incident
  else:
    - close_ticket
"""
    with open(playbook_path, "w") as f:
        f.write(playbook_content.strip())

# -----------------------------
# 4️⃣ Count tickets by severity
# -----------------------------
all_alerts = list(alerts_folder.glob("*.json"))
severity_counts = {"high":0, "medium":0, "low":0}

for alert_file in all_alerts:
    with open(alert_file) as f:
        a = json.load(f)
    sev = a.get("severity", "low")
    severity_counts[sev] += 1

# -----------------------------
# 5️⃣ Generate SVG chart
# -----------------------------
def bar_width(count):
    return max(count*20, 10)

svg = f"""<svg width="300" height="100" xmlns="http://www.w3.org/2000/svg">
  {'<rect x="10" y="10" width="'+str(bar_width(severity_counts['high']))+'" height="20" fill="red"/><text x="'+str(10+bar_width(severity_counts['high'])+5)+'" y="25" font-size="12" fill="red">High</text>' if severity_counts['high']>0 else ''}
  {'<rect x="10" y="40" width="'+str(bar_width(severity_counts['medium']))+'" height="20" fill="orange"/><text x="'+str(10+bar_width(severity_counts['medium'])+5)+'" y="55" font-size="12" fill="orange">Medium</text>' if severity_counts['medium']>0 else ''}
  {'<rect x="10" y="70" width="'+str(bar_width(severity_counts['low']))+'" height="20" fill="green"/><text x="'+str(10+bar_width(severity_counts['low'])+5)+'" y="85" font-size="12" fill="green">Low</text>' if severity_counts['low']>0 else ''}
</svg>"""

chart_path = charts_folder / "severity_chart.svg"
with open(chart_path, "w") as f:
    f.write(svg)

# -----------------------------
# 6️⃣ Update README
# -----------------------------
total_xp = severity_counts['high']*10 + severity_counts['medium']*5 + severity_counts['low']*2
badge_url = f"https://img.shields.io/badge/XP%3A{total_xp}%20%7C%20H%3A{severity_counts['high']}%20M%3A{severity_counts['medium']}%20L%3A{severity_counts['low']}-blue"

dashboard = f"![XP Badge]({badge_url})\n\n"
dashboard += "# SOC Automation & Data Analytics Simulation\n\n"
dashboard += "> Simulated SOC workflow: alert → ticket → playbook → analyst/IR decision → XP scoring\n\n"
dashboard += "### 📊 Alert Severity Distribution\n"
dashboard += svg + "\n\n"

dashboard += "### 🚨 Recent Alerts\n"
dashboard += "| Date | Alert ID | Severity | Event |\n"
dashboard += "|------|---------|---------|-------|\n"
for alert_file in sorted(all_alerts, reverse=True)[-5:]:
    with open(alert_file) as f:
        a = json.load(f)
    dashboard += f"| {alert_file.stem} | ALERT-{alert_file.stem} | {a['severity'].capitalize()} | {a['event']} |\n"

with open(BASE_DIR / "README.md", "w") as f:
    f.write(dashboard)

print("Daily SOC simulation complete!")
