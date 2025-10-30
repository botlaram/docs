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
