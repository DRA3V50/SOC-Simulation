# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:171%20H:10%20M:11%20L:8-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128224915" width="320" />

<table>
<tr>
<td>

**Severity Counts**

| Severity | Count |
|---|---|
| 🔴 High | 10 |
| 🟠 Medium | 11 |
| 🟢 Low | 8 |


</td>
<td>

**Severity % of Total**

| Severity | Count | % |
|---|---|---|
| 🔴 High | 10 | 34% |
| 🟠 Medium | 11 | 38% |
| 🟢 Low | 8 | 28% |


</td>
</tr>
</table>

## ⏱️ Alert Velocity

| Window | Alerts |
|-------|--------|
| Last 24 Hours | 7 |
| All Time | 29 |

## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|---|---|---|---|---|
| 2026-01-28_20260128224915 | SOC-INC20260128-1300 | ALERT-20260128-5130 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-28_20260128224446 | SOC-INC20260128-5377 | ALERT-20260128-5500 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128224207 | SOC-INC20260128-6121 | ALERT-20260128-4177 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128223234 | SOC-INC20260128-3926 | ALERT-20260128-2954 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-28_20260128222853 | SOC-INC20260128-1264 | ALERT-20260128-3394 | 🟢 Low | Simulated SOC event (low) |

## 🖥️ Top 5 Hosts by Alerts
| Host | Count |
|---|---|
| UNKNOWN_HOST | 26 |
| HOST-25 | 1 |
| HOST-29 | 1 |
| HOST-58 | 1 |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |