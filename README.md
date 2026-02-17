# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:456%20🔴:25%20🟠:30%20🟢:28-blue)

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

<img src="charts/severity_chart.svg?20260217053657" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>25</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>30</td><td>36%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>28</td><td>34%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-13</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>2</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>83</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-02-17_20260217053657 | SOC-INC20260217-4764 | ALERT-20260217-1809 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-16_20260216171859 | SOC-INC20260216-1683 | ALERT-20260216-4604 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-16_20260216054005 | SOC-INC20260216-1734 | ALERT-20260216-3772 | 🔴 High | Simulated SOC event (high) |
| 2026-02-15_20260215171523 | SOC-INC20260215-3419 | ALERT-20260215-5391 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-02-15_20260215051737 | SOC-INC20260215-5059 | ALERT-20260215-3939 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |