# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:2343%20🔴:131%20🟠:155%20🟢:129-blue)

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

<img src="charts/severity_chart.svg?20260803084925" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>131</td><td>32%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>155</td><td>37%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>129</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-30</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-36</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-12</td><td style='color:black; font-weight:bold;'>8</td></tr><tr><td>HOST-43</td><td style='color:black; font-weight:bold;'>8</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>415</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-08-03_20260803084925 | SOC-INC20260803-1531 | ALERT-20260803-4018 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-08-02_20260802184506 | SOC-INC20260802-7153 | ALERT-20260802-5913 | 🟢 Low | Simulated SOC event (low) |
| 2026-08-02_20260802071033 | SOC-INC20260802-7883 | ALERT-20260802-2822 | 🔴 High | Simulated SOC event (high) |
| 2026-08-01_20260801184418 | SOC-INC20260801-4313 | ALERT-20260801-2561 | 🟢 Low | Simulated SOC event (low) |
| 2026-08-01_20260801071014 | SOC-INC20260801-2300 | ALERT-20260801-8589 | 🔴 High | Simulated SOC event (high) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |