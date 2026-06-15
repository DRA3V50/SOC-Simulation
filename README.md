# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1821%20🔴:105%20🟠:115%20🟢:98-blue)

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

<img src="charts/severity_chart.svg?20260615113631" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>105</td><td>33%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>115</td><td>36%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>98</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>7</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>318</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-06-15_20260615113631 | SOC-INC20260615-5117 | ALERT-20260615-6193 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-14_20260614185902 | SOC-INC20260614-3363 | ALERT-20260614-3380 | 🟢 Low | Simulated SOC event (low) |
| 2026-06-14_20260614074915 | SOC-INC20260614-6943 | ALERT-20260614-3208 | 🟢 Low | Simulated SOC event (low) |
| 2026-06-13_20260613185430 | SOC-INC20260613-5810 | ALERT-20260613-2561 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-06-13_20260613074724 | SOC-INC20260613-3741 | ALERT-20260613-9944 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |