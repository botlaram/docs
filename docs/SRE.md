# 🧠 SRE (Site Reliability Engineering)

SRE is the practice of using software engineering to make systems reliable, scalable, and efficient.
It bridges the gap between development and operations by automating manual work and measuring reliability.

## 📏 SLI (Service Level Indicator)

“What we measure”

Definition: A measurement of how well a service is performing.
It tells you what the user is actually experiencing.

Example:

Availability (e.g., % of successful requests)

Latency (e.g., 95% of requests respond in <200 ms)

Error rate (e.g., % of failed logins)

Throughput (e.g., requests per second)

## 🎯 SLO (Service Level Objective) — “What we aim for”

Definition: A target value or range for an SLI that defines the desired level of service reliability.
It’s what you aim to achieve.

Example:

The system should have 99.9% availability per month.

The API should respond within 200 ms for 95% of requests.

## 🤝 SLA (Service Level Agreement) — “What we promise (legally)”

An SLA is usually a contract between you and your users/customers.
It defines the minimum service level you guarantee — and what happens if you fail.

💼 Example:

“We guarantee 99.5% uptime per month.

If we go below that, we’ll credit you 10% of your bill.

## Difference between Monitoring and Observibility

### 🔍 Monitoring — “Are we OK right now?”

Definition:
Monitoring means collecting and tracking predefined metrics to know if your system is healthy.  
It’s about detecting known problems.

Key idea: You already know what to look for.

Examples:

CPU usage above 90% → alert

Website response time > 2s → alert

Error rate > 1% → alert

Goal:
Detect when something goes wrong — and alert the right people.

Tools:
Prometheus, Grafana, Nagios, CloudWatch, Datadog, Zabbix

### 🧠 Observability — “Why aren’t we OK?”

Definition:
Observability means understanding what’s happening inside your system just by looking at the data it produces — even for problems you didn’t predict.  
It’s about exploration and debugging unknown issues.

Key idea: You might not know what to look for yet.

Examples:

Tracing a single user’s request across multiple microservices.

Investigating why latency suddenly spiked in one region.

Correlating logs, metrics, and traces to find the root cause.

Goal:
Help engineers ask new questions about the system and find unknown problems.

Tools:
OpenTelemetry, Grafana Tempo, Jaeger, Honeycomb, New Relic, Elastic Stack

⚙️ Simple Analogy

Concept	Analogy	Purpose
Monitoring	Like a car dashboard — it shows known indicators (fuel, speed, temperature).	Tells you when something’s wrong.  
Observability	Like a mechanic diagnosing the engine when the car makes a strange noise.	Helps you understand why it’s wrong.

🧩 Summary

| Aspect | Monitoring | Observability |
|--------|-------------|---------------|
| **Purpose** | Detect known issues | Explore and diagnose unknown issues |
| **Focus** | Metrics and alerts | Logs, metrics, and traces (the “three pillars”) |
| **Approach** | Reactive | Proactive |
| **Question answered** | “Is it working?” | “Why isn’t it working?” |

## What is Toil in SRE

**Toil** is the **manual, repetitive, and operational work** that keeps a system running —  
but **doesn’t add long-term value** to the system.

It’s the kind of work that:
- You have to do **over and over again**
- **Scales linearly** with the system (more servers = more toil)
- **Could be automated**, but isn’t (yet)

> In short: **Toil = repetitive work that keeps the lights on, not work that improves the lights.**

---

### Examples of Toil

| Type of Work | Toil Example | Why It’s Toil |
|---------------|--------------|----------------|
| Manual Operations | Restarting crashed servers every morning | Repetitive and should be automated |
| Deployment | Running manual deployment commands each release | Adds no lasting value |
| Monitoring | Manually checking dashboards for CPU usage | Can be replaced by alerts |
| Incident Response | Manually clearing disk space every week | Same problem keeps recurring |
| Support | Responding to the same user issue again and again | Could be automated with self-service tools |

---

### Non-Toil (Valuable) Work

| Type of Work | Example | Why It’s Valuable |
|---------------|----------|------------------|
| Automation | Writing a script to auto-restart crashed servers | Reduces future toil |
| System Improvement | Improving monitoring to detect issues earlier | Increases reliability |
| Optimization | Making deployments fully automated | Saves time long-term |

---

One of the **core goals of SRE** is to **reduce toil** through **automation and process improvement**.

> **Rule of Thumb:**  
> Toil should be **less than 50%** of an SRE’s time.  
> The rest should go into improving systems so future toil decreases.
> **Toil is doing the same manual task again and again, instead of fixing the root cause or automating it.**

---

### How to Measure Toil in SRE

Measuring toil means figuring out **how much of your team’s time** is spent doing **manual, repetitive operational work** — instead of **engineering improvements**.

The goal is to **quantify toil**, so you can:
- Justify automation work
- Prioritize improvements
- Ensure SREs focus on reliability, not busywork

---

#### 1. Define What Counts as Toil

**Toil Characteristics:**
- Manual (requires human intervention)
- Repetitive (done over and over)
- Reactive (responding to issues)
- Tactical (short-term fix, not long-term improvement)
- No enduring value (system state is the same after you finish)

✅ **Example (Counts as Toil):** Restarting a failed service manually.  
❌ **Not Toil:** Writing a script to auto-restart that service.

---

#### 2. Track Time Spent on Toil

Start simple: measure **how much time** engineers spend on toil tasks.

**Ways to track:**
- Self-reporting (log hours weekly)
- Ticket analysis (track operational vs. project work)
- Incident reviews (count repetitive manual actions)

**Example Metric:**  
“In the past month, 40% of our team’s time was spent on toil.”

---

#### 3. Categorize and Quantify Toil

| Category | Example Task | Estimated % of Time |
|-----------|---------------|--------------------|
| Deployments | Manual deploys to prod | 20% |
| Incidents | Restarting services | 15% |
| Monitoring | Checking dashboards | 10% |
| Maintenance | Clearing disk space | 5% |

---

#### 4. Set a Target or Threshold

SRE best practice:  
> Toil should be **less than 50%** of an SRE’s time.

If it’s higher, the team is likely overloaded with operational work.

---

#### 5. Reduce Toil and Re-Measure

Once you know where toil comes from:
- Automate manual steps (scripts, CI/CD, auto-remediation)
- Improve tooling (better dashboards, alerts, runbooks)
- Eliminate root causes (fix recurring incidents)
- Measure again every 1–2 months

---

#### Example Improvement

| Metric | Before | After Automation |
|--------|---------|------------------|
| Manual deployments per week | 10 | 1 |
| Time spent on deployment toil | 8 hrs | 1 hr |
| Total toil % of team time | 45% | 25% |

✅ This shows measurable improvement — clear ROI on automation.

---

#### Summary

> **Measure toil = track time spent on manual, repetitive work → categorize it → reduce it → track again.**

---

### SRE Toil Tracking Template (Markdown)

#### SRE Toil Tracking Template

| Date | Engineer | Toil Category | Task Description | Time Spent (hrs) | Frequency | Automation Possible? (Y/N) | Comments / Next Steps |
|------|-----------|----------------|------------------|------------------|------------|-----------------------------|-----------------------|
| 2025-11-10 | Alice | Incident Response | Restarted crashed web service | 2 | Daily | Y | Add auto-restart script |
| 2025-11-10 | Bob | Monitoring | Checked disk usage manually | 1 | Weekly | Y | Add disk alert rule |
| 2025-11-11 | Carol | Deployment | Ran manual release to prod | 3 | Biweekly | Y | Automate CI/CD pipeline |
| 2025-11-11 | Dan | Maintenance | Cleared old log files | 1 | Weekly | Y | Add log rotation config |

#### Summary for Week

| Category | Total Hours | % of Total | Notes |
|-----------|--------------|-------------|--------|
| Incident Response | 5 | 40% | Need better alerting |
| Deployment | 3 | 25% | Automate release pipeline |
| Monitoring | 2 | 15% | Add proactive alerting |
| Maintenance | 2 | 20% | Improve log cleanup |

**Total Toil Hours:** 12 hrs  
**Total Team Hours:** 40 hrs  
**Toil %:** 30%  
**Goal:** Keep below 50%
