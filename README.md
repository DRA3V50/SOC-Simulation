# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2918%20🔴:156%20🟠:208%20🟢:159-blue)

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

<img src="charts/severity_chart.svg?20260926095747" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>156</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>208</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>159</td><td>30%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-27</td><td style='color:black; font-weight:bold;'>9</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>523</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-09-26_20260926095747 | SOC-INC20260926-3301 | ALERT-20260926-1996 | 🔴 High | Simulated SOC event (high) |
| 2026-09-25_20260925201544 | SOC-INC20260925-5357 | ALERT-20260925-1163 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-25_20260925105158 | SOC-INC20260925-5440 | ALERT-20260925-3789 | 🟢 Low | Simulated SOC event (low) |
| 2026-09-24_20260924200946 | SOC-INC20260924-7760 | ALERT-20260924-5697 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-24_20260924103123 | SOC-INC20260924-7129 | ALERT-20260924-1277 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |