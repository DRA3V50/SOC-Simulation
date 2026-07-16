# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2157%20🔴:122%20🟠:141%20🟢:116-blue)

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

<img src="charts/severity_chart.svg?20260716072627" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>122</td><td>32%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>141</td><td>37%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>116</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>8</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>379</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-07-16_20260716072627 | SOC-INC20260716-8287 | ALERT-20260716-6788 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-07-15_20260715184932 | SOC-INC20260715-6094 | ALERT-20260715-3132 | 🔴 High | Simulated SOC event (high) |
| 2026-07-15_20260715072125 | SOC-INC20260715-1329 | ALERT-20260715-8056 | 🟢 Low | Simulated SOC event (low) |
| 2026-07-14_20260714184700 | SOC-INC20260714-1546 | ALERT-20260714-3129 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-07-14_20260714071749 | SOC-INC20260714-1398 | ALERT-20260714-3625 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |