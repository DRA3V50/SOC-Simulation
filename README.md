# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:509%20🔴:29%20🟠:31%20🟢:32-blue)

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

<img src="charts/severity_chart.svg?20260221171437" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>29</td><td>32%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>31</td><td>34%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>32</td><td>35%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-13</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>3</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>92</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-02-21_20260221171437 | SOC-INC20260221-5716 | ALERT-20260221-3879 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-21_20260221051655 | SOC-INC20260221-4415 | ALERT-20260221-4761 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-20_20260220171622 | SOC-INC20260220-7290 | ALERT-20260220-7897 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-20_20260220052852 | SOC-INC20260220-4086 | ALERT-20260220-5336 | 🔴 High | Simulated SOC event (high) |
| 2026-02-19_20260219172206 | SOC-INC20260219-2565 | ALERT-20260219-4790 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |