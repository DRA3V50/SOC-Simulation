# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2274%20🔴:125%20🟠:154%20🟢:127-blue)

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

<img src="charts/severity_chart.svg?20260729185123" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>125</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>154</td><td>38%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>127</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>8</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>406</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-07-29_20260729185123 | SOC-INC20260729-7104 | ALERT-20260729-5611 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-07-29_20260729075407 | SOC-INC20260729-6259 | ALERT-20260729-3270 | 🟢 Low | Simulated SOC event (low) |
| 2026-07-28_20260728185059 | SOC-INC20260728-4953 | ALERT-20260728-3654 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-07-28_20260728074951 | SOC-INC20260728-6936 | ALERT-20260728-7981 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-07-27_20260727185222 | SOC-INC20260727-7090 | ALERT-20260727-5393 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |