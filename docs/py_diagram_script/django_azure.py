from diagrams import Diagram, Cluster
from diagrams.onprem.client import Client  # Generic client for GitHub
from diagrams.azure.compute import ContainerInstance  # Use ContainerInstance as a placeholder for ACR
from diagrams.azure.database import SQLDatabases
from diagrams.azure.network import LoadBalancers
from diagrams.azure.web import AppService
from diagrams.azure.devops import DevOps  # For representing CI/CD pipeline, you can still use this

with Diagram("Django Deployment in Azure", show=True):
    # GitHub Repo for code (represented generically as a client)
    git_repo = Client("GitHub Repo")
    
    # CI/CD Pipeline (This can be GitHub Actions or Azure DevOps)
    with Cluster("CI/CD Pipeline"):
        build_image = DevOps("Build Docker Image")  # Representing the CI/CD pipeline step
    
    # Generic Container to represent Azure Container Registry
    acr = Client("Azure Container Registry")  # Using generic client for ACR
    
    # Django app inside Azure Container App (with database in Azure SQL)
    with Cluster("Django Application"):
        db = SQLDatabases("Azure SQL Database")
        container_app = ContainerInstance("Azure Container App")

    # Load Balancer for routing requests to the Django app
    load_balancer = LoadBalancers("Load Balancer")

    # End User accessing the application URL
    end_user = AppService("End User Access")
    
    # Define the flow
    git_repo >> build_image >> acr >> container_app
    container_app >> db  # Django app connects to SQL Database
    container_app >> load_balancer  # Container App is accessed through the Load Balancer
    load_balancer >> end_user  # End User accesses the app via URL
