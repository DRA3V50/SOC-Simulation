# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:197%20H:12%20M:11%20L:11-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128230438" width="320" />

<table>
<tr>
<td>

<b>Severity Overview</b>

| Severity | Count | % of Total |
|---|---|---|
| 🔴 High | 12 | 35% |
| 🟠 Medium | 11 | 32% |
| 🟢 Low | 11 | 32% |


</td>
<td>

<b>Alert Velocity</b>

| Window | Alerts |
|---|---|
| Last 24 Hours | 12 |
| All Time | 34 |


</td>
</tr>
</table>

## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|---|---|---|---|---|
| 2026-01-28_20260128230438 | SOC-INC20260128-4669 | ALERT-20260128-9906 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128230220 | SOC-INC20260128-3595 | ALERT-20260128-7478 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225951 | SOC-INC20260128-7731 | ALERT-20260128-9923 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225649 | SOC-INC20260128-3186 | ALERT-20260128-9290 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128225256 | SOC-INC20260128-3930 | ALERT-20260128-6946 | 🟢 Low | Simulated SOC event (low) |

## 🖥️ Top 5 Hosts by Alerts
| Host | Count |
|---|---|
| HOST-67 | 2 |
| HOST-25 | 1 |
| HOST-29 | 1 |
| HOST-61 | 1 |
| HOST-58 | 1 |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |