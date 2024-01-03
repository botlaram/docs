# Commands

### Python commands

| Execute                                          | Command
| ------------------------------------------------ | ----------------------------------------------
| Create virtual env                  | `python -m venv venv`
| Activate virtual environment        | Windows`./venv/bin/activate` <br> Linux`source venv/bin/activate`
| Deactivate virtual environment      | `deactivate`
| Install requirements.txt            | `pip install -r requirements.txt`
| Create requirements.txt | `pip freeze > requirements.txt`

### Docker commands

| Execute                                          | Command
| ------------------------------------------------ | ----------------------------------------------
| Build an Image from a Dockerfile                  | `docker build -t <image_name> `
| List all images                                    | `docker images / docker images ls`
| Run the container (--rm remove filesystem and associated resources (such as networking resources) when the container stops)      | `docker run --rm -p 80:5001 <image name>`
| Build an Image from a Dockerfile without the cache | docker build -t <image_name> . –no-cache 
| Delete an Image | `docker rmi <image_name>`
| Remove all unused images | `docker image prune` 
| Create and run a container from an image, with custom name: | `docker run --name <container_name> <image_name>`
| Run a container with and publish a container’s port(s) to the host. | `docker run -p <host_port>:<container_port> <image_name>`
| Run a container in the background    | `docker run -d <image_name>`
| Start or stop an existing container:  | `docker start|stop <container_name> (or <container-id>)`
| Kill running container  | `docker kill $ID`
| Remove a stopped container:    | `docker rm <container_name>`
| Open a shell inside a running container:    | `docker exec -it <container_name> sh`
| Fetch and follow the logs of a container:    | `docker logs -f <container_name>`
| To inspect a running container:    | `docker inspect <container_name> (or <container_id>)`
| To list currently running containers:    | `docker ps`
| List all docker containers (running and stopped):    | `docker ps --all`
| View resource usage stats    | `docker container stats`
| Delete all docker images  | `docker rmi $(docker images -q)`
| prune your entire system |  `docker system prune `
| change docker tag | `docker tag <image_id> <new_image_name:tag> `


### Git commands

| Execute                                          | Command
| ------------------------------------------------ | ----------------------------------------------
| Git configuration/set username                   | `git config--global user.name "<User name>"`
| Git configuration/set email                      | `git config --global user.email "xyz123@gmail.com"`
| Git configuration list                           | `git config-list`
| Git init                                         | ` git init <Repo Name>`
| Git clone                                        | `git clone <remote Url>`
| git clone particular branch                      | `git clone -b <branch-name> <git-url>`
| Create branch                                    | `git branch <branch name>`
| List all branch names                            | `git branch -a` <br> `git branch --list ` 
| Checkout branch                                  | `git checkout <branch name>`
| Checkout and switch to new branch                | `git checkout -b <branchname>`
| Git add single file                              | `git add <Filename> <Filename>`
| Git add all files                                | `git add .`
| Git status                                       | `git status`
| Git commit                                       | `git commit -m " Commit Message"`
| Git add+commit                                   | `git commit -am " Commit Message"`
| Git push                                         | `git push`
| Undo git add / Unstage All Files                 | `git reset`
| Undo git file / Unstage a Specific File:         |`git reset <file_name>`
| unstage a file but keep its changes in working dir  | `git reset HEAD <file_name>`
| Undo the Commit and Discard Changes               | `git reset --hard HEAD~1`
| Undo the Commit and Keep Changes                      | `git reset HEAD~1`
| Delete branch                                    | `git branch -d <branch_name>`
| Delete remote branch                             | `git push origin-delete <branch name>`
| Git commit history                               | `git log`
| Rename branch                                    | `git branch -m <old branch name> <new branch name>`
| Merge branch  | `vscode >` <br> `git clone url` <br> `git checkout main branch` <br> `git pull` <br> `git checkout feature branch` <br> `git merge main_branch` <br> ## if you want to update feature branch with main <br> ## you will get merge conflicts in vscode <br> ## resolve merge conflicts <br> `git commit` <br> ##check branch name and commit to your feature branch <br> `git push feature branch`
| Display the modified files                       | `git log --stat`
| Display the modification on each line of a file  | `git blame <filename> `
| Track changes that have not been staged          | `git diff`
| Track changes that have staged but not committed | `git diff --staged`
| Track the changes after committing a file        | `git diff HEAD`
| Track the changes between two commits            | `git diff <commit1-sha> <commit2-sha>`
| Git Diff Branches                                | `git diff <branch 1> < branch 2>`

### Kubernetes commands

| Execute                                          | Command
| ------------------------------------------------ | ----------------------------------------------
| To start Minikube                                | `minikube start`
| host minikube dashboard                          |   `minikube dashboard`
| host minikube dashboard url                      |   `minikube dashboard --url`
| Create a namespace                               | `kubectl create namespace development`
| Create a deployment using kubectl command         | `kubectl create deployment "nameofdeployment" --image="imagename"`<br>Example: `kubectl create deployment nginx-deploy --image=nginx`
| Deploy using a YAML file                          | `kubectl apply -f deployment.yaml`
| Display nodes                                    | `kubectl get nodes`
| Display services                                 | `kubectl get services`
| Display pods                                     | `kubectl get pods`
| Display pods with a specific namespace           | `kubectl get pods -n "namespace"`
| debug pods                                       | `kubectl describe pod "pod-name"`
| Display deployments                              | `kubectl get deployment`
| Display ReplicaSets                              | `kubectl get replicaset`
| Display config maps                              | `kubectl get cm`
| Display storage class                            | `kubectl get sc`
| Display Custom Resource Definition               | `kubectl get crd`
| Display Get Jobs                                 | `kubectl get jobs -n namespace`
| Display Scaled Jobs                              | `kubectl describe scaledjob <scaledjob-name> -n <namespace>`
| Display Secret Provider class                    | `kubectl get secretproviderclass`
| Display service status                           | `kubectl describe service "service-name"`
| Display changes of a config map                   | `kubectl describe cm "release-name"-configmap`
| Switch to a different namespace                   | `kubectl config set-context --current --namespace="namespace"`
| Display deployment file snippet in VS Code        | `$env:KUBE_EDITOR="code --wait" > kubectl edit deployment "deployment-name"`
| Display pod status                               | `kubectl get pods`<br>`kubectl describe pod "pod-name"`
| Display Secrets                                  | `kubectl get secret`
| Display describe secrets                         | `kubectl describe secret "secret-name"`
| Debug pod status with a specific namespace       | `kubectl describe pod "pod-name" -n development`
| Debug init container                             | `kubectl logs 'pod-name' -c init-cont-name`
| Debug pods with external IP addresses             | `kubectl get pod -o wide`
| Display pod logs                                 | `kubectl logs "pod-name" -n development`
| Interact with pods                               | `kubectl exec -it "pod-name" -- /bin/bash`
| Copy pods data to local system | `kubectl cp "pod-name":/etc/data/test.txt ./data/test.txt` <br> [pod_path local_path] 
| Delete all pods                                  | `kubectl delete pods --all -n development`
| Delete deployments                               | `kubectl delete deployment "deployment-name"`

### Helm commands

| Execute                                           | Commands |
| ------------------------------------------------- | -------- |
| Helm repo add bitnami                             | `helm repo add bitnami https://charts.bitnami.com/bitnami` |
| Helm repo update                                  | `helm repo update` |
| Helm repo list                                    | `helm repo list` |
| Minikube start                                    | `minikube start` |
| Kubectl create namespace                          | `kubectl create ns "namespace"` |
| Helm install kube-state-metrics                   | `helm install kube-state-metrics bitnami/kube-state-metrics -n metrics` |
| Helm create chart                                 | `helm create "chart-name"` |
| Helm lint                                         | `helm lint .` |
| Helm template with debug                          | `helm template --dry-run --debug "release-name" .` |
| Helm install status                               | `helm ls -n "namespace"` |
| Kubectl get all                                   | `kubectl get all -n "namespace"` |
| Helm install with namespace                       | `helm install demo-001 . -n development` |
| Helm upgrade                                      | `helm upgrade "release-name" .` |
| Helm upgrade with namespace                       | `helm upgrade demo-001 . -n development` |
| Helm history                                      | `helm history "release-name"` |
| Helm rollback                                     | `helm rollback "release-name"` |
| Helm rollback with revision                       | `helm rollback "release-name" "revision-number"` |
| Helm upgrade with specific version                | `helm upgrade kube-state-metrics bitnami/kube-state-metrics --version 0.4.0 -n metrics` |
| Helm delete                                       | `helm delete "release-name"` |
| Helm install with updated values                  | `helm install "release-name" --set data.type="9090"` |
| Kubectl port-forward for kube-state-metrics        | `kubectl port-forward svc/kube-state-metrics 8080:8080 -n metrics` |
| Helm show chart                                   | `helm show chart bitnami/kube-state-metrics` |
| Helm show values                                  | `helm show values bitnami/kube-state-metrics` |
| Helm uninstall                                    | `helm uninstall "release-name" . -n "namespace"` |




### Openshift commands

| Execute                                          | Command
| ------------------------------------------------ | ----------------------------------------------
| OpenShift login                                  | `oc login`
| Create new project                               | `oc new-project <project-name>`
| Switch to specific project                       | `oc project <project-name>`
| Check the project name                           | `oc project`
| Current status of project                        | `oc status`
| Display pods                                     | `oc get pods `
| Describe pod                                     | `oc describe pod <pod-name> `
| Display logs                                     | `oc logs <pod-name>`
| Display service of project                       | `goc get svc `
| Display specific service of project              | `oc describe svc <service-name> `
| Expose a service to the internet                 | `oc expose svc <service-name> `
| Delete a specific service.                       | `oc delete svc <service-name> `
| Create new application                           | `oc new-app`
| Edit a deployment configuration                  |  `oc edit dc <deployment-config>` 
| Scale a deployment configuration                | `oc scale dc <deployment-config> --replicas=<number>`
| Rollout to latest version of deployment configuration | `oc rollout latest <deployment-config>`





