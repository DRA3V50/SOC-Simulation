# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:3678%20🔴:202%20🟠:256%20🟢:189-blue)

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

<img src="charts/severity_chart.svg?20261127141542" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>202</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>256</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>189</td><td>29%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>13</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>12</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>11</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>647</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-11-27_20261127141542 | SOC-INC20261127-1986 | ALERT-20261127-9922 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-11-26_20261126225205 | SOC-INC20261126-6757 | ALERT-20261126-4867 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-11-26_20261126142036 | SOC-INC20261126-4501 | ALERT-20261126-2749 | 🔴 High | Simulated SOC event (high) |
| 2026-11-25_20261125225044 | SOC-INC20261125-9612 | ALERT-20261125-8608 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-11-25_20261125143953 | SOC-INC20261125-7829 | ALERT-20261125-5396 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |