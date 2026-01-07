# 🛡️ SOC Threat Analytics & Data Automation

![XP Badge](https://img.shields.io/badge/XP:15%20H:1%20M:1%20L:0-blue)

> ⚡ Hands-on **SOC simulation**: automated ticketing 🎫, alert escalation 🚨, and data-driven analytics 📊—mirroring SIEM, SOAR, IR/EDR workflows used by Blue Teams.

---

## 🚀 Key Focus

- 🎫 **Automated Ticketing & Alerts** – Daily simulated incidents  
- 🔥 **Escalation & Prioritization** – High 🔴 / Medium 🟠 / Low 🟢 alerts  
- 📊 **Analytics & Visualization** – Severity charts & XP scoring  
- 🔍 **Data Analysis** – SOC/IR analyst-style pattern detection  
- 🤖 **Full Automation** – GitHub Actions updates repo daily  

---

## 📈 Alert Snapshot

| Severity | Count |
|----------|-------|
| 🔴 High  | 1     |
| 🟠 Medium| 1     |
| 🟢 Low   | 0     |

**📊 Severity Chart**

<img src="charts/severity_chart.svg" width="320" height="120" />

**📰 Recent Tickets / Alerts**

| Date       | Ticket 🎫 | Alert 🚨 | Severity | Event                       |
|------------|-----------|----------|----------|-----------------------------|
| 2026-01-07 | TICKET-2026-01-07 | ALERT-2026-01-07 | 🔴 High   | Simulated SOC event (high)  |
| 2026-01-06 | TICKET-2026-01-06 | ALERT-2026-01-06 | 🟠 Medium | Simulated SOC event (medium)|

---

## 🖥️ Run Locally

```bash
git clone <repo-url>
cd SOC-Simulation
pip install -r requirements.txt
python scripts/generate_daily.py
