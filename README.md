# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:121%20H:8%20M:7%20L:3-blue)

- Simulates a professional Security Operations Center workflow with automated ticketing using 🎟️ Jira and ServiceNow, alert escalation 🚨 based on severity, and data-driven analytics 📊 for SIEM, SOAR, and incident response.

## 🔹 Project Focus and Incident Correlation
- 🎟️ Automated Ticketing & Alerts – Generates daily tickets in Jira/ServiceNow format and simulates real incident intake.
- 🚨 Escalation & Prioritization – Automatically classifies alerts High 🔴 / Medium 🟠 / Low 🟢 for analyst prioritization.
- 📈 Analytics & Visualization – Counts alerts, calculates XP points, and generates severity charts 📊.
- 🔍 Data Analysis – Identifies patterns, recurring issues, and prioritizes incidents.
- ⚙️ Automation – Fully automated via GitHub Actions to simulate daily SOC activity.
- ⚡ Detection and Incident Correlation
- 📐 SIEM Detection Rules – Structured detection rules identify suspicious activity.
- 🔄 Incident Lifecycle Tracking – Tracks events from detection to resolution.
- 🔗 Alert Correlation – Groups related alerts into single incidents to reduce noise.

## 📈 Alert Analytics
Severity Distribution

| Severity | Count |
|----------|-------|
| 🔴 High  | 8 |
| 🟠 Medium| 7 |
| 🟢 Low   | 3 |

## 📊 Chart Display
<img src="charts/severity_chart.svg" width="320" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
| 2026-01-23 | SOC-INC20260123-5984 | ALERT-20260123-5496 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-22 | SOC-INC20260122-8467 | ALERT-20260122-5117 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-21 | SOC-INC20260121-1476 | ALERT-20260121-5449 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-20 | SOC-INC20260120-6434 | ALERT-20260120-3977 | 🔴 High | Simulated SOC event (high) |
| 2026-01-19 | SOC-INC20260119-5481 | ALERT-20260119-6474 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---------|------|---------|-------------|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |