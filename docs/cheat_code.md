# Commands

## Python commands

| Execute                                          | Command
| ------------------------------------------------ | --------------------------------------
| Create virtual env                               | `python -m venv venv`
| Activate virtual environment        | Windows   `./venv/bin/activate` <br> Linux   `source venv/bin/activate`
| Deactivate virtual environment                   | `deactivate`
| Install requirements.txt                         | `pip install -r requirements.txt`
| Create requirements.txt | `pip freeze > requirements.txt`
| Upgrade a Package                                 | `pip install --upgrade <package-name>`
| List Installed Packages                           | `pip list`
| Show Package Details                              | `pip show <package-name>`
| Install package from git repository      | `pip install git+https://github.com/psf/requests.git`
| Configure Pip Settings                |`pip config set global.index-url https://pypi.org/simple`

## Docker commands

| **Category**                    | **Command**                                     |
|----------------------------------|------------------------------------------------|
| **Image Management**              |                                                |
| Build an image from a Dockerfile           | `docker build -t <image_name> .`               |
| Build an image without cache              | `docker build -t <image_name> . --no-cache`    |
| List all images                           | `docker images`                                |
| Delete an image                             | `docker rmi <image_name>`                      |
| Remove all unused images                    | `docker image prune`                           |
| Delete all images                           | `docker rmi $(docker images -q)`               |
| Tag an image                                | `docker tag <image_id> <new_image_name:tag>`   |
| Pull an image from Docker Hub               | `docker pull <image_name>`                     |
| Push an image to Docker Hub      | `docker push <image_name>`                     |
| **Container Management**        |                                                |
| Run a container                  | `docker run <image_name>`                      |
| Run and remove container on stop | `docker run --rm -p 80:5001 <image_name>`      |
| Create and name a container      | `docker run --name <container_name> <image_name>` |
| Run in the background (detached) | `docker run -d <image_name>`                   |
| Run with port mapping            | `docker run -p <host_port>:<container_port> <image_name>` |
| Run with volume mapping          | `docker run -v <host_path>:<container_path> <image_name>` |
| Start a container                | `docker start <container_name>`                |
| Stop a container                 | `docker stop <container_name>`                 |
| Restart a container              | `docker restart <container_name>`              |
| Kill a running container         | `docker kill <container_name>`                 |
| Remove a stopped container       | `docker rm <container_name>`                   |
| Remove all stopped containers               | `docker container prune`                       |
| **Container Inspection**                   |                                                |
| List running containers                     | `docker ps`                                    |
| List all containers                         | `docker ps --all`                              |
| Fetch logs                                  | `docker logs <container_name>`                 |
| Follow logs in real-time                    | `docker logs -f <container_name>`              |
| Inspect container details                   | `docker inspect <container_name>`              |
| Check resource usage stats                  | `docker container stats`                       |
| Open a shell inside a container             | `docker exec -it <container_name> sh`          |
| Execute a command in container              | `docker exec -it <container_name> <command>`   |
| **Network Management**          |                                                |
| List networks                    | `docker network ls`                            |
| Create a network                 | `docker network create <network_name>`         |
| Inspect a network                | `docker network inspect <network_name>`        |
| Connect a container to a network | `docker network connect <network_name> <container_name>` |
| Disconnect a container from a network | `docker network disconnect <network_name> <container_name>` |
| Remove a network                 | `docker network rm <network_name>`             |
| **Volumes Management**          |                                                |
| List volumes                     | `docker volume ls`                             |
| Create a volume                  | `docker volume create <volume_name>`           |
| Inspect a volume                 | `docker volume inspect <volume_name>`          |
| Remove a volume                  | `docker volume rm <volume_name>`               |
| Remove unused volumes            | `docker volume prune`                          |
| Use a volume in a container      | `docker run -v <volume_name>:<path> <image_name>` |
| **System Cleanup**              |                                                |
| Remove unused objects            | `docker system prune`                          |
| Clean unused volumes             | `docker volume prune`                          |
| Clean unused images              | `docker image prune`                           |
| Clean unused networks            | `docker network prune`                         |
| **Miscellaneous**               |                                                |
| Display Docker version           | `docker --version`                             |
| Display system-wide information  | `docker info`                                  |
| Login to Docker Hub              | `docker login`                                 |
| Logout from Docker Hub           | `docker logout`                                |
| Save an image to a tar file      | `docker save -o <filename.tar> <image_name>`   |
| Load an image from a tar file    | `docker load -i <filename.tar>`                |
| Export a container to a tar file | `docker export <container_name> > <file.tar>`  |
| Import a tar file as an image    | `docker import <file.tar> <image_name>`        |
| Pause a container                | `docker pause <container_name>`                |
| Unpause a container              | `docker unpause <container_name>`              |
| Rename a container               | `docker rename <old_name> <new_name>`          |
| View Docker events               | `docker events`                                |

## Git commands

| **Category**                      | **Command**                                      |
|-----------------------------------|--------------------------------------------------|
| **Configuration**                 |                                                  |
| Set username                      | `git config --global user.name "<User name>"`    |
| Set email                         | `git config --global user.email "xyz123@gmail.com"` |
| List configuration                | `git config --list`                              |
| Set default editor                | `git config --global core.editor "<editor>"`     |
| **Repository Initialization**     |                                                  |
| Initialize repository             | `git init <Repo Name>`                           |
| Clone repository                  | `git clone <remote URL>`                         |
| Clone specific branch             | `git clone -b <branch-name> <git-url>`           |
| **Branch Management**             |                                                  |
| Create branch                     | `git branch <branch name>`                       |
| List branches                     | `git branch -a`                                  |
| Checkout branch                   | `git checkout <branch name>`                     |
| Create and switch to branch       | `git checkout -b <branch name>`                  |
| Delete branch                     | `git branch -d <branch name>`                    |
| Force delete branch               | `git branch -D <branch name>`                    |
| Rename branch                     | `git branch -m <old branch name> <new branch name>` |
| Delete remote branch              | `git push origin --delete <branch name>`         |
| **Staging and Commit**            |                                                  |
| Add specific files to stage       | `git add <filename> <filename>`                  |
| Add all changes to stage          | `git add .`                                      |
| View status of changes            | `git status`                                     |
| Commit staged changes             | `git commit -m "Commit message"`                 |
| Add and commit simultaneously     | `git commit -am "Commit message"`                |
| Amend last commit                 | `git commit --amend`                             |
| Undo staged changes               | `git reset`                                      |
| Unstage specific file             | `git reset <file_name>`                          |
| Unstage file but keep changes     | `git reset HEAD <file_name>`                     |
| Undo commit and keep changes      | `git reset HEAD~1`                               |
| Undo commit and discard changes   | `git reset --hard HEAD~1`                        |
| **Pull and Push**                 |                                                  |
| Pull latest changes               | `git pull`                                       |
| Pull with rebase                  | `git pull --rebase`                              |
| Push changes                      | `git push`                                       |
| Push specific branch              | `git push origin <branch name>`                  |
| Set upstream branch               | `git push --set-upstream origin <branch name>`   |
| **Merge and Revert**              |                                                  |
| Merge branches                    | `git merge <branch name>`                        |
| Revert a commit                   | `git revert <commit_hash>`                       |
| **Logs and History**              |                                                  |
| View commit history               | `git log`                                        |
| View history with stats           | `git log --stat`                                 |
| View changes line by line         | `git blame <filename>`                           |
| View changes between commits      | `git diff <commit1-sha> <commit2-sha>`           |
| View changes in branch comparison | `git diff <branch1> <branch2>`                   |
| **Remote Management**             |                                                  |
| View remotes                      | `git remote -v`                                  |
| Add new remote                    | `git remote add <name> <url>`                    |
| Change remote URL                 | `git remote set-url <name> <new-url>`            |
| Remove remote                     | `git remote remove <name>`                       |
| Fetch changes                     | `git fetch`                                      |
| **Cleaning and Optimization**     |                                                  |
| Remove untracked files            | `git clean -fd`                                  |
| Remove untracked files and dirs   | `git clean -fdx`                                 |
| Prune remote-tracking branches    | `git remote prune origin`                        |
| Optimize repository               | `git gc`                                         |
| **Rebase and Cherry-Pick**        |                                                  |
| Start rebase                      | `git rebase <branch>`                            |
| Abort rebase                      | `git rebase --abort`                             |
| Continue rebase after conflict    | `git rebase --continue`                          |
| Cherry-pick a commit              | `git cherry-pick <commit-hash>`                  |
| **Tags**                          |                                                  |
| Create a tag                      | `git tag <tag-name>`                             |
| Create annotated tag              | `git tag -a <tag-name> -m "Tag message"`         |
| Push tags to remote               | `git push origin <tag-name>`                     |
| List tags                         | `git tag`                                        |
| Delete local tag                  | `git tag -d <tag-name>`                          |
| Delete remote tag                 | `git push origin --delete <tag-name>`            |
| **Miscellaneous**                 |                                                  |
| Stash changes                     | `git stash`                                      |
| View stashes                      | `git stash list`                                 |
| Apply last stash                  | `git stash apply`                                |
| Delete a stash                    | `git stash drop <stash@{index}>`                 |
| Create patch                      | `git format-patch <commit-range>`                |
| Apply patch                       | `git apply <patch-file>`                         |
| Merge branch  | `vscode >` <br> `git clone url` <br> `git checkout main branch` <br> `git pull` <br> `git checkout feature branch` <br> `git merge main_branch` <br> ## if you want to update feature branch with main <br> ## you will get merge conflicts in vscode <br> ## resolve merge conflicts <br> `git commit` <br> ##check branch name and commit to your feature branch <br> `git push feature branch` |
| Clone other's code and push to your repo  | `git clone` <br> `git remote -v` <br> `git remote set-url origin <add-your-url>` <br> `git remote -v` <br> `git push origin` |

## Kubernetes commands

| **Category**                   | **Command**                      |
|--------------------------------|-----------------------------------------------------------|
| **Minikube Operations**        |                                                          |
| Start Minikube                 | `minikube start` |
| Host Minikube dashboard        | `minikube dashboard` |
| Get Minikube dashboard URL     | `minikube dashboard --url` |
| **Namespace Commands**         |                                                    |
| Create a namespace             | `kubectl create namespace <namespace>` |
| List all namespaces            | `kubectl get namespaces` |
| Switch to a namespace         | `kubectl config set-context --current --namespace=<namespace>` |
| Display pods in a namespace    | `kubectl get pods -n <namespace>` |
| Delete all pods in a namespace | `kubectl delete pods --all -n <namespace>` |
| **Deployment and Apply Commands** |                                                  |
| Create a deployment      | `kubectl create deployment <deployment-name> --image=<image-name>` |
| Example                        | `kubectl create deployment nginx-deploy --image=nginx` |
| Deploy using a YAML file       | `kubectl apply -f <file.yaml>` |
| Edit a deployment in VS Code   | `$env:KUBE_EDITOR="code --wait" > kubectl edit deployment <deployment-name>` |
| Delete a deployment            | `kubectl delete deployment <deployment-name>` |
| Scale a deployment       | `kubectl scale deployment <deployment-name> --replicas=<number>` |
| Restart a deployment           | `kubectl rollout restart deployment <deployment-name>` |
| **Display Resource Information** |                                                    |
| Display nodes                  | `kubectl get nodes` |
| Display services               | `kubectl get services` |
| Display pods                   | `kubectl get pods` |
| Display deployments            | `kubectl get deployments` |
| Display ReplicaSets            | `kubectl get replicasets` |
| Display config maps            | `kubectl get configmaps` |
| Display storage classes        | `kubectl get storageclasses` |
| Display CRDs                   | `kubectl get crds` |
| Display secrets                | `kubectl get secrets` |
| Display Secret Provider class  | `kubectl get secretproviderclass` |
| Display events                 | `kubectl get events`|
| **Debug Commands**             |                                                     |
| Describe a pod                 | `kubectl describe pod <pod-name>` |
| Describe a service             | `kubectl describe service <service-name>` |
| Describe a config map          | `kubectl describe configmap <configmap-name>` |
| Debug pod logs                 | `kubectl logs <pod-name>` |
| Debug pod logs with namespace  | `kubectl logs <pod-name> -n <namespace>` |
| Debug init container logs      | `kubectl logs <pod-name> -c <init-container-name>` |
| Debug pod status with wide view| `kubectl get pods -o wide` |
| Interact with a pod            | `kubectl exec -it <pod-name> -- /bin/bash` |
| Copy files from a pod          | `kubectl cp <pod-name>:<path-in-pod> <local-path>` |
| Port-forward to access a pod   | `kubectl port-forward <pod-name> <local-port>:<pod-port>` |
| **Apply and Manage Configurations** |                                                    |
| Apply a configuration file     | `kubectl apply -f <file.yaml>` |
| Delete resources from a file   | `kubectl delete -f <file.yaml>` |
| Check rollout status           | `kubectl rollout status deployment/<deployment-name>` |
| Undo a rollout                 | `kubectl rollout undo deployment/<deployment-name>` |
| **Clean-up Commands**          |                                                      |
| Delete all pods                | `kubectl delete pods --all` |
| Delete all resources in namespace | `kubectl delete all --all -n <namespace>` |
| Delete a resource              | `kubectl delete <resource-type> <resource-name>` |
| Force delete a pod             | `kubectl delete pod <pod-name> --grace-period=0 --force` |
| **Miscellaneous Commands**     |                                                  |
| Check cluster info             | `kubectl cluster-info` |
| Check current context          | `kubectl config current-context` |
| List all contexts              | `kubectl config get-contexts` |
| Set a default namespace for a context | `kubectl config set-context --current --namespace=<namespace>` |
| View resource usage            | `kubectl top nodes` |
| Monitor pod resource usage     | `kubectl top pods -n <namespace>` |

## Helm commands

| Execute                                          | Command
| ------------------------------------------------ | -------------------------
| Helm repo add bitnami                             | `helm repo add bitnami https://charts.bitnami.com/bitnami`
| Helm repo update                                  | `helm repo update`
| Helm repo list                                    | `helm repo list`
| Minikube start                                    | `minikube start`
| Kubectl create namespace                          | `kubectl create ns "namespace"`
| Helm install kube-state-metrics                   | `helm install kube-state-metrics bitnami/kube-state-metrics -n metrics`
| Helm create chart                                 | `helm create "chart-name"`
| Helm lint                                         | `helm lint .`
| Helm template with debug                          | `helm template --dry-run --debug "release-name" .`
| Helm install status                               | `helm ls -n "namespace"`
| Kubectl get all                                   | `kubectl get all -n "namespace"`
| Helm install with namespace                       | `helm install demo-001 . -n development`
| Helm upgrade                                      | `helm upgrade "release-name" .`
| Helm upgrade with namespace                       | `helm upgrade demo-001 . -n development`
| Helm history                                      | `helm history "release-name"`
| Helm rollback                                     | `helm rollback "release-name"`
| Helm rollback with revision                       | `helm rollback "release-name" "revision-number"`
| Helm upgrade with specific version                | `helm upgrade kube-state-metrics bitnami/kube-state-metrics --version 0.4.0 -n metrics`
| Helm delete                                       | `helm delete "release-name"`
| Helm install with updated values                  | `helm install "release-name" --set data.type="9090"`
| Kubectl port-forward for kube-state-metrics       | `kubectl port-forward svc/kube-state-metrics 8080:8080 -n metrics`
| Helm show chart                                   | `helm show chart bitnami/kube-state-metrics`
| Helm show values                                  | `helm show values bitnami/kube-state-metrics`
| Helm uninstall                                  | `helm uninstall "release-name" . -n "namespace"`

## Openshift commands

| Execute                                          | Command
| ------------------------------------------------ | ---------------------------------------
| OpenShift login                                  | `oc login`
| Create new project                               | `oc new-project <project-name>`
| Switch to specific project                       | `oc project <project-name>`
| Check the project name                           | `oc project`
| Current status of project                        | `oc status`
| Display pods                                     | `oc get pods`
| Describe pod                                     | `oc describe pod <pod-name>`
| Display logs                                     | `oc logs <pod-name>`
| Display service of project                       | `oc get svc`
| Display specific service of project              | `oc describe svc <service-name>`
| Expose a service to the internet                 | `oc expose svc <service-name>`
| Delete a specific service.                       | `oc delete svc <service-name>`
| Create new application                           | `oc new-app`
| Edit a deployment configuration                  | `oc edit dc <deployment-config>`
| Scale a deployment configuration              | `oc scale dc <deployment-config> --replicas=<number>`
| Rollout to latest version of deployment configuration | `oc rollout latest <deployment-config>`

## Terraform

| **Category**                   | **Command**                                      |
|--------------------------------|--------------------------------------------------|
| **General Commands**           |                                                  |
| Terraform version              | `terraform --version`                            |
| Terraform help                 | `terraform --help`                               |
| **Formatting Commands**        |                                                  |
| Format files                   | `terraform fmt`                                  |
| Format files recursively       | `terraform fmt --recursive`                      |
| Show format changes            | `terraform fmt --diff`                           |
| Check formatting               | `terraform fmt --check`                          |
| **Initialization Commands**    |                                                  |
| Initialize project             | `terraform init`                                 |
| Initialize without plugins     | `terraform init -get-plugins=false`              |
| Initialize without state lock  | `terraform init -lock=false`                     |
| Migrate state to backend       | `terraform init -migrate-state`                  |
| Reconfigure backend            | `terraform init -reconfigure`                    |
| Upgrade modules and providers  | `terraform init -upgrade`                        |
| **Module Commands**            |                                                  |
| Download modules               | `terraform get`                                  |
| Update modules                 | `terraform get -update`                          |
| **Validation Commands**        |                                                  |
| Validate configuration         | `terraform validate`                             |
| Validate in JSON format        | `terraform validate -json`                       |
| **Planning Commands**          |                                                  |
| Generate execution plan        | `terraform plan`                                 |
| Save execution plan to file    | `terraform plan -out=<path>`                     |
| Plan for destruction           | `terraform plan -destroy`                        |
| Plan with variables            | `terraform plan -var="key=value"`                |
| Plan with variable file        | `terraform plan -var-file="filename.tfvars"`     |
| Plan with refresh disabled     | `terraform plan -refresh=false`                  |
| **Apply Commands**             |                                                  |
| Apply changes                  | `terraform apply`                                |
| Auto-approve apply             | `terraform apply --auto-approve`                 |
| Apply with variables           | `terraform apply -var="key=value"`               |
| Apply with variable file       | `terraform apply -var-file="filename.tfvars"`    |
| Apply a saved plan             | `terraform apply <plan file>`                    |
| **Destruction Commands**       |                                                  |
| Destroy resources              | `terraform destroy`                              |
| Auto-approve destroy           | `terraform destroy --auto-approve`               |
| Destroy with variables         | `terraform destroy -var="key=value"`             |
| Destroy with variable file     | `terraform destroy -var-file="filename.tfvars"`  |
| **State Management Commands**  |                                                  |
| Display state                  | `terraform show`                                 |
| Display state file             | `terraform show <statefile>`                     |
| Refresh state                  | `terraform refresh`                              |
| List resources in state        | `terraform state list`                           |
| Push state to backend          | `terraform state push`                           |
| Remove resource from state     | `terraform state rm <resource>`                  |
| Move resource in state         | `terraform state mv <src> <dest>`                |
| Lock state                     | `terraform force-unlock <lock ID>`               |
| Import resource to state       | `terraform import <address> <resource ID>`       |
| Show resource state details    | `terraform state show <resource>`                |
| **Resource Lifecycle Commands**|                                                  |
| Force resource recreation      | `terraform taint <resource>`                     |
| Remove taint from resource     | `terraform untaint <resource>`                   |
| **Provider Commands**          |                                                  |
| List providers                 | `terraform providers`                            |
| **Workspace Commands**         |                                                  |
| List workspaces                | `terraform workspace list`                       |
| Show current workspace         | `terraform workspace show`                       |
| Create a new workspace         | `terraform workspace new <workspace>`            |
| Delete a workspace             | `terraform workspace delete <workspace>`         |
| Select a workspace             | `terraform workspace select <workspace>`         |
| **Debugging Commands**         |                                                  |
| Debug a command                | `terraform -debug <command>`                     |
| Show logs                      | `TF_LOG=<level> terraform <command>`             |
| Enable detailed logs           | `TF_LOG=TRACE terraform <command>`               |
| **Miscellaneous Commands**     |                                                  |
| Create graph of resources      | `terraform graph`                                |
| Generate graph to file         | `terraform graph \ dot -Tpng > graph.png`        |
| Output resource values         | `terraform output`                               |
| Output specific value          | `terraform output <output name>`                 |
| Suppress colored output        | `terraform <command> -no-color`                  |
| Show available providers       | `terraform providers schema`                     |
