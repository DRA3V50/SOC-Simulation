# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1055%20🔴:63%20🟠:61%20🟢:60-blue)

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

<img src="charts/severity_chart.svg?20260408183011" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>63</td><td>34%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>61</td><td>33%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>60</td><td>33%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-13</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-62</td><td style='color:black; font-weight:bold;'>4</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>184</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-04-08_20260408183011 | SOC-INC20260408-6223 | ALERT-20260408-7606 | 🟢 Low | Simulated SOC event (low) |
| 2026-04-08_20260408064938 | SOC-INC20260408-8220 | ALERT-20260408-5119 | 🔴 High | Simulated SOC event (high) |
| 2026-04-07_20260407182938 | SOC-INC20260407-5988 | ALERT-20260407-3413 | 🔴 High | Simulated SOC event (high) |
| 2026-04-07_20260407064719 | SOC-INC20260407-9829 | ALERT-20260407-7380 | 🔴 High | Simulated SOC event (high) |
| 2026-04-06_20260406182651 | SOC-INC20260406-1895 | ALERT-20260406-9882 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |