![XP Badge](https://img.shields.io/badge/XP:5%20H:0%20M:1%20L:0-blue)

# SOC Automation & Data Analytics Simulation

Daily SOC / SIEM / SOAR automation simulating analyst-driven alert triage, ticket escalation, and incident response reporting.

This repository demonstrates:

- Automated alert generation (SIEM-style)
- Ticket creation & escalation (ServiceNow / Jira–like)
- SOAR playbook execution
- Severity-based analytics & visualization
- Daily reporting using GitHub Actions (EST)

---

## 📌 Project Scope

This simulation focuses on daily security operations workflows commonly found in enterprise and government environments.  
It emphasizes alert normalization, severity-based escalation, and repeatable automation used to support analyst investigation and incident response decision-making.

The repository is intentionally lightweight, data-driven, and structured to resemble operational SOC tooling rather than standalone scripts.

---

## 📊 Alert Severity Distribution

Alert severity is aggregated from daily generated tickets and visualized automatically.

The chart reflects analyst-style escalation logic based on alert criticality and updates on each scheduled run.

---

## 🚨 Recent Alerts

| Date | Alert ID | Severity | Event |
|------|---------|----------|-------|
| 2026-01-06 | ALERT-2026-01-06 | Medium | Simulated SOC event (medium) |

---

## 🎟️ Ticketing & Escalation Workflow

Each alert generates a corresponding ticket containing:

- Severity classification
- Escalation logic
- Analyst decision tracking

Tickets are stored as structured JSON under `/tickets` and simulate enterprise case management platforms such as:

- ServiceNow  
- Jira  
- TheHive  

---

## 📂 Data & Detection Logic

Alerts and tickets are generated using structured JSON schemas to simulate normalized SIEM output.  
Severity assignment reflects simplified detection logic based on behavioral indicators and escalation thresholds.

This approach enables:

- Consistent severity classification
- Trend analysis over time
- Automation-friendly reporting
- Downstream enrichment and correlation

The data model is designed to support future expansion into log parsing, detection tuning, and anomaly-based analysis.

---

## 🛠️ Automation & Analytics Design

This project emphasizes repeatable, analyst-friendly automation patterns, including:

- Python-based workflow orchestration
- Time-based execution aligned to EST
- Structured datasets for analysis and reporting
- Severity aggregation across alert lifecycles
- Lightweight visual dashboards for daily SOC review

The overall design mirrors real SOC environments where automation supports analyst judgment, escalation accuracy, and operational reporting.

---

_Last updated automatically via GitHub Actions_
