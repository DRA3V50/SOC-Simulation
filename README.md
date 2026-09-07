# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2712%20🔴:147%20🟠:188%20🟢:151-blue)

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

<img src="charts/severity_chart.svg?20260907195156" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>147</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>188</td><td>39%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>151</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>9</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>486</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-09-07_20260907195156 | SOC-INC20260907-6381 | ALERT-20260907-5526 | 🟢 Low | Simulated SOC event (low) |
| 2026-09-07_20260907112324 | SOC-INC20260907-5241 | ALERT-20260907-4634 | 🟢 Low | Simulated SOC event (low) |
| 2026-09-06_20260906192126 | SOC-INC20260906-9367 | ALERT-20260906-2324 | 🔴 High | Simulated SOC event (high) |
| 2026-09-06_20260906091730 | SOC-INC20260906-4393 | ALERT-20260906-1914 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-05_20260905192720 | SOC-INC20260905-5444 | ALERT-20260905-4575 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |