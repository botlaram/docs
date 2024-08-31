# Learnings

## Az

### [App Service](https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-app-service/7-create-html-web-app)

Azure Web App is a Platform-as-a-Service (PaaS) offering from Microsoft Azure that allows you to host web applications, RESTful APIs, and mobile backends without managing the underlying infrastructure. It is part of the Azure App Service platform, which provides a range of features for building and hosting web applications.

You can host az web app using cli, for this [index.html](https://github.com/Azure-Samples/html-docs-hello-world/blob/master/index.html) page should be present in parent dir.

```bash
az webapp up -g $resourceGroup -n $appName --html --location EastUS
```

#### Steps to setup app service

Create Azure Web App to host Py flask web application, using Azure CLI

1. az login

2. create resource group

    ```bash
    resourceGroup=$(az group list --query "[].{id:name}" -o tsv)
    appName=az204app$RANDOM
    ```

3. Verify resource group

    ```bash
    echo $resourceGroup
    ```

4. Create dir and cd dir

5. Git clone [this](https://github.com/botlaram/azure-web-app) repo

6. Run az web app create command

    ```bash
    az webapp up -g $resourceGroup -n $appName --runtime "PYTHON:3.9" --location CentralUS
    ```

    this will create web app service and zip src code, it will recognize that the src is python structure as py and requirements.txt will be present.

7. It will show the following logs and url hosted to access flask app.

    ```logs
    ramakrishnabotla04 [ ~/demo/azure ]$ az webapp up -g $resourceGroup -n $appName --runtime "PYTHON:3.9" --location CentralUS
    Webapp 'az204app18227' already exists. The command will deploy contents to the existing app.
    Creating AppServicePlan 'ramakrishnabotla04_asp_5823' or Updating if already exists
    Readonly attribute name will be ignored in class <class 'azure.mgmt.web.v2023_01_01.models._models_py3.AppServicePlan'>
    Creating zip with contents of dir /home/ramakrishnabotla04/demo/azure ...
    Getting scm site credentials for zip deployment
    Starting zip deployment. This operation can take a while to complete ...
    Deployment endpoint responded with status code 202
    Polling the status of async deployment. Start Time: 2024-08-25 13:44:55.291459+00:00 UTC
    Status: Building the app... Time: 3(s)
    Status: Building the app... Time: 19(s)
    Status: Build successful. Time: 36(s)
    Status: Starting the site... Time: 52(s)
    Status: Site started successfully. Time: 69(s)
    You can launch the app at http://az204app18227.azurewebsites.net
    Setting 'az webapp up' default arguments for current directory. Manage defaults with 'az configure --scope local'
    --resource-group/-g default: learn-e2a9e9ac-ede2-4607-8219-42db48e581fa
    --sku default: F1
    --plan/-p default: ramakrishnabotla04_asp_5823
    --location/-l default: centralus
    --name/-n default: az204app18227
    {
    "URL": "http://az204app18227.azurewebsites.net",
    "appserviceplan": "ramakrishnabotla04_asp_5823",
    "location": "centralus",
    "name": "az204app18227",
    "os": "Linux",
    "resourcegroup": "learn-e2a9e9ac-ede2-4607-8219-42db48e581fa",
    "runtime_version": "PYTHON|3.9",
    "runtime_version_detected": "-",
    "sku": "PAID",
    "src_path": "//home//ramakrishnabotla04//demo//azure"
    }
    ```

8. Access py flask app using url

    ```url
    http://az204app18227.azurewebsites.net
    ```

### Setup Project configure complete [CI/CD](https://www.youtube.com/watch?v=aAjH9wqtx9o&list=PLdpzxOOAlwvIcxgCUyBHVOcWs0Krjx9xR&index=15)

Host voting app src provided by docker, [docker sample voting app](https://github.com/dockersamples/example-voting-app/blob/main/README.md)

#### Steps to setup project

Need to create 3 different pipelines for
[vote](https://github.com/dockersamples/example-voting-app/tree/main/vote)
[result](https://github.com/dockersamples/example-voting-app/tree/main/result)
[worker](https://github.com/dockersamples/example-voting-app/tree/main/worker)

Project CI, setup VM and use as Agent.

1. create a new project (import from github)
2. create a new resource grp
3. create vm and container registry to store docker image
4. create pool in az board settings > agentpool.
5. After creating agentpool > agent_pool_name > new agent > select the OS to install agent install script.
6. login in VM (with password or ssh) and install agent script.
7. to create and push docker image. Install docker in VM.
8. create new pipeline to build and push to az Container registry for vote Docker image

Project CD setup hosting K8 using Azure AKS and install Argocd to deploy K8 components.

1. create k8 service in azure portal.
2. choose VM to install K8 cluster and to manage pods in it.
3. login to K8 and install Argocd.
4. access argocd and configure repo connection
5. deploy [k8-specifications](https://github.com/dockersamples/example-voting-app/tree/main/k8s-specifications).
6. to pull Image from Private registry. Configure K8 ImagePullSecrets

    ```bash
    kubectl create secret docker-registry <secret-name> \
    --namespace <namespace> \
    --docker-server=<container-registry-name>.azurecr.io \
    --docker-username=<service-principal-ID> \
    --docker-password=<service-principal-password>
    ```

7. port forward the vote svc to access externally.

## Argocd

### Handle multi-cluster and configure [Argocd](https://www.youtube.com/watch?v=QhDnXsmSnfk)

Configuring Argo-cd to multi-cluster is also known as Hub-Spoke Model.

#### What is the hub and spoke model strategy

The hub and spoke model is a model of distribution for goods in which there's a single centralized hub. All the goods sent to customers come from this one hub before being sent to distribution centers and then to consumers. The hub is the central location, while the spokes are the small distribution centers.

#### Setup

1. Create 3 clusters as hub and 2 spoke
2. kubectl config get-contexts (to display all created cluster)
3. login to hub cluster

    ```kubectl config use-context <cluster-name>```

4. Verify cluster login

    ```kubectl config current-context```

5. create namespace and install Argocd

6. port forward, setup HTTP to access Argo-cd UI.

7. Add cluster to Argocd, this is done by argocd cli.

   a. ```kubectl config get-clusters``` display all available cluster  
   b. ```agrocd login <ip-address:port-or-url>``` login to argocd  
   c. ```argocd add cluster <cluster-name>```
