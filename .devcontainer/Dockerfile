FROM python:3.9-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install nox

# # Create a non-root user named vscode and add it to the sudo group
# RUN useradd -ms /bin/bash vscode \
#     && echo 'vscode ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/nopasswd \
#     && chmod 0440 /etc/sudoers.d/nopasswd

# # Set the default user
# USER vscode