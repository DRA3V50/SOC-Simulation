# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:142%20H:9%20M:8%20L:6-blue)

- Simulates a professional Security Operations Center workflow with automated ticketing using 🎟️ Jira and ServiceNow, alert escalation 🚨 based on severity, and data-driven analytics 📊 for SIEM, SOAR, and incident response.

## 🔹 Project Focus and Incident Correlation
- 🎟️ Automated Ticketing & Alerts
- 🚨 Escalation & Prioritization
- 📈 Analytics & Visualization
- 🔍 Data Analysis
- ⚙️ Automation

## 📈 Alert Analytics
Severity Distribution

| Severity | Count |
|----------|-------|
| 🔴 High  | 9 |
| 🟠 Medium| 8 |
| 🟢 Low   | 6 |

## 📊 Chart Display
<img src="charts/severity_chart.svg" width="320" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
| 2026-01-28 | SOC-INC20260128-3316 | ALERT-20260128-9026 | 🔴 High | Simulated SOC event (high) |
| 2026-01-27 | SOC-INC20260127-6734 | ALERT-20260127-5536 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-26 | SOC-INC20260126-6847 | ALERT-20260126-8506 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-25 | SOC-INC20260125-4342 | ALERT-20260125-2792 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-24 | SOC-INC20260124-1853 | ALERT-20260124-9618 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---------|------|---------|-------------|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |