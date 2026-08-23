# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2570%20🔴:142%20🟠:174%20🟢:140-blue)

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

<img src="charts/severity_chart.svg?20260823181120" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>142</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>174</td><td>38%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>140</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-12</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>8</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>456</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-08-23_20260823181120 | SOC-INC20260823-6988 | ALERT-20260823-2070 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-08-23_20260823061336 | SOC-INC20260823-1939 | ALERT-20260823-1445 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-08-22_20260822181136 | SOC-INC20260822-3861 | ALERT-20260822-7545 | 🔴 High | Simulated SOC event (high) |
| 2026-08-22_20260822061305 | SOC-INC20260822-4690 | ALERT-20260822-4632 | 🟢 Low | Simulated SOC event (low) |
| 2026-08-21_20260821181320 | SOC-INC20260821-7624 | ALERT-20260821-8535 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |