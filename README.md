# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:146%20H:8%20M:10%20L:8-blue)

## 📈 Alert Analytics

| Severity | Count |
|----------|-------|
| 🔴 High  | 8 |
| 🟠 Medium| 10 |
| 🟢 Low   | 8 |

<img src="charts/severity_chart.svg?20260128223234" width="320" height="120" />

## 🎟️ Recent Tickets / Alerts
| Date | Ticket ID 🎟️ | Alert ID 🚨 | Severity | Event |
|------|---------------|------------|---------|-------|
| 2026-01-28_20260128223234 | SOC-INC20260128-3926 | ALERT-20260128-2954 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-28_20260128222853 | SOC-INC20260128-1264 | ALERT-20260128-3394 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128222743 | SOC-INC20260128-9317 | ALERT-20260128-3084 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28 | SOC-INC20260128-9396 | ALERT-20260128-2127 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-27 | SOC-INC20260127-6734 | ALERT-20260127-5536 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---------|------|---------|-------------|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |