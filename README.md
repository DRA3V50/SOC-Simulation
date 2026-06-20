# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1863%20🔴:107%20🟠:117%20🟢:104-blue)

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

<img src="charts/severity_chart.svg?20260620075031" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>107</td><td>33%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>117</td><td>36%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>104</td><td>32%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>7</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>328</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-06-20_20260620075031 | SOC-INC20260620-6574 | ALERT-20260620-5097 | 🔴 High | Simulated SOC event (high) |
| 2026-06-19_20260619184344 | SOC-INC20260619-5204 | ALERT-20260619-8180 | 🟢 Low | Simulated SOC event (low) |
| 2026-06-19_20260619092736 | SOC-INC20260619-8759 | ALERT-20260619-7217 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-18_20260618192807 | SOC-INC20260618-8115 | ALERT-20260618-9156 | 🔴 High | Simulated SOC event (high) |
| 2026-06-18_20260618084518 | SOC-INC20260618-6643 | ALERT-20260618-2829 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |