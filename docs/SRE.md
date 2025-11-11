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

