# CKA

## Understand K8 architecture

### Vanilla Kubernetes

"Vanilla Kubernetes" refers to the standard, unmodified, open-source version of Kubernetes as released by the Kubernetes community, without any vendor-specific customizations, extensions, or added features. It is the pure form of Kubernetes as maintained by the Cloud Native Computing Foundation (CNCF).

Using Vanilla Kubernetes ensures you’re working with the core features and APIs defined by the Kubernetes project, providing a consistent foundation for container orchestration.

### Core Components of Vanilla Kubernetes

Vanilla Kubernetes consists of several components categorized as either control plane components or node components:

**Control Plane Components** : These components are responsible for managing the cluster and ensuring the desired state of the system.

1. API Server (kube-apiserver): Acts as the central management point for Kubernetes. It exposes the Kubernetes API, processes client requests, and communicates with other components.

    Key feature: Handles REST API calls.

2. Controller Manager (kube-controller-manager): Runs controllers that regulate the state of the cluster, such as the Node Controller (monitoring nodes), ReplicaSet Controller (managing replicas), and others.

    Key feature: Ensures the cluster meets the desired state.

3. Scheduler (kube-scheduler):Assigns workloads (Pods) to nodes in the cluster based on resource availability and policies.

    Key feature: Ensures optimal placement of Pods.

4. Etcd: A distributed key-value store that serves as Kubernetes' database, storing all cluster data such as configurations, secrets, and the desired state.

    Key feature: Provides high availability and consistency.

**Node Components** : Node components manage the execution of workloads on individual machines.

1. Kubelet: A daemon running on each node, ensuring that containers are running as defined by the Pod specifications.

    Key feature: Manages container lifecycle on a node.

2. Kube-Proxy: A network proxy that manages network rules and enables service discovery and communication between Pods.

    Key feature: Provides networking for Pods and services.

3. Container Runtime: Executes containers and manages container lifecycle. Examples include Docker, containerd, and CRI-O.

    Key feature: Ensures Pods' containers run smoothly.

**Add-Ons (Optional Components)** : These are additional features often deployed in a Kubernetes cluster.

1. DNS (CoreDNS): Provides service discovery and DNS resolution for services within the cluster.
2. Ingress Controllers: Manages external HTTP and HTTPS access to cluster services.
3. Metrics Server: Collects resource metrics for autoscaling and monitoring.

### Ecosystem of Vanilla Kubernetes

Kubernetes has a rich ecosystem of tools and technologies that enhance its functionality and usability. These tools are often open-source and community-driven, but they may also include vendor-specific solutions:

1. Networking

    CNI (Container Network Interface): Plugins like Calico, Flannel, and Weave Net enable networking in Kubernetes.

    Service Mesh: Istio and Linkerd provide advanced networking features like traffic routing and observability.

2. Storage

    CSI (Container Storage Interface): Allows Kubernetes to interact with storage systems. Examples: Rook, Ceph, and AWS EBS.

3. Observability

    Monitoring: Prometheus, Grafana, and Datadog help monitor cluster health and workloads.

    Logging: Tools like Elasticsearch, Fluentd, and Kibana (EFK stack) collect and analyze logs.

4. Deployment and Scaling

    Helm: A package manager for Kubernetes that simplifies application deployment.

    Kustomize: Provides declarative configuration management for Kubernetes resources.

5. Security

    RBAC (Role-Based Access Control): Manages permissions within the cluster.

    Tools: Falco, Aqua Security, and OPA (Open Policy Agent) for runtime security and policy enforcement.

6. CI/CD Integration

    ArgoCD: A declarative GitOps continuous delivery tool for Kubernetes.

    Jenkins X: Kubernetes-native CI/CD solution.

7. Backup and Disaster Recovery

    Tools like Velero for backing up and restoring Kubernetes resources.

**Advantages of Using Vanilla Kubernetes**

- Portability: No vendor lock-in; deployable across any environment supporting Kubernetes.
- Flexibility: Offers complete control over how you configure and extend Kubernetes.
- Community Support: Benefits from a vibrant open-source community and frequent updates.

**Challenges with Vanilla Kubernetes**

- Complexity: Requires expertise to set up, maintain, and secure.
- Lack of Pre-Configured Features: Unlike managed Kubernetes services (e.g., GKE, AKS, EKS)
- Vanilla Kubernetes doesn’t include out-of-the-box solutions for scaling, logging, or monitoring.

## Understand cluster node requirements install using kubeadm

Cluster Node Requirements for Installing Kubernetes Using kubeadm.

Before installing a Kubernetes cluster using kubeadm, it’s essential to ensure that the system requirements and prerequisites are met for the control plane and worker nodes. Below is a comprehensive guide to help you prepare.

1. Hardware Requirements

    Control Plane Node (Master Node)

    - CPU: 2 cores or more.
    - RAM: 2 GB or more (4 GB recommended for production).
    - Disk Space: 10 GB or more free space.
    - Network: Stable network connection (public or private).

    Worker Nodes

    - CPU: 1 core or more.
    - RAM: 1 GB or more (2 GB recommended for production).
    - Disk Space: 10 GB or more free space.
    - Network: Network connectivity to control plane and other nodes.

2. Operating System Requirements

    Use one of the following operating systems:

    - Ubuntu 20.04, 22.04
    - CentOS 7 or 8
    - Red Hat Enterprise Linux (RHEL) 7 or 8
    - Debian 10 or 11
    - Ensure the OS is up-to-date with the latest patches and security updates.

3. Software Requirements

    Container Runtime - Kubernetes supports multiple container runtimes. Ensure one of these is installed and configured:

    - containerd (preferred and recommended)
    - Docker (requires CRI plugin, deprecated after Kubernetes 1.24)
    - CRI-O
    - Packages

4. Installation Instructions

   - kubectl: CLI tool to manage the cluster.
   - kubeadm: Used to bootstrap the cluster.
   - kubelet: Responsible for running containers on nodes.

    Disable Swap Kubernetes requires swap to be disabled to function correctly.

    ```bash
    sudo swapoff -a
    ```

    To make this change permanent, comment out any swap entries in /etc/fstab.

    Enable Bridge-NF and IP Forwarding Kubernetes networking requires specific kernel parameters. Configure them as follows:

    ```bash

    cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
    overlay
    br_netfilter
    EOF

    sudo modprobe overlay
    sudo modprobe br_netfilter

    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-ip6tables = 1
    net.bridge.bridge-nf-call-iptables = 1
    net.ipv4.ip_forward = 1
    EOF

    sudo sysctl --system
    ```

    Firewall Configuration

    Allow traffic on ports used by Kubernetes components:

    ```bash
    sudo firewall-cmd --permanent --add-port=6443/tcp   # API server
    sudo firewall-cmd --permanent --add-port=2379-2380/tcp # etcd server
    sudo firewall-cmd --permanent --add-port=10250/tcp # kubelet API
    sudo firewall-cmd --reload
    ```

5. Network Requirements

    All nodes must be able to communicate with each other.

    Required ports:
    - Control Plane: 6443, 2379-2380, 10250, 10251, 10252
    - Worker Nodes: 10250, 30000-32767 (NodePort range)

6. Cluster Configuration

    Node Hostnames, Each node should have a unique hostname.  
    Update the hostname if necessary:

    ```bash
    sudo hostnamectl set-hostname <node-name>
    ```

    Time Synchronization
    Ensure time synchronization is set up using chrony or ntp.
    DNS and Host File Configuration
    Update the /etc/hosts file on all nodes with the control plane node's IP and hostname:

    ```bash
    <control-plane-node-ip> <control-plane-node-hostname>
    ```

7. Installing Kubernetes with kubeadm

   1. Install Prerequisites
        Install required packages:

        ```bash
        sudo apt-get update
        sudo apt-get install -y apt-transport-https ca-certificates curl
        curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
        echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
        sudo apt-get update
        sudo apt-get install -y kubelet kubeadm kubectl
        sudo apt-mark hold kubelet kubeadm kubectl
        ```

   2. Initialize the Control Plane
        On the control plane node:

        ```bash
        sudo kubeadm init --pod-network-cidr=10.244.0.0/16
        ```

   3. Set Up kubectl for the Admin User

        ```bash
        mkdir -p $HOME/.kube
        sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
        sudo chown $(id -u):$(id -g) $HOME/.kube/config
        ```

   4. Install a Pod Network Add-On
        Install a network plugin, such as Flannel:

        ```bash
        kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
        ```

   5. Join Worker Nodes
        On each worker node, join the cluster using the command provided by kubeadm init:

        ```bash
        sudo kubeadm join <control-plane-ip>:6443 --token <token> --discovery-token-ca-cert-hash <hash>
        ```

        If you don’t have the join command, you can regenerate it on the control plane node:

        ```bash
        kubeadm token create --print-join-command
        ```

   6. Verification

        Check nodes in the cluster:

        ```bash
        kubectl get nodes
        ```

   7. Check pods in all namespaces:

        ```bash
        kubectl get pods --all-namespaces
        ```

## Understanding Node Network Requirements in Kubernetes

Networking in Kubernetes is crucial for enabling communication between cluster nodes, workloads (Pods), and external users or systems. Properly configuring the network requirements ensures smooth operation of your Kubernetes cluster.

Below is an overview of the key node networking requirements and concepts.

1. Key Kubernetes Networking Concepts

   - Pod-to-Pod Communication
   Every Pod in a Kubernetes cluster gets its own IP address, and Pods can communicate with each other directly using these IPs.
   Requirement: All nodes must be able to reach every Pod on any node without NAT (Network Address Translation).
   - Pod-to-Service Communication
   Kubernetes services provide a stable IP and DNS name for accessing Pods, even if Pod IPs change.
   Requirement: Nodes must allow traffic between Pods and the ClusterIP addresses of services.
   - Node-to-Node Communication
   Nodes communicate to ensure the control plane and worker nodes operate cohesively.
   Requirement: Nodes need to communicate over specific ports for API server, kubelet, kube-proxy, etc.
   - External Communication
   Kubernetes must support traffic from external users or systems to access cluster workloads.
   Requirement: Nodes must allow traffic for exposing services via NodePort, LoadBalancer, or Ingress.

2. Network Requirements by Node Role

    Control Plane Node Requirements : Communication between the control plane and worker nodes is critical.

    Required ports

    ```bash
    6443/tcp: Kubernetes API server.
    2379-2380/tcp: etcd server (key-value store).
    10250/tcp: kubelet API for managing workloads.
    10251/tcp: kube-scheduler (internal cluster communications).
    10252/tcp: kube-controller-manager (internal cluster communications).
    ```

    Worker Node Requirements : Worker nodes communicate with the control plane and other nodes to manage workloads.

    Required ports:

    ```bash
    10250/tcp: kubelet API.
    30000-32767/tcp: NodePort range for services.
    Any additional ports based on the container runtime (e.g., CRI or Docker).
    ```

3. Cluster-Wide Network Requirements

    1. Pod Network CIDR
        Kubernetes clusters use a Pod network CIDR range to assign IPs to Pods. 

        For example:

        ```bash
        Flannel default: 10.244.0.0/16
        Calico default: 192.168.0.0/16
        ```

        Requirement: Ensure the Pod CIDR does not overlap with existing network ranges in your environment.

    2. Service CIDR

        Kubernetes services are assigned virtual IPs from a separate CIDR range. 

        For example: `Default: 10.96.0.0/12`
        Requirement: Ensure the service CIDR does not conflict with existing network ranges.

    3. DNS

        CoreDNS, or another DNS provider, resolves service names to ClusterIPs.  
        Requirement: Nodes must have access to the DNS service within the cluster.

    4. Required Ports

        Control Plane Node Ports - Port Range Protocol Purpose

        ```bash
        6443 TCP Kubernetes API server
        2379-2380 TCP etcd server communication
        10250 TCP Kubelet API
        10251 TCP kube-scheduler communication
        10252 TCP kube-controller-manager communication
        ```

        Worker Node Ports - Port Range Protocol Purpose
        10250 TCP Kubelet API
        30000-32767 TCP NodePort services
        Pod CIDR Range TCP/UDP Pod-to-Pod communication

4. Configuring Network Plugins

    Kubernetes itself does not handle networking, it relies on network plugins conforming to the Container Network Interface (CNI) specification. 

    Some popular CNI plugins include:

    - Flannel: Simple overlay network.
    - Calico: Provides advanced networking and network policies.
    - Weave Net: Offers automatic service discovery and encryption.
    - Cilium: Layer 7 observability and security.

    Steps to Configure Networking Using a CNI  
    Choose a CNI plugin compatible with your cluster.  
    Apply the CNI plugin’s YAML manifest after initializing the cluster.

    Example for Flannel:

    ```bash
    kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
    ```

    Verify that Pods receive IPs and can communicate across nodes.

5. Additional Considerations

    Firewall Rules : Ensure firewall rules allow traffic on the required ports for Kubernetes components and networking.
    Allow traffic between the Pod CIDR range, Service CIDR range, and nodes.

    Cloud-Specific Networking : If running Kubernetes in a cloud environment, configure networking based on the cloud provider’s requirements.  
    Most managed Kubernetes services (like AWS EKS, Azure AKS, or GKE) have native integrations.

    Network Policies : Network policies define rules for traffic flow between Pods and services.  
    Use tools like Calico or Cilium to enforce these policies.

6. Verifying Network Connectivity

    Ping Test Between Pods : Deploy Pods on different nodes and verify they can communicate:

    ```bash

    kubectl exec -it pod-a -- ping <pod-b-ip>
    ```

    Create a test service and ensure it is reachable via its ClusterIP or NodePort.

    DNS Test : Check if DNS resolution is working:

    ```bash
    kubectl exec -it pod-a -- nslookup <service-name>
    ```

## What different phases k8 execute while running kubeadm init

When you run kubeadm init, it executes a series of phases to set up a Kubernetes control plane. Each phase performs a specific task to bootstrap the cluster.

Phases of kubeadm init

1. Preflight Checks
    Validates system configuration (e.g., swap disabled, required ports open).  
    Ensures prerequisites are met.
2. kubelet Configuration
    Writes the kubelet configuration file (/var/lib/kubelet/config.yaml).  
    Enables and starts the kubelet service.
3. Certificates
    Generates and signs certificates for cluster components (e.g., API server, etcd).  
    Stores them in /etc/kubernetes/pki.
4. KubeConfig Files
    Creates kubeconfig files for communication with the cluster (admin.conf, kubelet.conf, etc.).  
    Stores them in /etc/kubernetes/.
5. etcd Initialization
    Bootstraps the etcd key-value store for cluster state management.
6. Kubernetes API Server
    Starts the API server and configures its certificates and kubeconfig.
7. Control Plane Components
    Deploys static Pods for: kube-apiserver, kube-controller-manager, kube-scheduler
8. Bootstrap Token
    Generates a token to allow worker nodes to join the cluster.
9. Cluster Network
    Configures basic networking (e.g., setting Pod CIDR).  
    Prepares for the installation of a network plugin (like Flannel or Calico).
10. Mark the Node
    Marks the control plane node with a specific taint to prevent scheduling Pods on it.

## Installation cluster

Refer the [github](https://github.com/sandervanvugt/cka.git), this contains script to install cluster.

install cri : `sudo /cka/setup-container.sh`

install kubetools : `sudo /cka/setup-kubetools.sh`, this includes (kubeadm, kubelet, kubectl)

install cluster : `sudo kubeadm init`, this need to run only on master node

setup client in master node:

```bash
mkdir ~/.kube
sudo cp -i /etc/kubernetes/admin.conf ~/.kube/config #to provide admin access to kubernetes cluster
sudo chown $(id -u):$(id -g) .kube/config
```

validate

```bash
kubectl get all # this should display type: clusterIP
```

Install network add-on

```bash
kubectl create -f https://raw.githubusercontent.com/projectcalico//calico/v3.25.0/manifests/tigera-operator.yaml

kubectl create -f https://raw.githubusercontent.com/projectcalico//calico/v3.25.0/manifests/custom-resources.yaml

watch kubectl get pods -n calico-system

# BAckup options: 
kubectl apply -f cka/calico.yaml

#validate
kubectl get pods -n kube-system #this will display calico status

# Join other nodes, execute this in worker nodes
sudo kubeadm join <join-token>

# validate worker nodes, execute this in master node
kubectl get nodes #this will display worker nodes
```

## K8 Applications

Running Applications

1. deploying k8 applications
   1. using deployment
   2. running agents with daemonsets
   3. understanding0 stateful and stateless applications
   4. the case for running individual pods
   5. managing pod initialization
   6. scaling applications
   7. sidecar containers for application logging
2. Managing storage
   1. understanding k8 storage options
   2. accessing storage through pod volumes
   3. configuring pv storage
   4. configuring pvc
   5. configuring pv and pvc with pod storage
   6. using storage class
   7. storage provisioner
   8. using configmap and secrets
3. managing application access

## doubts

