# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:314%20🔴:17%20🟠:22%20🟢:17-blue)

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

<img src="charts/severity_chart.svg?20260203172124" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>17</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>22</td><td>39%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>17</td><td>30%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-50</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-67</td><td style='color:black; font-weight:bold;'>2</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>56</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-02-03_20260203172124 | SOC-INC20260203-9685 | ALERT-20260203-2258 | 🔴 High | Simulated SOC event (high) |
| 2026-02-03_20260203053104 | SOC-INC20260203-5945 | ALERT-20260203-5727 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-02_20260202053556 | SOC-INC20260202-6072 | ALERT-20260202-3765 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-01_20260201171500 | SOC-INC20260201-7309 | ALERT-20260201-1771 | 🔴 High | Simulated SOC event (high) |
| 2026-02-01_20260201051656 | SOC-INC20260201-5813 | ALERT-20260201-1258 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |