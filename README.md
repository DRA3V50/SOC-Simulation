# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1442%20🔴:85%20🟠:86%20🟢:81-blue)

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

<img src="charts/severity_chart.svg?20260512185204" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>85</td><td>34%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>86</td><td>34%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>81</td><td>32%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>7</td></tr><tr><td>HOST-62</td><td style='color:black; font-weight:bold;'>6</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>6</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>6</td></tr><tr><td>HOST-39</td><td style='color:black; font-weight:bold;'>5</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>252</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-05-12_20260512185204 | SOC-INC20260512-2152 | ALERT-20260512-1576 | 🟢 Low | Simulated SOC event (low) |
| 2026-05-12_20260512074655 | SOC-INC20260512-6730 | ALERT-20260512-3418 | 🔴 High | Simulated SOC event (high) |
| 2026-05-11_20260511184545 | SOC-INC20260511-5743 | ALERT-20260511-4027 | 🔴 High | Simulated SOC event (high) |
| 2026-05-11_20260511083416 | SOC-INC20260511-8197 | ALERT-20260511-4116 | 🔴 High | Simulated SOC event (high) |
| 2026-05-10_20260510183715 | SOC-INC20260510-2997 | ALERT-20260510-3079 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |