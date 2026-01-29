# 🛡️ SOC-Analytics-Dashboard

![XP Badge](https://img.shields.io/badge/XP:239%20🚨:14%20⚠️:13%20✅:17-blue)

---

## 🔹 Purpose
SOC-Analytics-Dashboard simulates a **Security Operations Center (SOC)** for realistic incident tracking and blue team training.  
It provides:

- Automated ticketing & alert generation  
- Severity prioritization 🚨⚠️✅  
- Tracking top hosts 🖥️  
- Alert velocity monitoring ⏱️  
- Daily dashboards with historical trends  

---

## 🧩 How It Works
- **Telemetry:** Simulates alerts for multiple hosts  
- **Analytics:** Counts severity, calculates percentages, and tracks top hosts  
- **Visualization:** Generates color-coded SVG dashboards  
- **Automation:** GitHub Actions updates daily; all data preserved

---

## 📊 Dashboard Overview

<img src="charts/severity_chart.svg?20260128232611" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🚨 High</td><td style='color:red; font-weight:bold;'>14</td><td>32%</td></tr><tr><td>⚠️ Medium</td><td style='color:orange; font-weight:bold;'>13</td><td>30%</td></tr><tr><td>✅ Low</td><td style='color:green; font-weight:bold;'>17</td><td>39%</td></tr></table></td><td valign='top'><b>Top 5 Hosts 🖥️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-67</td><td style='color:black; font-weight:bold;'>2</td></tr><tr><td>HOST-25</td><td style='color:black; font-weight:bold;'>1</td></tr><tr><td>HOST-45</td><td style='color:black; font-weight:bold;'>1</td></tr><tr><td>HOST-66</td><td style='color:black; font-weight:bold;'>1</td></tr></table></td><td valign='top'><b>Alert Velocity ⏱️</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>22</td></tr><tr><td>All Time</td><td>44</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-01-28_20260128232611 | SOC-INC20260128-1050 | ALERT-20260128-6946 | <span style='color:orange'>⚠️ Medium</span> | Simulated SOC event (medium) |
| 2026-01-28_20260128232309 | SOC-INC20260128-4796 | ALERT-20260128-8181 | <span style='color:red'>🚨 High</span> | Simulated SOC event (high) |
| 2026-01-28_20260128231951 | SOC-INC20260128-6433 | ALERT-20260128-2208 | <span style='color:green'>✅ Low</span> | Simulated SOC event (low) |
| 2026-01-28_20260128231732 | SOC-INC20260128-9933 | ALERT-20260128-2160 | <span style='color:orange'>⚠️ Medium</span> | Simulated SOC event (medium) |
| 2026-01-28_20260128231606 | SOC-INC20260128-1049 | ALERT-20260128-6566 | <span style='color:green'>✅ Low</span> | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |