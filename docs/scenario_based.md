# Scenario Based Question

## Terraform

### You have 50 Terraform resources created using a Jenkins pipeline, and the pipeline takes more than 5 hours to complete. How would you reduce the build time?

Enable Parallelism in Terraform

By default, Terraform applies resources sequentially.
You can increase the number of parallel operations using the -parallelism flag.

```bash
terraform apply -parallelism=20
```

Default is 10. Increasing it allows Terraform to create independent resources concurrently.

However, it must be tuned carefully — too high may overload the backend or API rate limits.

### What is a Module?

A module in Terraform is a container for multiple resources that are used together.
It allows reusability, organization, and consistency across environments (dev, test, prod).

Type	              | Description
Root Module         |	The directory where you run terraform init, plan, or apply. It contains main Terraform configuration files like main.tf, variables.tf, and outputs.tf.
Child Module	      | A reusable module defined in a separate directory (or from a remote source) and called by the root module using the module block.

Folder structure

```bash
terraform-project/
│
├── main.tf                # Root module
├── variables.tf
├── outputs.tf
│
└── modules/
|   └── ec2-instance/      # Child module
|       ├── main.tf
|       ├── variables.tf
|       └── outputs.tf
└── modules/
    └── vpc/      # Child module
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```
Step 1 — Create a Child Module

📁 modules/ec2-instance/main.tf

```bash
resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = var.instance_type
  tags = {
    Name = var.instance_name
  }
}
```

📁 modules/ec2-instance/variables.tf

```bash
variable "ami" {
  description = "AMI ID for the EC2 instance"
  type        = string
}

variable "instance_type" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t2.micro"
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
}
```

📁 modules/ec2-instance/outputs.tf

```bash
output "instance_id" {
  description = "The ID of the created EC2 instance"
  value       = aws_instance.example.id
}
```

Step 2 — Use the Child Module in the Root Module

📁 main.tf (Root Module)

```bash
provider "aws" {
  region = var.region
}

# Using the child module
module "web_server" {
  source         = "./modules/ec2-instance"
  ami            = var.ami
  instance_type  = var.instance_type
  instance_name  = "web-server"
}

output "web_server_id" {
  value = module.web_server.instance_id
}
```

📁 variables.tf

```bash
variable "region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "ami" {
  description = "AMI ID for EC2 instance"
  type        = string
  default     = "ami-0c55b159cbfafe1f0"  # Example Amazon Linux 2 AMI
}

variable "instance_type" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t3.micro"
}
```

📁 outputs.tf

```bash
output "instance_id" {
  description = "ID of the EC2 instance created via module"
  value       = module.web_server.instance_id
}
```

Step 3: Run the Terraform Commands

```bash
terraform init      # Initialize and download providers & modules
terraform plan      # Show what will be created
terraform apply
```

Use Remote Module (Example from GitHub)

You can also source a module remotely:

```bash
module "network" {
  source  = "git::https://github.com/example-org/terraform-aws-vpc.git?ref=v1.0.0"
  cidr_block = "10.0.0.0/16"
  environment = "dev"
}
```

### Your Terraform state file (terraform.tfstate) got corrupted. What will you do?

1. Don’t run terraform apply immediately — it can worsen the situation.
2. Check if you have state file backups:
    Local backend → .terraform/backup/
    S3 backend → Versioning-enabled bucket.
3. Restore the last known good version:

```bash
aws s3 cp s3://bucket/path/terraform.tfstate <restore-location>
```

4. If partial corruption → try manual fix by editing JSON carefully.
5. If full recovery not possible → use terraform import to rebuild the state from real infrastructure.

### Someone manually changed a resource in the cloud outside Terraform. How do you detect and fix it?

```bash
## run
terraform plan
```

Terraform will detect the drift and show differences.

Revert the manual change by re-applying:

```bash
terraform apply
```

Or, if the manual change is correct, update the Terraform configuration and re-run plan.

### Two team members applied Terraform changes to the same module at the same time. One of the applies failed. How can you prevent this?

Use state locking in your backend.
Example: AWS S3 + DynamoDB backend setup

```bash
backend "s3" {
  bucket         = "tf-state-bucket"
  key            = "prod/terraform.tfstate"
  region         = "us-east-1"
  dynamodb_table = "terraform-locks"
}
```

The DynamoDB lock prevents simultaneous apply operations.

Educate team to use:

```bash
terraform plan -out=tfplan
terraform apply tfplan
```

to ensure reproducible state.

The terraform apply tfplan command in Terraform is used to execute a previously generated execution plan. This command is crucial for applying infrastructure changes in a controlled and predictable manner, especially in automated pipelines or when a plan needs to be reviewed and approved before deployment.

Here's how it works:

1. Generate a plan: First, you create an execution plan using terraform plan -out tfplan, where tfplan is the name of the file where the plan will be saved. This command analyzes your Terraform configuration and the current state of your infrastructure to determine the actions (create, update, or destroy) required to reach the desired state.
2. Review the plan: The saved tfplan file can be reviewed using terraform show tfplan to understand the exact changes Terraform intends to make. This step is critical for ensuring that the proposed changes align with your expectations and do not introduce unintended consequences.
3. Apply the plan: Once the plan is reviewed and approved, you can execute it using terraform apply tfplan. Terraform will then perform the actions defined in the tfplan file, making the necessary changes to your infrastructure and updating the Terraform state file to reflect the new state of your resources.

### During terraform apply, some resources were created successfully, while others failed. What would you do next?

First, don’t destroy everything.

Run:
```bash
terraform apply
```

again — Terraform will detect already created resources and continue where it left off.

If still failing:

Use `terraform taint <resource>` to mark specific failed resources for recreation.

Or use `terraform state rm` to remove manually created resources if needed.

Always review the terraform plan output before reapplying.

### You already have an AWS EC2 instance created manually. How can you bring it under Terraform management?

Write the Terraform configuration that represents that instance:

```bash
## add resource in main.tf
resource "aws_instance" "web" {
  ami           = "ami-0abc12345"
  instance_type = "t2.micro"
}

## Run the import command:
terraform import aws_instance.web i-0abcd1234ef56789

## Now Terraform tracks it in state — verify with:
terraform state show aws_instance.web
```

### Large State File & Performance Issues

Your Terraform state file has grown large and plan is getting slow. How do you optimize?

1. Split your infrastructure into multiple smaller states (e.g., per environment or per component).
2. Use data sources instead of having everything in a single root module.
3. Enable state file compression and remote backends.
4. Use `terraform plan -target` for selective planning if needed temporarily (but not as long-term solution).

### How do you handle secrets in Terraform without exposing them in Git?

Store them in Azure Key Vault, AWS Secrets Manager, or Vault, and use data sources to fetch:

```bash
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "my-db-password"
}

variable "db_password" {
  default = data.aws_secretsmanager_secret_version.db_password.secret_string
}
```

Never hardcode secrets or commit .tfvars files with credentials. Use environment variables:

```bash
export TF_VAR_db_password="supersecret"
```

### Create a terraform workspace with dev and prod and configure backend file for dev and prod

Project structure

```bash
terraform-project/
│
├── main.tf
├── variables.tf
├── outputs.tf
├── backend.tf
│
├── modules/
│   └── ec2_instance/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
│
└── environments/
    ├── dev.tfvars
    └── prod.tfvars
```


🧩 Step 1: Define a Module (Example: EC2 Instance)

modules/ec2_instance/main.tf

```bash
resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = var.instance_type
  tags = {
    Name = "${var.env}-instance"
  }
}
```

modules/ec2_instance/variables.tf

```bash
variable "ami" {
  type        = string
  description = "AMI ID for the instance"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
}

variable "env" {
  type        = string
  description = "Environment name"
}
```

modules/ec2_instance/outputs.tf

```bash
output "instance_id" {
  value = aws_instance.example.id
}
```

⚙️ Step 2: Root Configuration

backend.tf

```bash
terraform {
  backend "s3" {
    bucket = "your-terraform-state-bucket"
    key    = "workspace-example/terraform.tfstate"
    region = "us-east-1"
  }
}
```

main.tf

```bash
provider "aws" {
  region = "us-east-1"
}

module "ec2" {
  source         = "./modules/ec2_instance"
  ami            = var.ami
  instance_type  = var.instance_type
  env            = terraform.workspace
}
```

variables.tf

```bash
variable "ami" {
  type        = string
  description = "AMI ID"
}

variable "instance_type" {
  type        = string
  description = "EC2 instance type"
}
```

outputs.tf

```bash
output "instance_id" {
  value = module.ec2.instance_id
}
```

🌍 Step 3: Environment Variable Files

environments/dev.tfvars

```bash
ami            = "ami-0c55b159cbfafe1f0"
instance_type  = "t2.micro"
```

environments/prod.tfvars

```bash
ami            = "ami-0d527b8c289b4af7f"
instance_type  = "t3.medium"
```

🚀 Step 4: Create and Use Workspaces

```bash
# Initialize Terraform
terraform init

# Create workspaces
terraform workspace new dev
terraform workspace new prod

# Switch to dev
terraform workspace select dev
terraform apply -var-file=environments/dev.tfvars

# Switch to prod
terraform workspace select prod
terraform apply -var-file=environments/prod.tfvars
```

✅ Result:

You now have a single Terraform configuration that:

Uses modules for reusable infrastructure logic.

Uses workspaces (dev, prod) to isolate state.

Uses environment variable files to customize settings

⚙️ Step 5: Configure Terraform Backend for Azure Blob

backend.tf

```bash
terraform {
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstateacct12345"
    container_name       = "tfstate"
    key                  = "terraform.${terraform.workspace}.tfstate"
  }
}
```

🔍 What happens here:

terraform.workspace dynamically names the state file.

When you use the dev workspace → state file = terraform.dev.tfstate

When you use the prod workspace → state file = terraform.prod.tfstate

🧩 Step 6: Initialize the Backend

After setting up the backend:

```bash
terraform init \
  -backend-config="resource_group_name=tfstate-rg" \
  -backend-config="storage_account_name=tfstateacct12345" \
  -backend-config="container_name=tfstate" \
  -backend-config="key=terraform.tfstate"
```

Then create workspaces:

```bash
terraform workspace new dev
terraform workspace new prod
```

🌍 Step 7: Apply per Environment

Use workspace + var files:

```bash
# Switch to dev
terraform workspace select dev
terraform apply -var-file=environments/dev.tfvars

# Switch to prod
terraform workspace select prod
terraform apply -var-file=environments/prod.tfvars
```

## Kubernetes

### Whats difference between loadbalancer and ingress in kubernetes?

LoadBalancer: It exposes your application externally (outside the cluster) by provisioning a cloud load balancer (like AWS ELB, Azure Load Balancer, GCP Load Balancer).

When you create a Service of type LoadBalancer, Kubernetes asks your cloud provider to create an external load balancer.

The load balancer forwards traffic to the Service, which then routes it to the right Pods.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-lb
spec:
  type: LoadBalancer
  selector:
    app: my-app
  ports:
    - port: 80
      targetPort: 8080
```

Result:
→ Cloud provider creates a load balancer (e.g., with an external IP)
→ Traffic to that IP goes to your app pods.

✅ Pros

Simple to set up.

Directly exposes your app to the internet.

⚠️ Cons

Each service of type LoadBalancer creates a separate cloud load balancer — expensive and not scalable if you have many services.

Limited control over routing (just ports).

Ingress: It’s an HTTP/HTTPS reverse proxy that manages external access to multiple services — typically at Layer 7 (application layer).

You deploy an Ingress Controller (like NGINX, HAProxy, Traefik, or the cloud provider’s ingress).

You define Ingress rules that tell it how to route incoming requests based on:

Hostnames (e.g., api.example.com)

Paths (e.g., /api, /web)

The Ingress Controller usually runs behind a single LoadBalancer.

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
      - path: /web
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

Result:
→ One LoadBalancer (via the ingress controller) handles requests for many services.
→ Routes based on domain name and path.

✅ Pros

Single entry point for all services.

Advanced routing (paths, hostnames, SSL termination, etc.).

Cost-effective (only one LoadBalancer needed).

⚠️ Cons

Requires setting up an Ingress Controller.

More complex configuration.

### Explain taints and tolerence

In Kubernetes (k8s), taints and tolerations are a way to control which pods can be scheduled onto which nodes — they’re essentially the inverse of node selectors and affinity rules.

Think of it like this:

Node labels / affinity = "Please put me on this kind of node" (pod’s request)

Taints / tolerations = "Stay away unless you have permission" (node’s warning)

1. What is a taint?

A taint is a property you put on a node that says:

"I won’t accept pods unless they tolerate this taint."

It’s defined by three parts:

```bash
key=value:effect
```

Where:

```bash
key → Identifier (e.g., dedicated)

value → Description of the taint (e.g., gpu-workload)

effect → One of:

NoSchedule → Don’t schedule pods unless they tolerate it.

PreferNoSchedule → Avoid scheduling pods unless no better option exists.

NoExecute → Evict existing pods that don’t tolerate it and stop new ones from being scheduled.
```

Example command to add a taint:

```bash
kubectl taint nodes node1 dedicated=gpu-workload:NoSchedule
```

2. What is a toleration?

A toleration is a property you add to a pod that says:

"I’m okay with being scheduled on nodes that have this taint."

It’s defined in the pod’s YAML spec:

```bash
tolerations:
- key: "dedicated"
  operator: "Equal"
  value: "gpu-workload"
  effect: "NoSchedule"
```

This tells Kubernetes: “If a node has the taint dedicated=gpu-workload:NoSchedule, I can still go there.”

3. How they work together

Without a toleration → Pod cannot be scheduled on a node with a matching taint.

With a matching toleration → Pod can be scheduled on the tainted node, but not forced — Kubernetes still considers other scheduling rules.

Example scenario:

Node is tainted: dedicated=gpu-workload:NoSchedule

Normal pods (no toleration) → won’t land there.

GPU job pods (with toleration) → can land there.

4. Why use taints & tolerations?

Dedicated nodes for specific workloads (e.g., GPU, high-memory, compliance-sensitive).

Isolating workloads (e.g., separate dev/test from prod).

Evicting pods during maintenance (NoExecute).

### Network Flow 

You’ve deployed your web app (say, a website running on Nginx or Node.js) into Kubernetes.  
Your goal: people on the internet should be able to open https://myapp.com and see your site.

🚀 Step-by-step flow

1️⃣ User makes a request

1. A user types https://myapp.com in their browser.  
2. The browser asks the DNS to find where myapp.com lives.
3. DNS points it to a public IP — that’s your Kubernetes LoadBalancer or Ingress Controller.

2️⃣ Request reaches Kubernetes

1. The request enters your Kubernetes cluster through one of these:
2. A LoadBalancer (provided by your cloud provider like AWS, Azure, or GCP)
3. Or an Ingress Controller (like Nginx or Traefik)

3️⃣ Ingress / LoadBalancer sends it to a Service

1. Inside Kubernetes, you have a Service that knows which app (Pods) should get this request.
2. The Service acts like a traffic director.
3. It decides which Pod (copy of your app) will handle the request.

4️⃣ Service forwards the request to a Pod

1. The Pod is where your web app actually runs — it’s like a small computer running your app container.
2. Each Pod has its own internal IP address.
3. The Service forwards the request to one of the Pods using that IP.
4. Kubernetes automatically load-balances between Pods (if you have multiple replicas).

5️⃣ Pod handles the request

1. Inside the Pod, your web server or app container (like Nginx or Flask or Node.js) receives the HTTP request on a port — for example, port 8080.
2. It processes the request (maybe fetches some data, renders HTML) and sends back a response.

6️⃣ Response goes back the same way

The response travels backward:

Pod → Service → Ingress/LoadBalancer → Internet → User's Browser


## Azure

### Difference between application gateway and load balancer 

🔹 High-Level Difference

| Feature	 | Azure Load Balancer	| Azure Application Gateway |
|---------|-----------------------|-----------------------------| 
| OSI Layer	 | Layer 4 (Transport Layer: TCP/UDP)		|Layer 7 (Application Layer: HTTP/HTTPS) 	|
Routing Type	| Based on IP address and port		|Based on HTTP(S) content (URL, headers, cookies, etc.)	|
Primary Use Case |	Distributes network traffic across backend servers	|	Provides web traffic routing, SSL termination, WAF (security), and URL-based routing	|
Protocol Support	| TCP, UDP	|	HTTP, HTTPS, WebSocket	|
SSL/TLS Termination	| ❌ Not supported	| ✅ Supported	|
Web Application Firewall (WAF)		| ❌ Not available	|	✅ Integrated WAF option	|
Health Probes	|	Checks TCP/port connectivity	|	Checks application-level health (HTTP response codes, paths)	|
Session Affinity	|	✅ Supported (by source IP)		|✅ Supported (by cookies)	|
URL Path-Based Routing	|	❌ Not possible		|✅ Possible	|
Redirection (HTTP to HTTPS, etc.)	|	❌ Not supported	|	✅ Supported	|
Typical Scenario	|	Internal or external non-HTTP traffic load balancing (e.g., databases, custom TCP apps)	|	Web application routing and protection for websites, APIs, or web apps	|

🔸 Example Use Cases

🔹 Azure Load Balancer

Balancing traffic between VMs running non-HTTP workloads — e.g.:

- SQL servers

- FTP servers

- Gaming servers

- Custom TCP/UDP-based apps

Backend VM access in an internal network (internal load balancer)

Simple, high-performance layer-4 traffic distribution

🔹 Azure Application Gateway

- Fronting web applications (HTTP/HTTPS)

- Terminating SSL to reduce load on backend servers

- URL path-based routing (e.g., /api → API backend, /images → static server)

- Protecting against web attacks using Web Application Firewall (WAF)

- Redirecting HTTP → HTTPS

- Hosting multiple websites using one gateway (multi-site routing)

🔹 Can they work together?

You can use both in combination:

- Application Gateway (Layer 7) → routes and secures web traffic

- Azure Load Balancer (Layer 4) → distributes that traffic to backend VMs or containers

This layered approach improves both performance and security.

🧠 Quick Summary

| Question	     | Answer |
-----------------|-----------------|
| What layer does it work on?	| Load Balancer = Layer 4, Application Gateway = Layer 7 |
| What does it understand? |	Load Balancer = IP/Port, Application Gateway = HTTP(S) requests |
| Can it inspect or modify requests? |	Only Application Gateway |
| Can it protect web apps (WAF)? |	Only Application Gateway |

### When to use which database

| **Database Type** | **Azure Service** | **AWS Equivalent** | **Description / Purpose** | **Best Use Cases** | **Key Features** |
|--------------------|------------------|--------------------|----------------------------|--------------------|------------------|
| **Relational (SQL Server)** | **Azure SQL Database** | **Amazon RDS for SQL Server** | Fully managed relational DB-as-a-service built on SQL Server. | - OLTP apps<br>- Web & enterprise systems<br>- Structured schema & ACID compliance | - Auto scaling<br>- High availability<br>- Built-in security & backups |
| **Open Source Relational (MySQL)** | **Azure Database for MySQL** | **Amazon RDS for MySQL / Aurora MySQL** | Managed open-source MySQL DB service. | - Web & CMS apps<br>- LAMP stack<br>- Cross-platform compatibility | - Fully managed<br>- Auto backup & patching<br>- High availability |
| **Open Source Relational (PostgreSQL)** | **Azure Database for PostgreSQL** | **Amazon RDS for PostgreSQL / Aurora PostgreSQL** | Managed PostgreSQL service. | - Geospatial apps<br>- Data analytics<br>- Django / Flask apps | - Open-source compatible<br>- Built-in HA<br>- Autoscaling |
| **Open Source Relational (MariaDB)** | **Azure Database for MariaDB** | **Amazon RDS for MariaDB** | Managed MariaDB service. | - Existing MariaDB workloads<br>- Web applications | - Managed MariaDB<br>- Easy migration<br>- Security integrated |
| **NoSQL (Multi-model)** | **Azure Cosmos DB** | **Amazon DynamoDB** | Globally distributed, multi-model NoSQL database (document, key-value, graph, column). | - IoT & real-time apps<br>- Global scale, low latency<br>- JSON document storage | - Multi-region replication<br>- Guaranteed low latency<br>- Horizontal scaling |
| **Big Data / Analytics Warehouse** | **Azure Synapse Analytics** | **Amazon Redshift** | Cloud-based enterprise data warehouse for analytics and BI. | - Data warehousing<br>- Business intelligence<br>- ETL workloads | - MPP architecture<br>- Integrates with Power BI<br>- Serverless options |
| **In-Memory Cache** | **Azure Cache for Redis** | **Amazon ElastiCache for Redis / Memcached** | Managed, in-memory cache for fast data access. | - Caching<br>- Session storage<br>- Real-time analytics | - Sub-millisecond latency<br>- Scalable performance<br>- Pub/Sub messaging |
| **Time-Series / Log Analytics** | **Azure Data Explorer (ADX)** | **Amazon Timestream** | Optimized for time-series and log data ingestion and querying. | - IoT telemetry<br>- Monitoring & logging<br>- Analytics dashboards | - KQL query language<br>- Fast ingestion<br>- Real-time queries |
| **Graph Database** | **Azure Cosmos DB (Gremlin API)** | **Amazon Neptune** | Graph database for highly connected data. | - Social networks<br>- Fraud detection<br>- Knowledge graphs | - Gremlin query support<br>- Multi-model flexibility<br>- Global scalability |
| **Data Lake / Object Storage** | **Azure Data Lake Storage (ADLS)** | **Amazon S3 / AWS Lake Formation** | Data lake for storing unstructured and big data. | - Data science<br>- ML pipelines<br>- Big data processing | - Unlimited storage<br>- Hadoop compatible<br>- Cost effective |
| **Search Engine / Indexing** | **Azure Cognitive Search** | **Amazon OpenSearch Service (Elasticsearch)** | Full-text search & AI-powered content indexing. | - App & site search<br>- Product catalogs<br>- Knowledge mining | - AI enrichment<br>- Integration with Blob, SQL, Cosmos<br>- Fast indexing |
| **Ledger / Immutable Records** | **Azure Confidential Ledger** | **Amazon QLDB (Quantum Ledger DB)** | Immutable, tamper-proof ledger for auditable transactions. | - Financial systems<br>- Compliance logs<br>- Auditing | - Cryptographic verification<br>- Managed ledger<br>- High security |


### Azure Networking Services — Types, Use Cases & AWS Equivalents

| **Network Type / Service** | **Azure Service Name** | **Description / Purpose** | **When to Use** | **Common Use Case Example** | **AWS Equivalent** |
|-----------------------------|------------------------|----------------------------|-----------------|------------------------------|--------------------|
| **Virtual Network (VNet)** | **Azure Virtual Network (VNet)** | Core private network in Azure that allows Azure resources (VMs, databases, etc.) to securely communicate. | When you need a private, isolated network in Azure. | Hosting web apps, databases, and VMs within the same secure subnet. | **Amazon VPC (Virtual Private Cloud)** |
| **Subnet** | **Azure Subnet (inside VNet)** | Logical segmentation of a VNet into smaller address spaces. | To organize and isolate workloads (frontend, backend, DB). | Separate subnet for web servers, app servers, and DB. | **AWS Subnet (inside VPC)** |
| **Network Security Group (NSG)** | **Azure NSG** | Acts as a virtual firewall to control inbound/outbound traffic at subnet or NIC level. | When you need granular control over traffic. | Allow only HTTP/HTTPS to web subnet, block others. | **AWS Security Group / NACL** |
| **Application Gateway (Layer 7)** | **Azure Application Gateway** | Layer 7 load balancer with Web Application Firewall (WAF). | For web traffic routing, SSL termination, and WAF protection. | Distribute web traffic between multiple app servers. | **AWS Application Load Balancer (ALB)** |
| **Load Balancer (Layer 4)** | **Azure Load Balancer** | Distributes network traffic (TCP/UDP) across multiple VMs. | For internal/external traffic balancing at network layer. | Balancing requests between backend VM instances. | **AWS Network Load Balancer (NLB)** |
| **VPN Gateway** | **Azure VPN Gateway** | Secure site-to-site or point-to-site encrypted connection between on-premises and Azure. | When connecting Azure network to on-prem data center securely. | Hybrid setup with on-prem servers and Azure VMs. | **AWS VPN Gateway** |
| **ExpressRoute** | **Azure ExpressRoute** | Dedicated private fiber connection between on-prem data center and Azure. | For enterprise-grade, low-latency, high-security private connection. | Banking or healthcare workloads requiring guaranteed performance. | **AWS Direct Connect** |
| **Firewall / Security Appliance** | **Azure Firewall** | Managed network firewall for centralized policy control and logging. | When you need enterprise-grade protection across VNets. | Centralized firewall protecting all workloads. | **AWS Network Firewall** |
| **Private Endpoint / Link** | **Azure Private Link** | Enables private access to Azure services via private IPs. | To access Azure services (Storage, SQL) privately without public internet. | Accessing Azure SQL Database securely from VNet. | **AWS PrivateLink** |
| **Traffic Manager (DNS-based routing)** | **Azure Traffic Manager** | Global DNS load balancer for routing traffic based on geography, latency, or priority. | For distributing traffic across multiple Azure regions. | Global app with users in multiple continents. | **AWS Route 53 (Latency / Geo Routing)** |
| **Application Gateway + Front Door** | **Azure Front Door** | Global load balancer and CDN for web applications. | For global, high-availability web applications with caching. | Multi-region web app with CDN acceleration. | **AWS CloudFront + Global Accelerator** |
| **Bastion Host** | **Azure Bastion** | Provides secure RDP/SSH access to VMs via browser (no public IP). | For secure remote access to Azure VMs. | Admins accessing VMs without exposing them publicly. | **AWS Systems Manager Session Manager / AWS Bastion Host** |
| **DNS Zone** | **Azure DNS** | Host and manage DNS records for your domains within Azure. | When managing custom domains within Azure. | Hosting `myapp.com` DNS zone inside Azure. | **Amazon Route 53 (DNS Management)** |
| **Peering / Hub-Spoke Network** | **VNet Peering / Hub-Spoke Architecture** | Connect multiple VNets for cross-communication with low latency. | When you have multiple VNets (apps, DBs, regions). | Multi-environment (Dev/Test/Prod) network design. | **AWS VPC Peering / Transit Gateway** |
| **Content Delivery Network (CDN)** | **Azure CDN** | Delivers content from edge servers close to users. | For fast delivery of static web content globally. | Serving website images, videos, scripts. | **AWS CloudFront** |
| **NAT Gateway** | **Azure NAT Gateway** | Provides outbound internet access for private resources without exposing inbound access. | For VMs that need outbound access securely. | VM in private subnet accessing internet APIs. | **AWS NAT Gateway** |
| **Virtual WAN (Global Network)** | **Azure Virtual WAN** | Simplifies connectivity between multiple branches, VNets, and on-prem sites. | For global enterprise networks with many sites. | Connecting multiple branch offices to Azure. | **AWS Transit Gateway / AWS Cloud WAN** |
| **Hybrid Storage Gateway** | **Azure File Sync**, **Azure Files**, **Azure Blob Storage**, **Azure NetApp Files**, **Azure Data Box**, **Azure Backup** | Provides hybrid on-prem ↔ cloud storage scenarios: cache and sync on-prem file shares to cloud, archive/tape replacement, bulk data transfer. Azure combines these services to cover AWS Storage Gateway modes (file, volume, tape). | - **File caching / sync**: Azure File Sync + Azure Files (SMB).<br>- **Block/volume storage**: Azure NetApp Files / Managed Disks.<br>- **Archive/tape replacement**: Azure Blob (cool/archive) + Azure Backup.<br>- **Offline bulk transfer**: Azure Data Box. | **AWS Storage Gateway (File / Volume / Tape Gateway)** |

### Azure Cost Management & Optimization Services — With AWS Equivalents

| **Category / Resource** | **Azure Service / Feature** | **Purpose / Description** | **When to Use** | **Common Use Case Example** | **AWS Equivalent** |
|--------------------------|-----------------------------|----------------------------|-----------------|------------------------------|--------------------|
| **Cost Monitoring & Analysis** | **Azure Cost Management + Billing** | Built-in tool to track, analyze, and optimize Azure spending. Provides cost breakdown by resource, service, and subscription. | To monitor and analyze cloud costs across subscriptions, resource groups, or management groups. | View monthly cost reports, forecast future spending, and analyze cost by department. | **AWS Cost Explorer** |
| **Budgets & Alerts** | **Azure Budgets** | Set spending limits with automated alerts when thresholds are reached. | To control overspending and trigger notifications or automation. | Set $10,000/month budget for dev environment, send alert at 80% spend. | **AWS Budgets** |
| **Pricing & Estimation Tool** | **Azure Pricing Calculator** | Estimate cost before deployment; simulate different configurations and services. | During planning or proposal phases to estimate future Azure costs. | Estimate total monthly cost for new VM setup. | **AWS Pricing Calculator** |
| **Advisor Recommendations** | **Azure Advisor (Cost Recommendations)** | AI-driven insights to optimize cost by right-sizing resources, removing idle VMs, etc. | When you want actionable cost-saving recommendations. | Reduce VM size or shut down unused VMs to save cost. | **AWS Trusted Advisor (Cost Optimization)** |
| **Reserved Instances / Savings Plans** | **Azure Reservations** | Prepay for 1 or 3 years to save up to 70% on VM, SQL, or App Service costs. | For predictable workloads running continuously. | Reserve VM instances for steady-state production workloads. | **AWS Reserved Instances / Savings Plans** |
| **Spot Instances (Low-cost Compute)** | **Azure Spot VMs** | Use unused Azure compute capacity at deep discounts. Can be evicted anytime. | For non-critical, batch, or test workloads tolerant to interruptions. | Run test jobs or render farms cheaply. | **AWS EC2 Spot Instances** |
| **Auto-Scaling** | **Azure Autoscale (in VMSS / App Service)** | Automatically scale compute up/down based on demand to control cost. | For variable or seasonal workloads. | Scale out web servers during peak traffic, scale in after hours. | **AWS Auto Scaling / EC2 Auto Scaling** |
| **Resource Tagging** | **Azure Tags** | Add metadata (like cost center, owner, environment) for cost tracking and governance. | To allocate and report costs by department, project, or environment. | Tag all resources with “Dept:Finance” for chargeback reports. | **AWS Resource Tags / Cost Allocation Tags** |
| **Management Groups & Policies** | **Azure Management Groups + Azure Policy** | Organize multiple subscriptions and enforce cost-related policies globally. | For enterprise-wide cost governance. | Apply cost limits or restrictions across all subscriptions. | **AWS Organizations + Service Control Policies (SCPs)** |
| **Enterprise Agreements / Billing Accounts** | **Enterprise Enrollment / MCA (Microsoft Customer Agreement)** | Centralized billing and negotiated enterprise pricing for large organizations. | When managing cost across multiple subscriptions and departments. | Consolidate billing for multiple teams under one contract. | **AWS Organizations Consolidated Billing / Enterprise Agreement** |
| **Cost Export & API Access** | **Azure Cost Management Exports / APIs** | Export detailed usage and cost data for BI tools or automation. | When integrating Azure cost data with Power BI or third-party systems. | Export daily cost usage data to Power BI for analysis. | **AWS Cost & Usage Report (CUR)** |
| **Free Tier & Credits** | **Azure Free Account / Dev/Test Pricing / Sponsorships** | Limited free usage and credits for testing or learning. | For new users or developers testing Azure services. | Deploy free-tier web apps or databases for POC. | **AWS Free Tier** |
| **Hybrid Benefit / License Savings** | **Azure Hybrid Benefit** | Reuse on-prem Windows Server or SQL licenses to reduce Azure costs. | When migrating licensed workloads from on-prem to Azure. | Apply hybrid benefit to reduce cost of SQL Server VMs. | **AWS BYOL (Bring Your Own License)** |
| **Cost Control for Dev/Test** | **Azure Dev/Test Labs / Dev/Test Pricing** | Manage cost-effective environments for development and testing. | For development teams that need to spin up/down environments frequently. | Create auto-expiring test environments for developers. | **AWS CloudFormation StackSets with Budget Controls / AWS Sandbox Accounts** |
| **Storage Tiering** | **Azure Blob Storage Tiers (Hot, Cool, Archive)** | Automatically move data between tiers based on usage to save cost. | For long-term data retention or infrequently accessed data. | Move logs to Cool tier, backups to Archive tier. | **AWS S3 Storage Classes (Standard, Infrequent Access, Glacier)** |
| **Monitoring & Insights** | **Azure Monitor + Log Analytics** | Analyze resource usage and performance metrics to detect cost spikes. | To monitor resource utilization and optimize for efficiency. | Detect overprovisioned compute or unused storage. | **AWS CloudWatch + CloudWatch Logs** |
| **FinOps & Governance Integration** | **Azure Cost Management APIs + Power BI Integration** | Integrate cost data into dashboards for FinOps visibility. | For finance and IT teams managing multi-department budgets. | Create Power BI dashboards from exported Azure cost data. | **AWS Cost Anomaly Detection + QuickSight Dashboards** |
| **Automation / Optimization Tools** | **Azure Automation / Logic Apps / Functions** | Automate shutdown/startup or resizing of VMs to save cost. | When automating cost control tasks. | Auto-stop VMs at 7 PM and restart at 8 AM daily. | **AWS Lambda + EventBridge + Instance Scheduler** |

## Python

### reverse the words in a given string

```python
input ="hello ramakrishna how are you"

for i in input.split()[::-1]:
    print(i,end=' ')
```

### sum of digits of number

```python
num='123456'
sum = 0
for i in num:
    sum=sum+int(i)
print(sum)
```

### Group Words That Are Anagrams

```python
Input=["eat", "tea", "tan", "ate", "nat", "bat","ant"]

from collections import defaultdict

def anagram(Input):
    groups=defaultdict(list)
    for word in Input:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return groups

print(anagram(Input))
```

### Find Duplicates in a List

```python
Input = [1, 3, 4, 2, 2, 3,3,3]

num_list=[]
duplicate=[]
for i in Input:
    if i not in num_list:
        num_list.append(i)
    else:
        duplicate.append(i)
print(list(set(duplicate)))
```

### Merge Two Sorted Lists

```python
input1= [1, 3, 5] 

input2=[2, 4, 6]

merge =input1+input2

print(sorted(merge))
```

### Find Common Elements Between Two Lists

```python
Input= [1, 2, 3, 4]
Input2=[3, 4, 5, 6]

common_list=[]
for i in Input:
    if i in Input2:
        common_list.append(i)
print(common_list)
```

### Move All Zeros to End of List

```python
Input= [0, 1, 0, 3, 12]

list1=[]
list2=[]
for i in Input:
    if i != 0:
        list1.append(i)
    else:
        list2.append(i)
print(list1+list2)

# or

def merge(Input):
    nonzeros = [x for x in Input if x !=0]
    zeros= [0] * (len(Input) - len(nonzeros))
    print(nonzeros+zeros)

merge(Input)
```

### Find Longest Substring Without Repeating Characters

```python
def longest_unique_substring(s):
    start = 0
    longest = 0
    current = ""
    seen = {}

    for end in range(len(s)):
        char = s[end]          # s[0]
        if char in seen and seen[char] >= start:
            start = seen[char]+1
        
        seen[char] = end
        current_length= end - start +1

        if current_length > longest:
            longest = current_length
            current= s[start:end + 1]
            
    return longest, current
        
s = "abcabcbbabcdefabc"
length, substring = longest_unique_substring(s)
print("Length:", length)
print("Substring:", substring)

```

### Two Sum Problem

```python
nums = [2,7,11,15]
s=len(nums)

def find_num(nums):

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
    return "no sum match"

target=22
print(find_num(nums))
```

### Find Majority Element in a List

```python
Input= [3, 3, 4, 2, 3, 3, 3]

max=0

for i in Input:
    if Input.count(i) > max:
        max = Input.count(i)
        print(i)
```

### Read a log file and count how many times each error message appears.

You have a log file (e.g., app.log) containing lines like this:

```text
INFO User logged in
ERROR Disk full
WARNING Memory low
INFO File saved
ERROR Disk full
ERROR Network timeout
```

You need to read the log file and count how many times each error message appears.

```python
from collections import Counter

def count_error_messages(log_file_path):
    error_messages = []

    with open(log_file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("ERROR"):
                # Extract the message after "ERROR"
                message = line.split("ERROR", 1)[1].strip()
                error_messages.append(message)

    # Count occurrences
    error_counts = Counter(error_messages)

    # Display results
    for message, count in error_counts.items():
        print(f"{message}: {count}")

# Example usage
count_error_messages("app.log")
```

Output:

```bash
Disk full: 2
Network timeout: 1
```
