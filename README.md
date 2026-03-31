# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:934%20🔴:54%20🟠:56%20🟢:57-blue)

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

<img src="charts/severity_chart.svg?20260331064444" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>54</td><td>32%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>56</td><td>34%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>57</td><td>34%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-63</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-96</td><td style='color:black; font-weight:bold;'>4</td></tr><tr><td>HOST-62</td><td style='color:black; font-weight:bold;'>4</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>167</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-03-31_20260331064444 | SOC-INC20260331-6659 | ALERT-20260331-6886 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-03-30_20260330182548 | SOC-INC20260330-6467 | ALERT-20260330-7718 | 🔴 High | Simulated SOC event (high) |
| 2026-03-30_20260330065505 | SOC-INC20260330-6807 | ALERT-20260330-6073 | 🟢 Low | Simulated SOC event (low) |
| 2026-03-29_20260329182058 | SOC-INC20260329-3795 | ALERT-20260329-4868 | 🟢 Low | Simulated SOC event (low) |
| 2026-03-29_20260329062353 | SOC-INC20260329-4976 | ALERT-20260329-9842 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |