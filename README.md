# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:713%20🔴:40%20🟠:45%20🟢:44-blue)

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

<img src="charts/severity_chart.svg?20260312063040" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>40</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>45</td><td>35%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>44</td><td>34%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-13</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-96</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>4</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>129</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-03-12_20260312063040 | SOC-INC20260312-2138 | ALERT-20260312-5681 | 🔴 High | Simulated SOC event (high) |
| 2026-03-11_20260311181918 | SOC-INC20260311-8322 | ALERT-20260311-9837 | 🟢 Low | Simulated SOC event (low) |
| 2026-03-11_20260311063007 | SOC-INC20260311-1509 | ALERT-20260311-7394 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-03-10_20260310181853 | SOC-INC20260310-6330 | ALERT-20260310-8058 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-03-10_20260310063015 | SOC-INC20260310-4717 | ALERT-20260310-2493 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |