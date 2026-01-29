# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:209%20H:13%20M:11%20L:12-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128230851" width="320" />


<div style="display:flex; justify-content:center; gap:50px;">

<div>
<b>Severity Overview</b>
| Severity | Count | % of Total |
|---|---|---|
| 🔴 High | 13 | 36% |
| 🟠 Medium | 11 | 31% |
| 🟢 Low | 12 | 33% |

</div>

<div>
<b>Alert Velocity</b>
| Window | Alerts |
|---|---|
| Last 24 Hours | 14 |
| All Time | 36 |

</div>

<div>
<b>Top 5 Hosts</b>
| Host | Count |
|---|---|
| HOST-29 | 2 |
| HOST-67 | 2 |
| HOST-25 | 1 |
| HOST-51 | 1 |
| HOST-61 | 1 |

</div>

</div>

## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|---|---|---|---|---|
| 2026-01-28_20260128230851 | SOC-INC20260128-3270 | ALERT-20260128-6654 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128230657 | SOC-INC20260128-3328 | ALERT-20260128-2258 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128230438 | SOC-INC20260128-4669 | ALERT-20260128-9906 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128230220 | SOC-INC20260128-3595 | ALERT-20260128-7478 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128225951 | SOC-INC20260128-7731 | ALERT-20260128-9923 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |