# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2093%20🔴:118%20🟠:137%20🟢:114-blue)

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

<img src="charts/severity_chart.svg?20260711065457" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>118</td><td>32%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>137</td><td>37%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>114</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>8</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>369</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-07-11_20260711065457 | SOC-INC20260711-5427 | ALERT-20260711-9836 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-07-10_20260710185113 | SOC-INC20260710-5104 | ALERT-20260710-6879 | 🟢 Low | Simulated SOC event (low) |
| 2026-07-10_20260710081917 | SOC-INC20260710-5687 | ALERT-20260710-5222 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-07-09_20260709190220 | SOC-INC20260709-6134 | ALERT-20260709-3592 | 🟢 Low | Simulated SOC event (low) |
| 2026-07-08_20260708185554 | SOC-INC20260708-5263 | ALERT-20260708-2048 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |