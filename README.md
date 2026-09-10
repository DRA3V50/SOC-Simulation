# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2734%20🔴:147%20🟠:192%20🟢:152-blue)

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

<img src="charts/severity_chart.svg?20260910095652" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>147</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>192</td><td>39%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>152</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>9</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>491</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-09-10_20260910095652 | SOC-INC20260910-7169 | ALERT-20260910-9178 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-09_20260909194042 | SOC-INC20260909-9982 | ALERT-20260909-7302 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-09_20260909100205 | SOC-INC20260909-5308 | ALERT-20260909-4717 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-08_20260908194456 | SOC-INC20260908-9377 | ALERT-20260908-5592 | 🟢 Low | Simulated SOC event (low) |
| 2026-09-08_20260908095937 | SOC-INC20260908-5830 | ALERT-20260908-8649 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |