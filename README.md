# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:3494%20🔴:192%20🟠:242%20🟢:182-blue)

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

<img src="charts/severity_chart.svg?20261111213540" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>192</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>242</td><td>39%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>182</td><td>30%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>13</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-50</td><td style='color:black; font-weight:bold;'>11</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>11</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>616</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-11-11_20261111213540 | SOC-INC20261111-6291 | ALERT-20261111-4124 | 🔴 High | Simulated SOC event (high) |
| 2026-11-11_20261111123359 | SOC-INC20261111-1268 | ALERT-20261111-9804 | 🔴 High | Simulated SOC event (high) |
| 2026-11-10_20261110203549 | SOC-INC20261110-1126 | ALERT-20261110-5789 | 🔴 High | Simulated SOC event (high) |
| 2026-11-10_20261110122228 | SOC-INC20261110-9427 | ALERT-20261110-1306 | 🔴 High | Simulated SOC event (high) |
| 2026-11-09_20261109225321 | SOC-INC20261109-5631 | ALERT-20261109-6785 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |