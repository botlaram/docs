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
