# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:3060%20🔴:164%20🟠:218%20🟢:165-blue)

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

<img src="charts/severity_chart.svg?20261008130455" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>164</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>218</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>165</td><td>30%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>11</td></tr><tr><td>HOST-55</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>10</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>547</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-10-08_20261008130455 | SOC-INC20261008-2909 | ALERT-20261008-6037 | 🔴 High | Simulated SOC event (high) |
| 2026-10-07_20261007212628 | SOC-INC20261007-7494 | ALERT-20261007-3149 | 🔴 High | Simulated SOC event (high) |
| 2026-10-07_20261007130545 | SOC-INC20261007-1739 | ALERT-20261007-9210 | 🟢 Low | Simulated SOC event (low) |
| 2026-10-06_20261006210817 | SOC-INC20261006-5477 | ALERT-20261006-2301 | 🔴 High | Simulated SOC event (high) |
| 2026-10-06_20261006122336 | SOC-INC20261006-3652 | ALERT-20261006-9071 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |