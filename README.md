# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:173%20H:10%20M:11%20L:9-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128225256" width="320" />

<table>
<tr>
<td>

**Severity Counts**

| Severity | Count |
|---|---|
| 🔴 High | 10 |
| 🟠 Medium | 11 |
| 🟢 Low | 9 |


</td>
<td>

**Severity % of Total**

| Severity | Count | % |
|---|---|---|
| 🔴 High | 10 | 33% |
| 🟠 Medium | 11 | 37% |
| 🟢 Low | 9 | 30% |


</td>
<td>

**Alert Velocity**

| Window | Alerts |
|---|---|
| Last 24 Hours | 8 |
| All Time | 30 |


</td>
</tr>
</table>

## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|---|---|---|---|---|
| 2026-01-28_20260128225256 | SOC-INC20260128-3930 | ALERT-20260128-6946 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128224915 | SOC-INC20260128-1300 | ALERT-20260128-5130 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-28_20260128224446 | SOC-INC20260128-5377 | ALERT-20260128-5500 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128224207 | SOC-INC20260128-6121 | ALERT-20260128-4177 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128223234 | SOC-INC20260128-3926 | ALERT-20260128-2954 | 🟠 Medium | Simulated SOC event (medium) |

## 🖥️ Top 5 Hosts by Alerts
| Host | Count |
|---|---|
| UNKNOWN_HOST | 26 |
| HOST-25 | 1 |
| HOST-29 | 1 |
| HOST-58 | 1 |
| HOST-74 | 1 |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |