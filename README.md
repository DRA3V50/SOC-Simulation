# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:199%20H:12%20M:11%20L:12-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128230657" width="320" />

<table>
<tr>
<td>

<b>Severity Overview</b>

| Severity | Count | % of Total |
|---|---|---|
| 🔴 High | 12 | 34% |
| 🟠 Medium | 11 | 31% |
| 🟢 Low | 12 | 34% |


</td>
<td>

<b>Velocity & Top Hosts</b>

| Window | Alerts |
|---|---|
| Last 24 Hours | 13 |
| All Time | 35 |


| Host | Count |
|---|---|
| HOST-29 | 2 |
| HOST-67 | 2 |
| HOST-25 | 1 |
| HOST-61 | 1 |
| HOST-58 | 1 |


</td>
</tr>
</table>

## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|---|---|---|---|---|
| 2026-01-28_20260128230657 | SOC-INC20260128-3328 | ALERT-20260128-2258 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128230438 | SOC-INC20260128-4669 | ALERT-20260128-9906 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128230220 | SOC-INC20260128-3595 | ALERT-20260128-7478 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225951 | SOC-INC20260128-7731 | ALERT-20260128-9923 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225649 | SOC-INC20260128-3186 | ALERT-20260128-9290 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |