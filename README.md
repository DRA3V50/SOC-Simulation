# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1557%20🔴:91%20🟠:95%20🟢:86-blue)

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

<img src="charts/severity_chart.svg?20260522185022" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>91</td><td>33%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>95</td><td>35%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>86</td><td>32%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-94</td><td style='color:black; font-weight:bold;'>6</td></tr><tr><td>HOST-39</td><td style='color:black; font-weight:bold;'>6</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>272</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-05-22_20260522185022 | SOC-INC20260522-6688 | ALERT-20260522-8847 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-05-22_20260522081227 | SOC-INC20260522-4254 | ALERT-20260522-7938 | 🔴 High | Simulated SOC event (high) |
| 2026-05-21_20260521185733 | SOC-INC20260521-8481 | ALERT-20260521-2386 | 🟢 Low | Simulated SOC event (low) |
| 2026-05-21_20260521083858 | SOC-INC20260521-3448 | ALERT-20260521-5012 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-05-20_20260520190438 | SOC-INC20260520-8932 | ALERT-20260520-2728 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |