🧰 Jenkins

# Overview

Jenkins is an open-source automation server used to build, test, and deploy applications continuously.
It supports Continuous Integration (CI) and Continuous Deployment (CD) by automating software development workflows.

## Jenkins Architecture

Jenkins Master/Controller – Orchestrates builds, schedules jobs, manages configurations.

Jenkins Agent/Slave – Executes builds on remote machines.

Communication happens via JNLP (Java Network Launch Protocol) or SSH.

This architecture helps in scaling build workloads across multiple nodes.

## What are the key features of Jenkins?

Open-source and extensible via plugins

Supports distributed builds using master-agent architecture

Compatible with all major version control systems (Git, SVN, etc.)

Provides Declarative and Scripted Pipelines

Supports integration with tools like Docker, Kubernetes, Maven, Ansible, etc.

## What is a Jenkins job?

A Jenkins job is a task or unit of work executed by Jenkins.

Examples include:

Freestyle Project

Pipeline Project

Multibranch Pipeline

Maven Project

## What is a Jenkinsfile?

A Jenkinsfile is a text file that contains the pipeline definition written in either Declarative or Scripted syntax.
It is usually stored in the root of your source code repository.

## How to start Jenkins manually

```bash
jenkins start
jenkins stop
jenkins restart
```

## Pipeline

There are two main types of pipelines:

Type	               | Description
Declarative  Pipeline | Simplified, structured syntax. Recommended for most use cases.
Scripted Pipeline | 	Groovy-based, more flexible and programmable syntax. Ideal for complex workflows.

### Declarative Pipeline
📘 Overview

Declarative Pipeline syntax provides a simple, structured way to define your build process.
It starts with a top-level pipeline block and enforces a specific hierarchy of elements (agent, stages, steps, etc.).

Easier to read and maintain.

Better validation and error handling.

```yaml
pipeline {
    agent any

    environment {
        // Define global environment variables
        BUILD_ENV = 'staging'
    }

    options {
        // Keep only last 5 builds
        buildDiscarder(logRotator(numToKeepStr: '5'))
        // Set build timeout to 30 minutes
        timeout(time: 30, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code..."
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building the project..."
                sh 'make build'
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'make test'
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying to ${BUILD_ENV} environment..."
                sh 'make deploy'
            }
        }
    }

    post {
        success {
            echo 'Build and deploy succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

```

### Scripted Pipeline
📘 Overview

Scripted Pipeline uses Groovy code to define the pipeline.
It offers full programmatic control (conditions, loops, functions, etc.).

More powerful and flexible.

Requires Groovy knowledge.

Older style, still widely used.

```yaml
node {
    stage('Checkout') {
        echo "Checking out source code..."
        checkout scm
    }

    stage('Build') {
        echo "Building the project..."
        sh 'make build'
    }

    stage('Test') {
        echo "Running tests..."
        sh 'make test'
    }

    stage('Deploy') {
        if (env.BRANCH_NAME == 'main') {
            echo "Deploying to production..."
            sh 'make deploy'
        } else {
            echo "Skipping deployment for non-main branch."
        }
    }

    // Post actions
    try {
        echo "Build completed successfully."
    } catch (err) {
        echo "Build failed: ${err}"
        currentBuild.result = 'FAILURE'
    }
}

```

## How do you trigger a Jenkins pipeline automatically?

SCM polling (e.g., pollSCM('* * * * *'))

Webhooks from GitHub/GitLab/Bitbucket

Build triggers (e.g., Build after other projects are built)

Manual trigger

API call

## What are Jenkins plugins?

Plugins extend Jenkins functionality (e.g., for Docker, Kubernetes, Slack, SonarQube).
They are managed under Manage Jenkins → Manage Plugins.

## What is Blue Ocean in Jenkins?

Blue Ocean is a modern Jenkins UI that provides:

Visual representation of pipelines

Simplified creation and debugging

Enhanced user experience

## Troubleshooting

How do you handle Jenkins build failures?

Check console logs.

Validate pipeline syntax using the Jenkinsfile validator.

Re-run with increased log level.

Ensure correct environment setup and plugin versions.

## You have multiple branches with different build steps — how do you handle this?

Use a Multibranch Pipeline or when conditions in Jenkinsfile:

```yaml
stage('Build') {
    when {
        branch 'main'
    }
    steps {
        sh 'make build-prod'
    }
}
```

## What are agents in jenkins

Agent in jenkins (also known as slave) is a machine that connects to Jenkins Master and execute tasks when directed by master.

## What happens when Jenkins agent are offline and What is best practice in this situation?

If target node is offline or all agents on that particular nodes are occupied building other jobs, then the triggered job has to wait until the node comes online  or agent from another node becomes available to trigger build request.

## How to stores credentials in Jenkins securely?

Credential plugin

Secret text plugin

HashiCorp Vault (Jenkins allow to integrate with HashiCorp Vault)

## How to debug if there is problem with job or pipeline fails

Using web interface: we can access logs files by going to Manage Jenkins > System Logs

Using the file system: You can access log files by going to Jenkins_Home directory on your Jenkins Server.

## How do you integrate Static Code Analysis tools into Jenkins pipeline

Install Sonarqube plugin from Jenkins Management later in pipeline add steps to execute static code analysis.

## Explain how to move or copy Jenkins one server to another?

Migrating Jenkins from one server to another involves transferring all configurations, jobs, plugins, and build histories safely while ensuring minimal downtime.

There are two main approaches:

Manual Migration (copy Jenkins home)

Backup & Restore using plugins or tools

1. Manual Migration (Most Common Approach)

Step-by-Step Process:

Step 1: Identify Jenkins Home Directory

Check the Jenkins home directory on the old server.

```bash
On Linux:

echo $JENKINS_HOME


Usually located at:

/var/lib/jenkins


On Windows:

C:\Program Files (x86)\Jenkins
```

Step 2: Stop Jenkins Service

Before copying, stop Jenkins to avoid file corruption.

```bash
On Linux:

sudo systemctl stop jenkins


On Windows (PowerShell):

net stop jenkins
```

Step 3: Copy Jenkins Home Directory

Copy the entire $JENKINS_HOME directory to the new server.

```bash
Linux Example:

rsync -avz /var/lib/jenkins/ user@newserver:/var/lib/jenkins/


Windows Example:
Use an SCP tool (like WinSCP) or robocopy:

robocopy "C:\Program Files (x86)\Jenkins" "\\newserver\Jenkins" /E
```

Step 4: Install Jenkins on New Server

Install the same Jenkins version (to avoid plugin mismatches).

Do not start Jenkins yet.

Step 5: Replace Jenkins Home

Replace the new server’s $JENKINS_HOME directory with the copied one from the old server.

Step 6: Start Jenkins

```bash
On Linux:

sudo systemctl start jenkins


On Windows:

net start jenkins
```

Then, access Jenkins UI to verify that: Jobs, credentials, and plugins are intact. Build history and configurations are preserved.

Step 7: Update System Configurations

After starting Jenkins on the new server, update:

Node/agent configurations (IP or hostname).

Webhooks and service URLs (GitHub, Bitbucket, etc.).

Credentials if using machine-specific secrets.

### If Jenkins Runs in Docker or Kubernetes

If Jenkins is containerized:

Backup the Jenkins Home volume.

Copy that volume to the new environment.

Use the same image version.

```bash
docker run -d \
  -v /path/to/jenkins_home:/var/jenkins_home \
  -p 8080:8080 jenkins/jenkins:lts
```

## How to implement rolling update deployment strategy using Jenkins

A rolling update in Jenkins can be implemented by integrating Jenkins with Kubernetes or a deployment tool like Ansible.

In Kubernetes, we define the rolling strategy in the deployment YAML (maxUnavailable and maxSurge), and in the Jenkins pipeline, we use kubectl set image followed by kubectl rollout status to apply and monitor the deployment.  

This ensures zero downtime — old pods are terminated only after new pods are healthy

If a failure occurs, Jenkins can automatically trigger a kubectl rollout undo rollback.”


## How do you ensure faster builds?

Use parallel stages.

Cache dependencies.

Use distributed builds.

Clean up old builds.

Use lightweight agents like Docker containers.
