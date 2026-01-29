# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:224%20H:13%20M:12%20L:17-blue)

This dashboard simulates a SOC workflow:
- Tracks severity of alerts (counts + % of total)
- Shows alert velocity (last 24 hours / all time)
- Highlights the top hosts generating alerts
- Displays recent alerts and detection rules

## 📈 Alert Analytics
<img src="charts/severity_chart.svg?20260128231951" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td style='color:red'>🔴 High</td><td style='color:red'>13</td><td style='color:red'>31%</td></tr><tr><td style='color:orange'>🟠 Medium</td><td style='color:orange'>12</td><td style='color:orange'>29%</td></tr><tr><td style='color:green'>🟢 Low</td><td style='color:green'>17</td><td style='color:green'>40%</td></tr></table></td><td valign='top'><b>Top 5 Hosts</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td>2</td></tr><tr><td>HOST-67</td><td>2</td></tr><tr><td>HOST-25</td><td>1</td></tr><tr><td>HOST-45</td><td>1</td></tr><tr><td>HOST-23</td><td>1</td></tr></table></td><td valign='top'><b>Alert Velocity</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>20</td></tr><tr><td>All Time</td><td>42</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-01-28_20260128231951 | SOC-INC20260128-6433 | ALERT-20260128-2208 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128231732 | SOC-INC20260128-9933 | ALERT-20260128-2160 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-28_20260128231606 | SOC-INC20260128-1049 | ALERT-20260128-6566 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128231404 | SOC-INC20260128-2292 | ALERT-20260128-3693 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128231217 | SOC-INC20260128-6732 | ALERT-20260128-6958 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |