from pathlib import Path
import json
from datetime import datetime
from zoneinfo import ZoneInfo
import random
import yaml

# -----------------------------
# 0️⃣ Paths
# -----------------------------
BASE_DIR = Path(__file__).parent.parent
alerts_folder = BASE_DIR / "alerts"
tickets_folder = BASE_DIR / "tickets"
charts_folder = BASE_DIR / "charts"
playbooks_folder = BASE_DIR / "playbooks"

for folder in [alerts_folder, tickets_folder, charts_folder, playbooks_folder]:
    folder.mkdir(exist_ok=True)

# -----------------------------
# 1️⃣ EST timestamp
# -----------------------------
def now_est_iso():
    now_utc = datetime.utcnow()
    now_est = now_utc.replace(tzinfo=ZoneInfo("UTC")).astimezone(ZoneInfo("America/New_York"))
    return now_est.isoformat()

# -----------------------------
# 2️⃣ Generate today's alert
# -----------------------------
today_str = datetime.now(ZoneInfo("America/New_York")).strftime("%Y-%m-%d")
alert_path = alerts_folder / f"{today_str}.json"
ticket_path = tickets_folder / f"{today_str}.json"

severity_levels = ["high", "medium", "low"]
# Randomly simulate alert
alert_severity = random.choices(severity_levels, weights=[2,3,5])[0]

alert_data = {
    "alert_id": f"ALERT-{today_str}",
    "ticket_id": f"TICKET-{today_str}",
    "host": f"DESKTOP-{random.randint(1,99):02}",
    "user": "john.doe",
    "process": "powershell.exe",
    "timestamp": now_est_iso(),
    "event": f"Simulated suspicious activity ({alert_severity})",
    "severity": alert_severity,
    "mitre": {
        "tactic": "Execution",
        "technique_id": "T1059.001",
        "technique_name": "PowerShell"
    }
}

if not alert_path.exists():
    with open(alert_path, "w") as f:
        json.dump(alert_data, f, indent=2)

if not ticket_path.exists():
    with open(ticket_path, "w") as f:
        json.dump(alert_data, f, indent=2)

# -----------------------------
# 3️⃣ Generate Playbook
# -----------------------------
playbook_path = playbooks_folder / f"{today_str}_playbook.yml"
playbook_content = {
    "playbook": {
        "id": f"PB-{today_str}",
        "name": "Automated IR Playbook",
        "linked_alert": f"ALERT-{today_str}",
        "linked_ticket": f"TICKET-{today_str}",
        "severity": alert_severity
    },
    "procedure": [
        {"step": 1, "action": "isolate_host", "description": "Isolate endpoint from network"},
        {"step": 2, "action": "collect_process_tree", "description": "Collect parent-child processes"},
        {"step": 3, "action": "memory_snapshot", "description": "Capture memory for forensic review"},
        {"step": 4, "action": "analyst_review", "description": "SOC analyst validates malicious behavior"}
    ],
    "decision": {
        "if_malicious": ["escalate_to_ir", "open_incident"],
        "else": ["close_ticket"]
    }
}

if not playbook_path.exists():
    with open(playbook_path, "w") as f:
        yaml.dump(playbook_content, f)

# -----------------------------
# 4️⃣ Aggregate counts
# -----------------------------
severity_count = {"high":0, "medium":0, "low":0}
for alert_file in alerts_folder.glob("*.json"):
    with open(alert_file) as f:
        alert = json.load(f)
    sev = alert.get("severity","low").lower()
    severity_count[sev] += 1

# -----------------------------
# 5️⃣ Generate SVG chart
# -----------------------------
def bar_width(count):
    return max(count*20, 10)

svg_content = f"""<svg width="300" height="100" xmlns="http://www.w3.org/2000/svg">
  {'<rect x="10" y="10" width="'+str(bar_width(severity_count['high']))+'" height="20" fill="red"/>' 
   + '<text x="'+str(10 + bar_width(severity_count['high']) + 5)+'" y="25" font-size="12" fill="red">High</text>' if severity_count['high']>0 else ''}
  {'<rect x="10" y="40" width="'+str(bar_width(severity_count['medium']))+'" height="20" fill="orange"/>' 
   + '<text x="'+str(10 + bar_width(severity_count['medium']) + 5)+'" y="55" font-size="12" fill="orange">Medium</text>' if severity_count['medium']>0 else ''}
  {'<rect x="10" y="70" width="'+str(bar_width(severity_count['low']))+'" height="20" fill="green"/>' 
   + '<text x="'+str(10 + bar_width(severity_count['low']) + 5)+'" y="85" font-size="12" fill="green">Low</text>' if severity_count['low']>0 else ''}
</svg>"""

chart_path = charts_folder / "severity_chart.svg"
with open(chart_path, "w") as f:
    f.write(svg_content)

# -----------------------------
# 6️⃣ Generate README.md
# -----------------------------
total_xp = severity_count['high']*10 + severity_count['medium']*5 + severity_count['low']*2
badge_url = f"https://img.shields.io/badge/XP%3A{total_xp}%20%7C%20H%3A{severity_count['high']}%20M%3A{severity_count['medium']}%20L%3A{severity_count['low']}-blue"

dashboard = f"![XP Badge]({badge_url})\n\n"
dashboard += "# 📊 SOC Simulation & Data Analyst Automation\n\n"
dashboard += "> Simulated SOC workflow: alert → ticket → playbook → analyst/IR decision → XP scoring\n\n"
dashboard += "### 📊 Alert Severity Distribution\n"
dashboard += svg_content + "\n\n"

dashboard += "### 🚨 Recent Alerts\n"
dashboard += "| Date | Alert ID | Severity | Event |\n|------|---------|---------|-------|\n"
for alert_file in sorted(alerts_folder.glob("*.json"), reverse=True)[0:5]:
    with open(alert_file) as f:
        alert = json.load(f)
    dashboard += f"| {alert_file.stem} | {alert.get('alert_id')} | {alert.get('severity')} | {alert.get('event')} |\n"

dashboard += "\n### 🛠️ Recent Playbooks\n"
dashboard += "| Date | Playbook ID | Name | Severity |\n|------|------------|------|---------|\n"
for pb in sorted(playbooks_folder.glob("*.yml"), reverse=True)[0:5]:
    date = pb.stem.split("_")[0]
    dashboard += f"| {date} | PB-{date} | Automated IR Playbook | {alert_severity} |\n"

dashboard += f"\n### 📈 Totals\n- Alerts generated: {len(list(alerts_folder.glob('*.json')))}\n- Total XP: {total_xp}\n"

dashboard += "\n## 🧠 MITRE ATT&CK Coverage\n| Date | Alert ID | Tactic | Technique ID | Technique Name |\n|------|---------|--------|--------------|----------------|\n"
for alert_file in sorted(alerts_folder.glob("*.json"), reverse=True)[0:5]:
    with open(alert_file) as f:
        alert = json.load(f)
    mitre = alert.get("mitre", {})
    dashboard += f"| {alert_file.stem} | {alert.get('alert_id')} | {mitre.get('tactic')} | {mitre.get('technique_id')} | {mitre.get('technique_name')} |\n"

with open(BASE_DIR / "README.md", "w") as f:
    f.write(dashboard)
