# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:249%20🔴:15%20🟠:13%20🟢:17-blue)

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

<img src="charts/severity_chart.svg?20260128232959" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>15</td><td>33%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>13</td><td>29%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>17</td><td>38%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-67</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-25</td><td style='color:black; font-weight:bold;'>1</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>1</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>23</td></tr><tr><td>All Time</td><td>45</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-01-28_20260128232959 | SOC-INC20260128-8871 | ALERT-20260128-6304 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128232611 | SOC-INC20260128-1050 | ALERT-20260128-6946 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-01-28_20260128232309 | SOC-INC20260128-4796 | ALERT-20260128-8181 | 🔴 High | Simulated SOC event (high) |
| 2026-01-28_20260128231951 | SOC-INC20260128-6433 | ALERT-20260128-2208 | 🟢 Low | Simulated SOC event (low) |
| 2026-01-28_20260128231732 | SOC-INC20260128-9933 | ALERT-20260128-2160 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |