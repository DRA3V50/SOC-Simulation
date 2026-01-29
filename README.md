# 🛡️ SOC Detection & Incident Automation

![XP Badge](https://img.shields.io/badge/XP:234%20H:14%20M:12%20L:17-blue)

---

## 🔹 About This Repository

This repository simulates a **modern Security Operations Center (SOC)** workflow, providing realistic alerting, ticketing, and incident tracking data. It is designed for:

- **SOC Training & Demonstrations** – simulate realistic alert flow for analysts.
- **Automation Testing** – experiment with alert generation, incident correlation, and data-driven dashboards.
- **Data Analytics & Visualization** – produce charts and tables for reporting KPIs.
- **Integration with SIEM/SOAR Tools** – practice automated ticket creation, alert prioritization, and response simulation.

The system **automatically generates alerts and tickets**, tracks their **severity**, calculates **alert velocity**, and identifies the **most frequently triggered hosts**, providing a full end-to-end workflow experience.

---

## 📊 Dashboard Overview

<img src="charts/severity_chart.svg?20260128232309" width="320" />
<table><tr><td valign='top'><b>Severity Overview</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Severity</th><th>Count</th><th>% of Total</th></tr><tr><td>🔴 High</td><td style='color:orange'>14</td><td>33%</td></tr><tr><td>🟠 Medium</td><td style='color:orange'>12</td><td>28%</td></tr><tr><td>🟢 Low</td><td style='color:orange'>17</td><td>40%</td></tr></table></td><td valign='top'><b>Top 5 Hosts</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Host</th><th>Count</th></tr><tr><td>HOST-29</td><td>2</td></tr><tr><td>HOST-67</td><td>2</td></tr><tr><td>HOST-25</td><td>1</td></tr><tr><td>HOST-45</td><td>1</td></tr><tr><td>HOST-66</td><td>1</td></tr></table></td><td valign='top'><b>Alert Velocity</b><br><table border='1' cellpadding='5' cellspacing='0'><tr><th>Window</th><th>Alerts</th></tr><tr><td>Last 24 Hours</td><td>21</td></tr><tr><td>All Time</td><td>43</td></tr></table></td></tr></table>

## 🎟️ Recent Alerts

| Date | Ticket | Alert | Severity | Event |
|------|--------|-------|---------|-------|
| 2026-01-28_20260128232309 | SOC-INC20260128-4796 | ALERT-20260128-8181 | <span style='color:red'>🔴 High</span> | Simulated SOC event (high) |
| 2026-01-28_20260128231951 | SOC-INC20260128-6433 | ALERT-20260128-2208 | <span style='color:green'>🟢 Low</span> | Simulated SOC event (low) |
| 2026-01-28_20260128231732 | SOC-INC20260128-9933 | ALERT-20260128-2160 | <span style='color:orange'>🟠 Medium</span> | Simulated SOC event (medium) |
| 2026-01-28_20260128231606 | SOC-INC20260128-1049 | ALERT-20260128-6566 | <span style='color:green'>🟢 Low</span> | Simulated SOC event (low) |
| 2026-01-28_20260128231404 | SOC-INC20260128-2292 | ALERT-20260128-3693 | <span style='color:green'>🟢 Low</span> | Simulated SOC event (low) |

## 🧰 Detection Rules

| Rule ID | Name | Severity | Description |
|---|---|---|---|
| DET-001 | Multiple Failed Logins | High | Detects multiple failed authentication attempts from the same host |