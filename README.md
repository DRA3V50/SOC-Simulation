# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:187%20H:11%20M:11%20L:11-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128230220" width="320" />

<table>
<tr>
<td>

<b>Severity Overview</b>

| Severity | Count | % of Total |
|---|---|---|
| 🔴 High | 11 | 33% |
| 🟠 Medium | 11 | 33% |
| 🟢 Low | 11 | 33% |


</td>
<td>

<b>Alert Velocity</b>

| Window | Alerts |
|---|---|
| Last 24 Hours | 11 |
| All Time | 33 |


</td>
</tr>
</table>

## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|---|---|---|---|---|
| 2026-01-28_20260128230220 | SOC-INC20260128-3595 | ALERT-20260128-7478 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225951 | SOC-INC20260128-7731 | ALERT-20260128-9923 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225649 | SOC-INC20260128-3186 | ALERT-20260128-9290 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128225256 | SOC-INC20260128-3930 | ALERT-20260128-6946 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128224915 | SOC-INC20260128-1300 | ALERT-20260128-5130 | 🟠 Medium | Simulated SOC event (medium) |

## 🖥️ Top 5 Hosts by Alerts
| Host | Count |
|---|---|
| UNKNOWN_HOST | 26 |
| HOST-25 | 1 |
| HOST-29 | 1 |
| HOST-61 | 1 |
| HOST-58 | 1 |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |