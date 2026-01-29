# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:217%20H:13%20M:11%20L:16-blue)

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128231606" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td style='color:red'>🔴 High</td><td style='color:red'>13</td><td style='color:red'>32%</td></tr><tr><td style='color:orange'>🟠 Medium</td><td style='color:orange'>11</td><td style='color:orange'>28%</td></tr><tr><td style='color:green'>🟢 Low</td><td style='color:green'>16</td><td style='color:green'>40%</td></tr></table></td><td valign='top'><b>Alert Velocity</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>18</td></tr><tr><td>All Time</td><td>40</td></tr></table></td><td valign='top'><b>Top 5 Hosts</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td>2</td></tr><tr><td>HOST-67</td><td>2</td></tr><tr><td>HOST-25</td><td>1</td></tr><tr><td>HOST-23</td><td>1</td></tr><tr><td>HOST-51</td><td>1</td></tr></table></td></tr></table>
## 🎟️ Recent Alerts
| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-01-28_20260128231606 | SOC-INC20260128-1049 | ALERT-20260128-6566 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128231404 | SOC-INC20260128-2292 | ALERT-20260128-3693 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128231217 | SOC-INC20260128-6732 | ALERT-20260128-6958 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128231029 | SOC-INC20260128-5124 | ALERT-20260128-5088 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128230851 | SOC-INC20260128-3270 | ALERT-20260128-6654 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules
| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |