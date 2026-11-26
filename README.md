# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:3658%20🔴:201%20🟠:254%20🟢:189-blue)

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

<img src="charts/severity_chart.svg?20261125225044" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>201</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>254</td><td>39%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>189</td><td>29%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>13</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>11</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>644</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-11-25_20261125225044 | SOC-INC20261125-9612 | ALERT-20261125-8608 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-11-25_20261125143953 | SOC-INC20261125-7829 | ALERT-20261125-5396 | 🟢 Low | Simulated SOC event (low) |
| 2026-11-24_20261124234138 | SOC-INC20261124-1466 | ALERT-20261124-2180 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-11-24_20261124152545 | SOC-INC20261124-4208 | ALERT-20261124-2602 | 🔴 High | Simulated SOC event (high) |
| 2026-11-24_20261124004041 | SOC-INC20261124-4983 | ALERT-20261124-5227 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |