# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:137%20H:8%20M:9%20L:6-blue)

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
| 🟠 Medium| 9 |
| 🟢 Low   | 6 |

## 📊 Chart Display
<img src="charts/severity_chart.svg" width="500" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
| 2026-01-28 | SOC-INC20260128-3075 | ALERT-20260128-9056 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-27 | SOC-INC20260127-6734 | ALERT-20260127-5536 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-26 | SOC-INC20260126-6847 | ALERT-20260126-8506 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-25 | SOC-INC20260125-4342 | ALERT-20260125-2792 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-24 | SOC-INC20260124-1853 | ALERT-20260124-9618 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---------|------|---------|-------------|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |
