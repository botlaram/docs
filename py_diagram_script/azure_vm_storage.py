from diagrams import Diagram, Cluster
from diagrams.azure.compute import VM
from diagrams.azure.storage import BlobStorage  # Use a specific storage type
from diagrams.azure.network import VirtualNetworks

with Diagram("azure_vm", show=True):
    vn = VirtualNetworks("vn")
    
    with Cluster("virtual machines"):
        worker1 = VM("worker1")
        worker2 = VM("worker2")
        worker3 = VM("worker3")        
    
    with Cluster("storage"):
        storage = BlobStorage("storage")
    
    # Connect components
    vn >> [worker1, worker2, worker3] >> storage
