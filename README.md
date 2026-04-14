# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1132%20🔴:67%20🟠:68%20🟢:61-blue)

---

## 🎯 Purpose
SOC-Analytics-Dashboard simulates a **Security Operations Center (SOC)** environment with automated ticketing and alert tracking.  
It helps blue teams **analyze trends, prioritize incidents, and monitor high-risk hosts** in a controlled environment.

- Simulates realistic SOC alerts 🔴🟠🟢  
- Prioritizes by severity  
- Tracks top hosts 🖥️  
- Monitors alert velocity ⏱️  
- Produces daily dashboards with historical trends 📈  

---

## ⚡ How SOC Simulation Works
- **Event Generation:** Simulates alerts and tickets for multiple systems  
- **Severity Analytics:** Counts alerts by high/medium/low and calculates percentages  
- **Host Monitoring:** Tracks top 5 hosts generating the most alerts 🖥️  
- **Velocity Tracking:** Measures alert trends for last 24 hours & all-time ⏱️  
- **Visualization:** Color-coded SVG charts & tables for fast comprehension

---

## 📊 Dashboard Overview

<img src="charts/severity_chart.svg?20260414183737" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>67</td><td>34%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>68</td><td>35%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>61</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-62</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-13</td><td style='color:black; font-weight:bold;'>4</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>196</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-04-14_20260414183737 | SOC-INC20260414-7064 | ALERT-20260414-3317 | 🔴 High | Simulated SOC event (high) |
| 2026-04-14_20260414065612 | SOC-INC20260414-9416 | ALERT-20260414-5417 | 🔴 High | Simulated SOC event (high) |
| 2026-04-13_20260413183521 | SOC-INC20260413-1004 | ALERT-20260413-3025 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-04-13_20260413070926 | SOC-INC20260413-3668 | ALERT-20260413-2963 | 🔴 High | Simulated SOC event (high) |
| 2026-04-12_20260412182412 | SOC-INC20260412-1097 | ALERT-20260412-3679 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |