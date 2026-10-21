# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:3220%20🔴:174%20🟠:228%20🟢:170-blue)

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

<img src="charts/severity_chart.svg?20261020201403" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>174</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>228</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>170</td><td>30%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>11</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>11</td></tr><tr><td>HOST-35</td><td style='color:black; font-weight:bold;'>10</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>572</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-10-20_20261020201403 | SOC-INC20261020-5314 | ALERT-20261020-3185 | 🟢 Low | Simulated SOC event (low) |
| 2026-10-20_20261020103357 | SOC-INC20261020-2111 | ALERT-20261020-1711 | 🔴 High | Simulated SOC event (high) |
| 2026-10-19_20261019204906 | SOC-INC20261019-2860 | ALERT-20261019-7056 | 🔴 High | Simulated SOC event (high) |
| 2026-10-19_20261019124148 | SOC-INC20261019-3152 | ALERT-20261019-7201 | 🔴 High | Simulated SOC event (high) |
| 2026-10-18_20261018194739 | SOC-INC20261018-8156 | ALERT-20261018-3554 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |