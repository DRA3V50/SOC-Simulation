# 🛡️ SOC Detection & Incident Data Automation

![XP Badge](https://img.shields.io/badge/XP:15%20H:1%20M:1%20L:0-blue)

Simulates a professional Security Operations Center workflow with automated ticketing using 🎟️ Jira and ServiceNow, alert escalation 🚨 based on severity, and data-driven analytics 📊 for SIEM, SOAR, EDR, and incident response.

---

## 🔹 Project Focus and Incident Correlation

- 🎟️ **Automated Ticketing & Alerts** – Generates daily tickets in Jira/ServiceNow format and simulates real incident intake.  
- 🚨 **Escalation & Prioritization** – Automatically classifies alerts High 🔴 / Medium 🟠 / Low 🟢 to guide analyst focus.  
- 📈 **Analytics & Visualization** – Counts alerts, calculates XP points, and generates severity charts 📊 to track trends.  
- 🔍 **Data Analysis** – Identifies patterns, recurring issues, and prioritizes incidents for investigation.  
- ⚙️ **Automation** – Fully automated via GitHub Actions to simulate daily SOC activity.  
- 📐 **SIEM Detection Rules** – Structured detection rules identify suspicious activity.  
- 🔄 **Incident Lifecycle Tracking** – Tracks events from detection to resolution, showing progress through New → Investigating → Escalated → Resolved → Closed.  
- 🔗 **Alert Correlation** – Groups related alerts into single incidents to reduce noise and improve analyst efficiency.  

---

## 📊 Alert Analytics

**Severity Distribution**

| Severity | Count |
|----------|-------|
| 🔴 High  | 1     |
| 🟠 Medium| 1     |
| 🟢 Low   | 0     |

---

## 📈 Chart Display

<img src="charts/severity_chart.svg" width="320" height="120" />

---

## 🎟️ Recent Tickets / Alerts

| Date       | Ticket ID 🎟️           | Alert ID 🚨         | Severity | Event                       |
|------------|------------------------|------------------|---------|-----------------------------|
| 2026-01-07 | SOC-INC20260107-5335   | ALERT-2026-01-07-1765 | 🔴 High | Simulated SOC event (high)  |
| 2026-01-06 | TICKET-2026-01-06      | ALERT-2026-01-06       | 🟠 Medium | Simulated SOC event (medium)|

---

## 🧰 Detection Rules

| Rule ID  | Name                    | Severity | Description                                        |
|----------|-------------------------|---------|---------------------------------------------------|
| DET-001  | Multiple Failed Logins   | High    | Detects multiple failed authentication attempts from the same host |

---

## 🔗 Correlated Incidents

| Incident ID | Related Alerts                  | Status        |
|------------|--------------------------------|--------------|
| INC-20260107-001 | ALERT-2026-01-07-1765, ALERT-2026-01-07-1766 | Investigating |

---

*Note: Daily automation updates tickets, alerts, and charts while keeping Detection & Correlation tables intact.*

