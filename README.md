# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2451%20🔴:136%20🟠:165%20🟢:133-blue)

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

<img src="charts/severity_chart.svg?20260812183005" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>136</td><td>31%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>165</td><td>38%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>133</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-28</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-86</td><td style='color:black; font-weight:bold;'>9</td></tr><tr><td>HOST-12</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>8</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>434</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-08-12_20260812183005 | SOC-INC20260812-5713 | ALERT-20260812-6679 | 🔴 High | Simulated SOC event (high) |
| 2026-08-12_20260812065137 | SOC-INC20260812-9486 | ALERT-20260812-8063 | 🔴 High | Simulated SOC event (high) |
| 2026-08-11_20260811183132 | SOC-INC20260811-5256 | ALERT-20260811-3106 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-08-11_20260811064126 | SOC-INC20260811-5506 | ALERT-20260811-8346 | 🟢 Low | Simulated SOC event (low) |
| 2026-08-10_20260810182626 | SOC-INC20260810-8071 | ALERT-20260810-7082 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |