# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:185%20H:11%20M:11%20L:10-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128225951" width="320" />

<table>
<tr>
<td>

<b>Severity Distribution</b>

| Severity | Count |
|---|---|
| 🔴 High | 11 |
| 🟠 Medium | 11 |
| 🟢 Low | 10 |


<br/>

| Severity | Count | % |
|---|---|---|
| 🔴 High | 11 | 34% |
| 🟠 Medium | 11 | 34% |
| 🟢 Low | 10 | 31% |


</td>
<td>

<b>Alert Velocity</b>

| Window | Alerts |
|---|---|
| Last 24 Hours | 10 |
| All Time | 32 |


</td>
</tr>
</table>

## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|---|---|---|---|---|
| 2026-01-28_20260128225951 | SOC-INC20260128-7731 | ALERT-20260128-9923 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225649 | SOC-INC20260128-3186 | ALERT-20260128-9290 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128225256 | SOC-INC20260128-3930 | ALERT-20260128-6946 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128224915 | SOC-INC20260128-1300 | ALERT-20260128-5130 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-28_20260128224446 | SOC-INC20260128-5377 | ALERT-20260128-5500 | 🔴 High | Simulated SOC event (high) |

## 🖥️ Top 5 Hosts by Alerts
| Host | Count |
|---|---|
| UNKNOWN_HOST | 26 |
| HOST-25 | 1 |
| HOST-29 | 1 |
| HOST-58 | 1 |
| HOST-31 | 1 |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |