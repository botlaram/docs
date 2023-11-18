# Kubernetes

- [Kubernetes](#kubernetes)
  - [Overview](#overview)
    - [Defination](#defination)
    - [Why to use K8](#why-to-use-k8)
  - [Architecture](#architecture)
    - [- Architecture Diagram](#--architecture-diagram)
    - [- K8 workflow diagram](#--k8-workflow-diagram)
  - [K8 components](#k8-components)
    - [Deployment](#deployment)
    - [Node](#node)
    - [Pod](#pod)
    - [Service](#service)
    - [Ingress](#ingress)
      - [Architecture of Ingress](#architecture-of-ingress)
      - [Ingress YAML](#ingress-yaml)
      - [Ingress Vs Internal Service](#ingress-vs-internal-service)
      - [Ingress YAML for path](#ingress-yaml-for-path)
    - [Volumes](#volumes)
      - [Backup Volumes](#backup-volumes)
      - [StorageClass](#storageclass)
      - [Architecture of Persistent Volume](#architecture-of-persistent-volume)
    - [Secret](#secret)
    - [ConfigMap](#configmap)
    - [StatefulSet](#statefulset)
  - [Minikube abd Kubectl-Setup](#minikube-abd-kubectl-setup)
  - [Helm](#helm)
  - [Volumes-Persisting Data](#volumes-persisting-data)
  - [K8 stateful set](#k8-stateful-set)


## Overview

### Defination

Kubernetes is a portable, extensible, open source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

- For more information visit **[here](https://kubernetes.io/docs/concepts/overview/components/)**
### Why to use K8

Containers are a good way to bundle and run your applications. In a production environment, you need to manage the containers that run the applications and ensure that there is no downtime. For example, if a container goes down, another container needs to start. Wouldn't it be easier if this behavior was handled by a system?

That's how Kubernetes comes to the rescue! Kubernetes provides you with a framework to run distributed systems resiliently. It takes care of scaling and failover for your application, provides deployment patterns, and more. For example: Kubernetes can easily manage a canary deployment for your system.

- Kubernetes provides you with:

> - **Service discovery and load balancing** Kubernetes can expose a container using the DNS name or using their own IP address. If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic so that the deployment is stable.

> - **Storage orchestration** Kubernetes allows you to automatically mount a storage system of your choice, such as local storages, public cloud providers, and more.

> - **Automated rollouts and rollbacks** You can describe the desired state for your deployed containers using Kubernetes, and it can change the actual state to the desired state at a controlled rate. For example, you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all their resources to the new container.
Automatic bin packing You provide Kubernetes with a cluster of nodes that it can use to run containerized tasks. You tell Kubernetes how much CPU and memory (RAM) each container needs. Kubernetes can fit containers onto your nodes to make the best use of your resources.

> - **Self-healing** Kubernetes restarts containers that fail, replaces containers, kills containers that don't respond to your user-defined health check, and doesn't advertise them to clients until they are ready to serve.

> - **Secret and configuration management** Kubernetes lets you store and manage sensitive information, such as passwords, OAuth tokens, and SSH keys. You can deploy and update secrets and application configuration without rebuilding your container images, and without exposing secrets in your stack configuration.

## Architecture

### - Architecture Diagram

![Architecture](./png/k8_architecture.jpg)

### - K8 workflow diagram

![K8 Work flow Architecture](./png/k8_timezone_architect.PNG)

## K8 components

### Deployment

### Node

- [nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)

### Pod

- [pods](https://kubernetes.io/docs/concepts/workloads/pods/)

### Service

- [service](https://kubernetes.io/docs/concepts/services-networking/service/)

### Ingress

- [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)

#### Architecture of Ingress
![image](./png/ingress1.png)

#### Ingress YAML
![image](./png/ingress2.png)

#### Ingress Vs Internal Service
![image](./png/ingress3.png)

#### Ingress YAML for path
![image](./png/ingress4.png)

### Volumes

#### Backup Volumes

- [Volumes](https://kubernetes.io/docs/concepts/storage/volumes/)

- We also use **Git Repo** as Persistent Volume - [link](https://kubernetes.io/docs/concepts/storage/volumes/#gitrepo)


#### StorageClass

- follow the docs for further info of [StorageClass](https://kubernetes.io/docs/concepts/storage/storage-classes/)

- template for storageclass

```apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: azurefile-sc
provisioner: kubernetes.io/azure-file
reclaimPolicy: Retain
mountOptions:
  - dir_mode=0777
  - file_mode=0777
volumeBindingMode: WaitForFirstConsumer
```

- Field/Parameters details:
  
    - **volumeBindingMode**: 
      This field specifies when volume binding should occur. In this case, Immediate means that a volume should be provisioned and bound as soon as a PersistentVolumeClaim (PVC) is created. This is in contrast to WaitForFirstConsumer, where the binding is delayed until a pod using the PVC is scheduled onto a node.

    - **reclaimPolicy** : in Persistent Volumes specifies what should happen to the underlying storage when the associated PersistentVolume (PV) is released or the PersistentVolumeClaim (PVC) is deleted:

      **Retain**: When the reclaimPolicy is set to Retain, the PV is not automatically deleted when the associated PVC is deleted.
      The PV is marked as released, and it's up to the cluster administrator to decide what to do with the data on the storage.
      
      **Delete**: When the reclaimPolicy is set to Delete, the PV is automatically deleted when the associated PVC is deleted.
      The storage resources associated with the PV are also deleted.


#### Architecture of Persistent Volume

![pvc](./png/pvc-architecture.png)


### Secret

### ConfigMap

### StatefulSet

## Minikube abd Kubectl-Setup


## Helm

## Volumes-Persisting Data

## K8 stateful set