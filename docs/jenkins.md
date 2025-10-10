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

## How do you ensure faster builds?

Use parallel stages.

Cache dependencies.

Use distributed builds.

Clean up old builds.

Use lightweight agents like Docker containers.
