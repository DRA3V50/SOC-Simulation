# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1968%20🔴:111%20🟠:128%20🟢:109-blue)

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

<img src="charts/severity_chart.svg?20260630080347" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>111</td><td>32%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>128</td><td>37%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>109</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>7</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>348</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-06-30_20260630080347 | SOC-INC20260630-8758 | ALERT-20260630-9883 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-29_20260629184639 | SOC-INC20260629-9918 | ALERT-20260629-9528 | 🟢 Low | Simulated SOC event (low) |
| 2026-06-29_20260629095754 | SOC-INC20260629-9218 | ALERT-20260629-1041 | 🟢 Low | Simulated SOC event (low) |
| 2026-06-28_20260628185445 | SOC-INC20260628-7201 | ALERT-20260628-7175 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-28_20260628074213 | SOC-INC20260628-5274 | ALERT-20260628-6353 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |