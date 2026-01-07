![XP Badge](https://img.shields.io/badge/XP:5%20H:0%20M:1%20L:0-blue)

# SOC Automation & Data Analytics Simulation

> Daily SOC / SIEM / SOAR automation simulating analyst-driven alert triage, ticket escalation, and incident response reporting.

This repository demonstrates:
- Automated alert generation (SIEM-style)
- Ticket creation & escalation (ServiceNow / Jira–like)
- SOAR playbook execution
- Severity-based analytics & visualization
- Daily reporting using GitHub Actions (EST)

---

## 📊 Alert Severity Distribution

![Alert Severity Chart](charts/severity_chart.svg)

> Chart updates automatically based on daily generated tickets and escalations.

---

## 🚨 Recent Alerts
| Date | Alert ID | Severity | Event |
|------|---------|----------|-------|
| 2026-01-06 | ALERT-2026-01-06 | Medium | Simulated SOC event (medium) |

---

## 🎟️ Ticketing & Escalation (SOC Workflow)
Each alert generates a corresponding ticket with:
- Severity classification
- Escalation logic
- Analyst decision tracking

Tickets are stored in `/tickets` and simulate platforms such as:
- ServiceNow
- Jira
- TheHive

---

## 🛠️ Automation & Analytics Focus
- Python-based automation
- Time-based execution (EST)
- Structured JSON datasets
- Severity aggregation & reporting
- Visual dashboards for analyst review

---

## 🎯 Target Roles
This repository emphasizes practical security operations concepts including alert triage, severity-based escalation, automation-driven response workflows, and structured data analysis.  
The project is designed to reflect real-world SOC environments where analysts rely on repeatable processes, accurate severity classification, and automated reporting to support investigation and decision-making.

---

_Last updated automatically via GitHub Actions_
