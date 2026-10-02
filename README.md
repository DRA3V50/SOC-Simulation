# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2980%20🔴:158%20🟠:216%20🟢:160-blue)

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

<img src="charts/severity_chart.svg?20261001211151" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>158</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>216</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>160</td><td>30%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>10</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>534</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-10-01_20261001211151 | SOC-INC20261001-5291 | ALERT-20261001-2036 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-10-01_20261001124700 | SOC-INC20261001-8021 | ALERT-20261001-7667 | 🔴 High | Simulated SOC event (high) |
| 2026-09-30_20260930205454 | SOC-INC20260930-5590 | ALERT-20260930-2188 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-30_20260930120938 | SOC-INC20260930-5382 | ALERT-20260930-5557 | 🔴 High | Simulated SOC event (high) |
| 2026-09-29_20260929205345 | SOC-INC20260929-7108 | ALERT-20260929-4967 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |