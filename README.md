# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1908%20🔴:109%20🟠:122%20🟢:104-blue)

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

<img src="charts/severity_chart.svg?20260623185929" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>109</td><td>33%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>122</td><td>36%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>104</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>7</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>335</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-06-23_20260623185929 | SOC-INC20260623-5198 | ALERT-20260623-1593 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-23_20260623082754 | SOC-INC20260623-4413 | ALERT-20260623-8279 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-22_20260622191203 | SOC-INC20260622-5316 | ALERT-20260622-4261 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-22_20260622111251 | SOC-INC20260622-7365 | ALERT-20260622-2557 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-21_20260621190031 | SOC-INC20260621-7908 | ALERT-20260621-5417 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |