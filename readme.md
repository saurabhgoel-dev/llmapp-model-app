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

## Development

Developing an app to categorise the sentences into POSITIVE and NEGATIVE. The app would take sentences as inputs from the users and out put the sentiments.

### 1. Save the Model on Local 

I have leveraged a relatively small model [A finetuned version of DistilBert](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english).

### 2. Develop a function to pass sentence and extract an output

### 3. Develop a REST API with a POST endpoint

## Deployment

### 1. Create a Dockerfile and a Docker Image

### 2. Create a Kubernetes Cluster

### 3. Create Deployment and Services config files

### 4. Apply config files