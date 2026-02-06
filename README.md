# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:351%20🔴:19%20🟠:25%20🟢:18-blue)

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

<img src="charts/severity_chart.svg?20260206171402" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>19</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>25</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>18</td><td>29%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-50</td><td style='color:black; font-weight:bold;'>2</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>62</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-02-06_20260206171402 | SOC-INC20260206-1959 | ALERT-20260206-6988 | 🔴 High | Simulated SOC event (high) |
| 2026-02-06_20260206053102 | SOC-INC20260206-8712 | ALERT-20260206-4069 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-05_20260205171808 | SOC-INC20260205-7200 | ALERT-20260205-4188 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-05_20260205053222 | SOC-INC20260205-9164 | ALERT-20260205-9221 | 🔴 High | Simulated SOC event (high) |
| 2026-02-04_20260204171740 | SOC-INC20260204-7468 | ALERT-20260204-6237 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |