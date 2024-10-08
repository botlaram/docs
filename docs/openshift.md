# Openshift

## installation

### self-managed

To install openshift on VM it should have OS (RHEL, RHCOS).

### service-managed

1. AWS (ROSA)
2. AZURE (ARO : Azure Redhat Openshift)

HA (High Availability)
To install openshift for HA (High Availability), we need to have atleast 3 control plane,  
each control plane must contain minimum (32 CPU, 32 GB RAM).

SNO (Single Node Openshift)

This installation is cost efffective, but this can be used when Org. have 70 users  
it needs (64 GB Ram, 16-32 CPU)

## Features

Openshift offers Advance feature as:

1. Operators
2. GITOPS
3. Networking (CRO, SDN)
4. CI\CD
5. Observisibilty
6. User Management (SSO)
7. User Interface

## Openshift route

Route has rich tls configuration

Types of TLS Termination

1. Edge Termination:

    In Edge termination, TLS is terminated at the OpenShift router.

    The traffic between the client and the OpenShift router is encrypted, but traffic from the OpenShift router to the pod (your service) is unencrypted.

    This is useful when you want to offload the TLS termination to the OpenShift infrastructure (router).

2. Passthrough Termination:

    With Passthrough termination, the router does not terminate TLS. Instead, it passes encrypted 
    TLS traffic directly to the backend pod.

    The pod itself is responsible for handling TLS termination and decryption.

    This is useful if you want your application to fully control encryption.

3. Re-encrypt Termination:

    In Re-encrypt termination, TLS is terminated at the OpenShift router, and a new encrypted connection is created between the router and the backend pod.

    This ensures that data remains encrypted between the client, router, and pod.
