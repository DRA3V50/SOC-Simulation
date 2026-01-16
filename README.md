# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:87%20H:7%20M:3%20L:1-blue)

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
| 🔴 High  | 7 |
| 🟠 Medium| 3 |
| 🟢 Low   | 1 |

## 📊 Chart Display
<img src="charts/severity_chart.svg" width="320" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
| 2026-01-16 | SOC-INC20260116-5905 | ALERT-20260116-9747 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-15 | SOC-INC20260115-1250 | ALERT-20260115-6984 | 🔴 High | Simulated SOC event (high) |
| 2026-01-14 | SOC-INC20260114-6661 | ALERT-20260114-8263 | 🔴 High | Simulated SOC event (high) |
| 2026-01-13 | SOC-INC20260113-5220 | ALERT-20260113-5095 | 🔴 High | Simulated SOC event (high) |
| 2026-01-12 | SOC-INC20260112-3056 | ALERT-20260112-3357 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---------|------|---------|-------------|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |