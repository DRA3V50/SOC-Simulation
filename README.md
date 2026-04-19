# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1188%20🔴:71%20🟠:70%20🟢:64-blue)

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

<img src="charts/severity_chart.svg?20260419063123" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>71</td><td>35%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>70</td><td>34%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>64</td><td>31%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-62</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-66</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-31</td><td style='color:black; font-weight:bold;'>4</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>3</td></tr><tr><td>All Time</td><td>205</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-04-19_20260419063123 | SOC-INC20260419-8358 | ALERT-20260419-7267 | 🟢 Low | Simulated SOC event (low) |
| 2026-04-18_20260418182447 | SOC-INC20260418-6758 | ALERT-20260418-3485 | 🟢 Low | Simulated SOC event (low) |
| 2026-04-18_20260418063230 | SOC-INC20260418-9843 | ALERT-20260418-1706 | 🔴 High | Simulated SOC event (high) |
| 2026-04-17_20260417182921 | SOC-INC20260417-2238 | ALERT-20260417-2186 | 🔴 High | Simulated SOC event (high) |
| 2026-04-17_20260417064647 | SOC-INC20260417-1929 | ALERT-20260417-7349 | 🟠 Medium | Simulated SOC event (medium) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |