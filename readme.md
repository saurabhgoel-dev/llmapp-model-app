# Building a LLM Deployment Pipeline in Kubernetes

## Overall Aim

Develop orchestration methodology leveraging Kubernetes and Helm Charts to deploy apps based on large language models on multi instance GPU clusters.

## Current Version Aim

As a proof of concept, leverage smaller LLM model and simpler use case which can be developed quickly and can be deployed locally with minimal resource requirement.

The focus of current version is to develop a blueprint that can be leveraged in later versions.

## Methodology

1. Develop an app levergaing a small LLM such as DistilBERT which can be developed locally. This is to create a proof of concept
2. Create a REST API using FastAPI framework in python. This is done to deploy the app as a microservice. The out of this microservice then can be leveraged in a UI to interact with users
3. Create a Docker Image of this REST API and push the image to the Docker Hub.
4. Develop Config Files to deploy the image on Kubernetes.
5. Create a project, GKE Cluster in Google Cloud and deploy the config files