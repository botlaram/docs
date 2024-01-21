FROM python:3.10-slim as builder


USER root

RUN apt-get update && apt-get install -y \
    graphviz git \
    && rm -rf /var/lib/apt/lists/*

