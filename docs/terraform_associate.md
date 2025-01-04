# Terraform Associate

## Provider

[Terraform providers](https://registry.terraform.io/browse/providers) are plugins or modules in Terraform that let it interact with external systems or services.

How They Work:

Connect to Systems: Providers are like translators that help Terraform communicate with cloud platforms (like AWS, Azure, or Google Cloud), on-premises tools, or third-party services.  

Define Resources: They define the types of resources you can manage, like virtual machines, databases, or storage buckets.  

Manage Resources: Providers handle creating, reading, updating, and deleting those resources in the system.  

Examples of Providers:

- Cloud Providers: AWS, Azure, Google Cloud  
- Service Providers: Kubernetes, GitHub, Datadog
- Infrastructure Providers: VMware, OpenStack

Key Points:

Each provider needs configuration, usually credentials or access keys, to connect to the system.  
Terraform uses providers to translate your .tf files (infrastructure code) into API calls to the respective services.

Eg: To install a provider

```terraform
terraform {
    required_providers {
        azurerm = {
            source = "hashicorp/azurerm"
            version = "4.14.0"
        }
    }
}
```

command : `terraform init`

## Lock file

Dependency Lock File

Purpose: Ensures consistent versions of Terraform providers are used across environments.

How It Works:

When you run terraform init, Terraform creates or updates the terraform.lock.hcl file.  
This file contains the exact versions of the providers Terraform is configured to use.

Benefits:

Prevents breaking changes by ensuring the same provider versions are used, even if newer versions are released.  
Ensures reproducibility across teams and environments.

Managing the Lock File:

To update provider versions, run:

```terraform
terraform init -upgrade
```

## State file

The state file contains details about the resources created by Terraform, including their current configuration and metadata like resource IDs and attributes.

When you run terraform plan - Terraform compares the desired configuration (defined in your .tf files) with the actual state of the infrastructure (in the state file). Any differences are shown in the plan output

State Management Commands

```bash
terraform state list: Lists all resources in the state file.
terraform state show <resource_address>: Displays detailed information about a specific resource.
terraform state pull: Downloads the remote state file locally.
terraform state push: Uploads a local state file to the remote backend.
```

## Terraform Import

Terraform import is command that allows you to incorporate existing infrastructure resources into your
Terraform configuration and state management.

Steps:

1. create main.tf containing resource name, subscription id

2. Execute import command with resource name and subscription id

    ```terraform
    terraform init
    terraform import azurerm_key_vault_secret.example /subscriptions/5896dffd-29db-dd8g-b786-dgdg8dgdg8/resourceGroups/pss-common/providers/Microsoft.KeyVault/vaults/terraform-kv-001/secrets/terraform-secret-name
    ```

3. Display imported resources

    ```bash
    terraform state list #to display configured resource
    terraform state show azurerm_key_vault_secret.example # to display resource values
    ```

4. To verify resources using terraform plan, updated main.tf with details display in terminal

    ```bash
    terraform plan
    ```

To show state file in json format

```bash
terraform show -json > terraform_state.json
```

## Verbose

Levels of TF_LOG

TF_LOG=TRACE: This is the most verbose logging level. It logs every detail about the process, including internal operations and data being sent between the Terraform CLI and providers.

TF_LOG=DEBUG: This level provides detailed information but omits some internal operations that aren’t normally needed for most users. It's useful for debugging the configuration and interactions with providers.

TF_LOG=INFO: This is the default level and provides general information about what Terraform is doing, like showing the resources being created, updated, or destroyed.

TF_LOG=WARN: Shows warnings, such as deprecated functionality, but doesn't provide much information otherwise.

TF_LOG=ERROR: Only shows error messages when something goes wrong.

```bash
# set terraform log
export TF_LOG="TRACE"
export TF_LOG_PATH="filepath.log"

# unset var
unset TF_LOG
unset TF_LOG_PATH
```

## Terraform Console

The terraform console command provides an interactive shell to evaluate Terraform expressions and interact with the Terraform configuration and state. It is a powerful tool for debugging, testing expressions, and exploring Terraform resources and data.

Key Features of terraform console: You can test Terraform expressions, such as arithmetic, string manipulation, or functions, to understand their output.

Inspect Variables and Outputs:Access variables or outputs defined in the configuration.

```bash
> var.my_variable
"some value"
> output.my_output
"output value"
```

## Modules

In Terraform, a module is a container for multiple resources that are used together. It allows you to group resources into reusable, self-contained units of configuration. Modules help organize Terraform code, improve reusability, and reduce duplication. They can be simple, like a single resource, or more complex, containing a set of resources for creating an entire infrastructure component.

Modules in Terraform allow for logical separation of infrastructure code and enable reusability. They are fundamental to writing clean, maintainable, and modular infrastructure code.

Types of Terraform Modules

**Root Module**: This is the starting point for Terraform execution and contains all the Terraform configuration files in the current working directory. It is the main module where you run terraform init, terraform plan, and terraform apply.

**Child Modules**: Modules that are used within the root module or other modules. You can create and call these modules to encapsulate parts of your configuration logic.

**External Modules**: Terraform modules that are stored outside of your project, typically shared in a module registry, like the Terraform Module Registry. You can use external modules to avoid "reinventing the wheel" and make use of pre-existing infrastructure code written by others.

```bash
/project
  ├── main.tf           (root module)
  ├── modules/
  │    └── s3_bucket/
  │        ├── main.tf  (child module to create an S3 bucket)
  │        └── variables.tf
  ├── outputs.tf
  └── variables.tf
```

## lock terraform state file

Locking the Terraform state file is a mechanism to prevent simultaneous operations (like multiple terraform apply or terraform plan commands) from corrupting the state file. When multiple users or processes try to modify the state file concurrently, there’s a risk of conflicts or overwrites. State file locking ensures that only one process can modify the state file at a time.

How State Locking Works in Terraform
Terraform uses a locking mechanism provided by the backend where the state file is stored.

1. Acquires a lock before modifying the state file.
2. Prevents other operations until the lock is released.
3. Releases the lock after the operation completes.

**Locking in Azure Cloud** : In Azure, the Azure Blob Storage backend supports state file locking by using Azure Storage blob leases. A lease is a mechanism provided by Azure Blob Storage to ensure exclusive access to a blob for a certain period.

Setting Up Terraform State Locking with Azure Blob Storage

Prerequisites:

1. An Azure Storage account.
2. A container in Azure Blob Storage to store the state file.
3. Configure the Backend: Add the following configuration in your Terraform code to use Azure Blob Storage as the backend:

```bash
terraform {
  backend "azurerm" {
    resource_group_name  = "myResourceGroup" # The Azure resource group containing the storage account.
    storage_account_name = "mystorageaccount" # The name of the storage account.
    container_name       = "terraformstate" # The container name in Blob Storage to store the state file.
    key                  = "terraform.tfstate" # The file name for the Terraform state file.
  }
}

```

Enable State Locking: By default, when you use Azure Blob Storage as a backend, Terraform automatically uses blob leases to lock the state file during operations. No additional configuration is needed.

Managing Locks: If Terraform detects a lock during an operation, it will:

Wait until the lock is released.

If needed, you can manually break the lock using Azure CLI:

```terraform
az storage blob lease break \
  --blob-name terraform.tfstate \
  --container-name terraformstate \
  --account-name mystorageaccount
```

## Resource drift

Resource drift in Terraform refers to the situation where the actual state of resources in your infrastructure differs from the expected state defined in your Terraform configuration files. Drift can occur when changes are made to infrastructure outside of Terraform's control, such as manual modifications in the cloud provider's console or API.

Causes of Resource Drift

1. Manual Changes: Alterations made directly in the cloud provider's management console or via other tools.
2. Automated Processes: Updates performed by scripts or other automated workflows outside of Terraform.
3. External Dependencies: Changes in resources that Terraform depends on but does not manage, such as auto-scaling events or updates in external systems.
4. Configuration Changes: Updates in Terraform configuration files that do not match the current state of the resources.

If manual changes have been made to your infrastructure and you want to bring those changes into Terraform so that it recognizes them without overwriting them, you can achieve this through a process called Terraform import. Here's how you can do it:

Steps to Add Manual Changes to Terraform

1. Identify the Resources to Import  

    Determine which resources have been manually changed and need to be imported into Terraform.
    Collect the identifiers (e.g., resource ID, ARN, or name) for these resources.

2. Update Your Terraform Configuration  

    Add the resource block to your Terraform configuration for the resource you want to import.
    Ensure that the resource block matches the current state of the resource as closely as possible (e.g., resource type, attributes).

    Example:

    ```terraform
    resource "azurerm_virtual_machine" "example" {
    name                  = "my-vm"
    resource_group_name   = "myResourceGroup"
    location              = "East US"
    vm_size               = "Standard_DS1_v2"
    network_interface_ids = [azurerm_network_interface.example.id]
    }
    ```

3. Run the Terraform Import Command

    Use the terraform import command to associate the manually created resource with the resource block in your configuration.

    Example: Replace placeholders ({subscriptionId}, {resourceGroupName}, {vmName}) with the actual values for your resource.

    ```terraform
    terraform import azurerm_virtual_machine.example /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}
    ```

4. Refresh the State

    After importing, run the terraform plan command to verify that the resource's current state matches the Terraform configuration.

    ```terraform
    terraform plan
    ```

    If there are discrepancies, Terraform will show a plan to align the state with the configuration.

## terraform taint

Terraform taint command marks a specific resource in the Terraform state as "tainted," meaning it needs to be destroyed and recreated during the next terraform apply.

Use Case: A resource is in a bad state (e.g., misconfigured, corrupted, or broken).
You want to force a resource to be recreated without modifying its configuration.

1. Mark the Resource as Tainted:

    ```terraform
    terraform taint <resource_address>

    #example
    terraform taint aws_instance.my_instance #<resource_address> refers to the resource's address in the Terraform configuration.
    ```

2. Apply the Changes: Run terraform apply to destroy the tainted resource and recreate it.

    ```terraform
    terraform apply
    ```

## terraform apply -replace

`terraform apply -replace=<address>` command is a more modern approach (introduced in Terraform 0.15) to achieve what terraform taint does but in a single step.  
It directly forces the replacement of a specific resource during the terraform apply operation.

Use Case: You want to recreate a specific resource immediately without manually tainting it first.

Run the Apply Command with Replace:

```terraform
terraform apply -replace=<resource_address>

#Example
terraform apply -replace=aws_instance.my_instance
```

## Meta Arguments

### Provider meta-argument

The provider meta-argument is used to specify which provider configuration to use for a resource or data source. It allows you to override the default provider configuration within a specific resource.

Usage: You can use the provider meta-argument to define the provider configuration for a resource or data source, especially in cases where you might have multiple provider configurations.  
This is particularly useful when managing resources across multiple accounts or regions.

```terraform
provider "aws" {
  region = "us-west-2"
}

provider "aws" {
  alias  = "east"
  region = "us-east-1"
}

resource "aws_instance" "west_instance" {
  provider = aws
  ami           = "ami-12345678"
  instance_type = "t2.micro"
}

resource "aws_instance" "east_instance" {
  provider = aws.east
  ami           = "ami-23456789"
  instance_type = "t2.micro"
}
```

In this example:

- The first aws_instance uses the us-west-2 region.
- The second aws_instance uses the us-east-1 region with an alias east

### Provisioner

**local-exec provisioner** : The local-exec provisioner runs a command or script on the machine where Terraform is executed (i.e., the local workstation or CI/CD server running Terraform).

Use Cases:

1. Triggering external processes, like CI/CD pipelines or API calls.  
2. Executing local scripts for configuration, validation, or logging.  
3. Sending notifications or updates to external systems.  

Configuration file local-exec

```terraform
# example1

resource "aws_instance" "example" {
# Resource definition
ami           = "ami-12345678"
instance_type = "t2.micro"

provisioner "local-exec" {
    command = "echo 'Instance created!'"
}
}


# example2
resource "aws_instance" "example" {
ami           = "ami-12345678"
instance_type = "t2.micro"

provisioner "local-exec" {
    command = "aws ec2 describe-instances > instances.json"
}
}
```

The local-exec provisioner runs an AWS CLI command locally to save instance details to a JSON file.

**remote-exec provisioner** : The remote-exec provisioner runs commands or scripts on a remote resource (e.g., a VM or instance) after it is created. This requires SSH or WinRM access to the resource.

Use Cases:

1. Installing or configuring software on a server.
2. Running startup scripts or applying configuration management tools (e.g., Ansible, Puppet).
3. Performing post-deployment tasks, such as downloading application code.

Configuration file remote-exec

```terraform
resource "aws_instance" "example" {
  # Resource definition
  ami           = "ami-12345678"
  instance_type = "t2.micro"

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install nginx -y"
    ]
  }
}
```

### lifecycle

The lifecycle meta-argument defines how Terraform should handle the lifecycle of resources during create, update, and destroy operations. It provides additional control over the resource management process, including handling resource replacement, deletion, and preventing accidental modifications.

Common Lifecycle Arguments:

- create_before_destroy: Ensures that a new resource is created before an old one is destroyed.
- prevent_destroy: Prevents the resource from being destroyed, even if it is removed from the configuration.
- ignore_changes: Tells Terraform to ignore changes to specific resource attributes during updates.

```terraform
resource "aws_instance" "example" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"

  lifecycle {
    create_before_destroy = true
    prevent_destroy       = true
    ignore_changes        = [
      ami,
    ]
  }
}
```

In this example:

- create_before_destroy = true: Ensures the new instance is created before the old one is destroyed (useful for avoiding downtime).
- prevent_destroy = true: Prevents the instance from being destroyed accidentally, even if it is removed from the configuration.
- ignore_changes: Instructs Terraform to ignore changes to the ami attribute, so if the AMI changes, it won't trigger a replacement of the instance

### depends_on

depends_on meta-argument explicitly defines dependencies between resources.

```terraform
resource "aws_instance" "example" {
ami           = "ami-12345678"
instance_type = "t2.micro"
}

resource "aws_security_group" "example" {
name        = "example-sg"
description = "Example security group"

depends_on = [aws_instance.example]
}
```

### count

The count meta-argument allows the creation of multiple instances of a resource.

```terraform
resource "aws_instance" "example" {
count         = 3
ami           = "ami-12345678"
instance_type = "t2.micro"
}
```

### for_each

The for_each meta-argument allows iteration over a set of values (like a map or list) to create multiple resources.

```terraform
resource "aws_instance" "example" {
for_each      = var.instance_configs
ami           = each.value["ami"]
instance_type = each.value["instance_type"]
}
```

### create_before_destroy

The create_before_destroy argument in the lifecycle block ensures that the new resource is created before the old one is destroyed. This is useful when a resource's replacement might disrupt service or functionality.

```terraform
resource "aws_instance" "example" {
ami           = "ami-12345678"
instance_type = "t2.micro"

lifecycle {
    create_before_destroy = true
}
}
```

### prevent_destroy

Prevents the destruction of the resource even if the configuration changes. Useful for protecting critical resources (e.g., databases, production servers).  
This prevents the resource from being destroyed, even if you run terraform destroy.

```terraform
resource "aws_instance" "example" {
ami           = "ami-12345678"
instance_type = "t2.micro"

lifecycle {
    prevent_destroy = true
}
}
```

## Output files

Output.tf is a file (or a section in any Terraform configuration file) where you define outputs.  
Outputs allow you to extract and display information about your infrastructure after Terraform has applied changes. These outputs can also be used as inputs to other modules or external systems.

Integration: Share data between Terraform modules. Pass infrastructure details to external tools, scripts, or CI/CD pipelines.

Basic Syntax:

```terraform
output "<name>" {
  value = <expression>
}
```

Example: Using output.tf

```terraform
output "instance_public_ip" {
  value       = aws_instance.example.public_ip
  description = "The public IP address of the EC2 instance"
}
```

## Secure secret available

Terraform often requires sensitive information such as API keys, passwords, and other secrets to provision infrastructure. Properly securing these secrets is crucial to prevent accidental exposure or breaches.

1. Use Environment Variables

    Terraform allows you to pass variables as environment variables, keeping them out of your configuration files.

    Define the variable in variables.tf:

    ```terraform
    variable "db_password" {
    type        = string
    description = "The database password"
    }
    ```

    Set the environment variable:

    ```terraform
    export TF_VAR_db_password="your_secret_password"
    Reference the variable in your configuration:
    ```

    ```terraform
    resource "aws_db_instance" "example" {
    password = var.db_password
    }
    ```

2. Use Terraform's Sensitive Attribute

    ``Terraform’s sensitive attribute can be used to mask sensitive data in the Terraform plan and output.

    Example:

    ```terraform
    variable "db_password" {
    type      = string
    sensitive = true
    }

    output "db_password" {
    value     = var.db_password
    sensitive = true
    }
    ```

    This prevents the sensitive variable from being displayed in the Terraform CLI output.``

3. Use .tfvars Files with Care

    You can define variables, including secrets, in a .tfvars file.

    Example: secrets.tfvars:

    ```terraform
    db_password = "super_secret_password"
    ```

    Run Terraform with the .tfvars file:

    ```terraform
    terraform apply -var-file="secrets.tfvars"
    ```

## Understand the use of collections and structural types

In Terraform, collections and structural types are mechanisms to handle complex and flexible data structures. They are used to represent and manage data such as lists, maps, and objects, which help organize configuration in a scalable and reusable way.

### Collections in Terraform

Collections are data types that group multiple values together. Terraform provides two main types of collections: lists and maps.

1. Lists

    Definition: A list is an ordered collection of values, indexed by sequential integers starting at 0.

    Example: list(string) (a list of strings)

    When to Use: Use lists when order matters, or when iterating through items sequentially.

    Example:

    ```terraform
    variable "instance_types" {
    type    = list(string)
    default = ["t2.micro", "t2.small", "t2.medium"]
    }

    resource "aws_instance" "example" {
    count         = length(var.instance_types)
    instance_type = var.instance_types[count.index]
    }
    ```

    This creates multiple instances using instance types from the list.

2. Maps

    Definition: A map is a collection of key-value pairs, where each value is identified by a unique key.

    Example: map(string) (a map with string keys and string values)

    When to Use: Use maps when you need to look up values by keys or store key-value pairs for better readability.

    ```terraform
    variable "region_amis" {
    type = map(string)
    default = {
        us-east-1 = "ami-12345678"
        us-west-2 = "ami-87654321"
    }
    }

    resource "aws_instance" "example" {
    ami           = var.region_amis[var.region]
    instance_type = "t2.micro"
    }
    ```

    This selects the correct AMI based on the region.

3. Combining Lists and Maps: Terraform supports nested collections, like a list of maps or a map of lists.

    ```terraform
    variable "servers" {
    type = list(map(string))
    default = [
        { name = "web1", type = "t2.micro" },
        { name = "web2", type = "t2.small" },
    ]
    }

    resource "aws_instance" "example" {
    count         = length(var.servers)
    instance_type = var.servers[count.index]["type"]
    tags = {
        Name = var.servers[count.index]["name"]
    }
    }
    ```

    This creates instances with types and names derived from the list of maps.

### Structural Types in Terraform

Structural types describe complex data structures using objects, tuples, or nested types. They allow for fine-grained control over the shape and constraints of the data.

1. Objects

    Definition: Objects are collections of attributes with specified names and types. Each attribute is like a named field in a JSON object.

    When to Use: Use objects for structured data with named fields and predictable types.

    ```terraform
    variable "server_config" {
    type = object({
        name         = string
        instance_type = string
        tags          = map(string)
    })
    default = {
        name         = "web-server"
        instance_type = "t2.micro"
        tags          = { Environment = "production" }
    }
    }

    resource "aws_instance" "example" {
    ami           = "ami-12345678"
    instance_type = var.server_config.instance_type
    tags          = var.server_config.tags
    }
    ```

2. Tuples

    Definition: Tuples are ordered collections of values with a fixed number of elements, where each element can have a different type.

    When to Use: Use tuples when you have a fixed structure but need to mix data types.

    ```terraform
    variable "database_info" {
    type = tuple([string, number, bool])
    default = ["db-primary", 3306, true]
    }

    output "database_name" {
    value = var.database_info[0]
    }

    output "database_port" {
    value = var.database_info[1]
    }

    output "is_database_active" {
    value = var.database_info[2]
    }
    ```

    Here, the tuple holds a database name (string), port (number), and active status (boolean)

## [built-in functions](https://developer.hashicorp.com/terraform/language/functions)

Terraform provides a variety of built-in functions that you can use to manipulate and operate on data within your configuration files. These functions allow you to work with strings, numbers, collections, dates, and more, enabling more dynamic and flexible Terraform code.
