# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:1267%20🔴:74%20🟠:77%20🟢:71-blue)

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

<img src="charts/severity_chart.svg?20260427184031" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:red; font-weight:bold;'>74</td><td>33%</td></tr><tr><td>🟠 Medium</td><td style='color:orange; font-weight:bold;'>77</td><td>35%</td></tr><tr><td>🟢 Low</td><td style='color:green; font-weight:bold;'>71</td><td>32%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>6</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>6</td></tr><tr><td>HOST-39</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-62</td><td style='color:black; font-weight:bold;'>5</td></tr><tr><td>HOST-66</td><td style='color:black; font-weight:bold;'>5</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>2</td></tr><tr><td>All Time</td><td>222</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-04-27_20260427184031 | SOC-INC20260427-7245 | ALERT-20260427-4207 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-04-27_20260427072959 | SOC-INC20260427-1851 | ALERT-20260427-4065 | 🟠 Medium | Simulated SOC event (medium) |
| 2026-04-26_20260426182810 | SOC-INC20260426-2288 | ALERT-20260426-6645 | 🟢 Low | Simulated SOC event (low) |
| 2026-04-26_20260426063719 | SOC-INC20260426-2170 | ALERT-20260426-5512 | 🔴 High | Simulated SOC event (high) |
| 2026-04-25_20260425182622 | SOC-INC20260425-7432 | ALERT-20260425-7334 | 🟢 Low | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |