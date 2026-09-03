# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2669%20🔴:145%20🟠:185%20🟢:147-blue)

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

<img src="charts/severity_chart.svg?20260903095942" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>145</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>185</td><td>39%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>147</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>9</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>477</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-09-03_20260903095942 | SOC-INC20260903-6300 | ALERT-20260903-4811 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-02_20260902194108 | SOC-INC20260902-9482 | ALERT-20260902-9071 | 🔴 High | Simulated SOC event (high) |
| 2026-09-02_20260902095720 | SOC-INC20260902-1775 | ALERT-20260902-7170 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-09-01_20260901194050 | SOC-INC20260901-2477 | ALERT-20260901-9666 | 🟢 Low | Simulated SOC event (low) |
| 2026-09-01_20260901102350 | SOC-INC20260901-5387 | ALERT-20260901-5837 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |