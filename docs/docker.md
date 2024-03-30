# Hands-on Docker

## python commands

```shell
python .\app.py

python -m venv .venv

pip install flask

python.exe .\app.py
```

## create Dockerfile

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install flask

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
ENTRYPOINT ["/bin/bash"]
```

## docker commands

```shell
docker build -t image-url:docker-demo .
(-t for <name>:<tag> | default it will take as latest)

docker run -it "image-id"

docker run -it -p 8000:8000 d9b65d5d6ab2

docker login global-registry

docker push image-url:docker-demo

# docker image pull
docker image-url:docker-demo
```
