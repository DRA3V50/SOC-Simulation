# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:55%20H:4%20M:3%20L:0-blue)

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
| 🔴 High  | 4 |
| 🟠 Medium| 3 |
| 🟢 Low   | 0 |

## 📊 Chart Display
<img src="charts/severity_chart.svg" width="320" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
| 2026-01-12 | SOC-INC20260112-3056 | ALERT-20260112-3357 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-11 | SOC-INC20260111-1617 | ALERT-20260111-8549 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-10 | SOC-INC20260110-4315 | ALERT-20260110-5420 | 🔴 High | Simulated SOC event (high) |
| 2026-01-09 | SOC-INC20260109-3320 | ALERT-20260109-1023 | 🔴 High | Simulated SOC event (high) |
| 2026-01-08 | SOC-INC20260108-2672 | ALERT-20260108-8475 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---------|------|---------|-------------|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |