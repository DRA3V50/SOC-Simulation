# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2891%20🔴:155%20🟠:205%20🟢:158-blue)

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

<img src="charts/severity_chart.svg?20260923200649" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>155</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>205</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>158</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-27</td><td style='color:black; font-weight:bold;'>9</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>518</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-09-23_20260923200649 | SOC-INC20260923-5425 | ALERT-20260923-5238 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-23_20260923103252 | SOC-INC20260923-1421 | ALERT-20260923-2672 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-22_20260922195446 | SOC-INC20260922-7887 | ALERT-20260922-1962 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-22_20260922101458 | SOC-INC20260922-3490 | ALERT-20260922-8679 | 🟢 Low | Simulated SOC event (low) |
| 2026-09-21_20260921202400 | SOC-INC20260921-9358 | ALERT-20260921-4025 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |