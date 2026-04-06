# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1021%20🔴:60%20🟠:61%20🟢:58-blue)

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

<img src="charts/severity_chart.svg?20260406064753" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>60</td><td>34%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>61</td><td>34%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>58</td><td>32%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-70</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-96</td><td style='color:black; font-weight:bold;'>4</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>179</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-04-06_20260406064753 | SOC-INC20260406-2094 | ALERT-20260406-4064 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-04-05_20260405182113 | SOC-INC20260405-1180 | ALERT-20260405-8892 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-04-05_20260405062357 | SOC-INC20260405-5260 | ALERT-20260405-8400 | 🔴 High | Simulated SOC event (high) |
| 2026-04-04_20260404182014 | SOC-INC20260404-1111 | ALERT-20260404-2456 | 🔴 High | Simulated SOC event (high) |
| 2026-04-04_20260404062403 | SOC-INC20260404-5931 | ALERT-20260404-4788 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |