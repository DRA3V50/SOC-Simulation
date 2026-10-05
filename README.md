# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:3013%20🔴:160%20🟠:217%20🟢:164-blue)

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

<img src="charts/severity_chart.svg?20261005145729" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>160</td><td>30%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>217</td><td>40%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>164</td><td>30%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-55</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-69</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-82</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>10</td></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>10</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>541</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-10-05_20261005145729 | SOC-INC20261005-7654 | ALERT-20261005-3786 | 🟢 Low | Simulated SOC event (low) |
| 2026-10-04_20261004201915 | SOC-INC20261004-9310 | ALERT-20261004-4479 | 🔴 High | Simulated SOC event (high) |
| 2026-10-04_20261004110207 | SOC-INC20261004-5256 | ALERT-20261004-3674 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-10-03_20261003201418 | SOC-INC20261003-9190 | ALERT-20261003-4056 | 🟢 Low | Simulated SOC event (low) |
| 2026-10-03_20261003102741 | SOC-INC20261003-3044 | ALERT-20261003-2190 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |