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

