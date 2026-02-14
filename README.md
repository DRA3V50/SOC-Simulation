# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:427%20🔴:24%20🟠:27%20🟢:26-blue)

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

<img src="charts/severity_chart.svg?20260214051738" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>24</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>27</td><td>35%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>26</td><td>34%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-13</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>2</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>77</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-02-14_20260214051738 | SOC-INC20260214-7219 | ALERT-20260214-4327 | 🔴 High | Simulated SOC event (high) |
| 2026-02-13_20260213172400 | SOC-INC20260213-7133 | ALERT-20260213-1803 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-13_20260213053115 | SOC-INC20260213-3465 | ALERT-20260213-6236 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-12_20260212172249 | SOC-INC20260212-6311 | ALERT-20260212-5775 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-12_20260212053556 | SOC-INC20260212-8326 | ALERT-20260212-8809 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |