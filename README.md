# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:398%20🔴:22%20🟠:26%20🟢:24-blue)

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

<img src="charts/severity_chart.svg?20260211172200" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>22</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>26</td><td>36%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>24</td><td>33%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-13</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>3</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-56</td><td style='color:black; font-weight:bold;'>2</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>72</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-02-11_20260211172200 | SOC-INC20260211-4021 | ALERT-20260211-8578 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-11_20260211054025 | SOC-INC20260211-4004 | ALERT-20260211-4283 | 🔴 High | Simulated SOC event (high) |
| 2026-02-10_20260210173055 | SOC-INC20260210-6453 | ALERT-20260210-7209 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-10_20260210054500 | SOC-INC20260210-5051 | ALERT-20260210-8669 | 🟢 Low | Simulated SOC event (low) |
| 2026-02-09_20260209172746 | SOC-INC20260209-3803 | ALERT-20260209-6552 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |