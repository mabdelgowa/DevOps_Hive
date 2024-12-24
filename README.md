# DevOps_Hive
[![Dynamic DevOps Roadmap](https://devopshive.net/badges/dynamic-devops-roadmap.svg)](https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap)

## End-to-End Project: HiveBox
Almost everyone loves honey, and we at DevOps Hive love it too and appreciate the role that bees play for the planet! Because bees are essential to people and planet.
For that reason, in this roadmap our main hands-on project will be for the bees! We will utilize the technology and open source software to build an API to track the environmental sensor data from openSenseMap, a platform for open sensor data in which everyone can participate.

## Goal
The goal of this project is to build a scalable RESTful API around openSenseMap but customized to help beekeeper with their chores. The API output should be in JSON. You will start with a basic implementation, then extend the whole system to handle thousands of requests per second. But always remember, every decision has a cost.

You can get senseBox IDs by checking the openSenseMap website. Use 3 senseBox IDs close to each other (you can use this one 5eba5fbad46fb8001b799786 as a starting point). Just copy the IDs, you will need them in the next steps.

we will change whole things in this file

## Software Project Management
This project was built in the KANBAN agile methodology with jira
![image](https://github.com/user-attachments/assets/17685dbf-54ff-45b1-95bf-95d1bdf8c31a)   ![image](https://github.com/user-attachments/assets/d2e2bea2-65e2-41f0-b6ae-189062a20f2e)

![image](https://github.com/user-attachments/assets/a497a63e-45e7-42d9-98e7-1b4be93e9d54)   ![image](https://github.com/user-attachments/assets/6f03563b-71a6-4181-87ac-ec4f5ba92f97)






## This is a complete DevOps project with the following tools:
* 1- Docker & Dockerhub
* 2- Github actions
* 3- python (fastapi, pylint, pytest)
* 4- ArgoCD for (continuous delivery)
* 5- Terraform
* 6- Kubernetes ( kind, helm, kustomize) 
* 7- Terrascan 
* 8- Sonarqube
* 9- Grafana cloud 


  ## 1- Docker & Dockerhub
  * Dockerfile builds the app with all environment dependencies and I selected the official python image as our app is written in Python.
  * After building the image it will be pushed to my docker hub repo 

  ## 2- Github Actions
  * Create a GitHub Actions workflow for CI using a template for a python project.
  * Add step to lint code and Dockerfile.
  * Add a step to build the Docker image.
  * Add step to unit tests.
  * Setup OpenSSF Scorecard GitHub Action and fix any issues reported by it.
  * Run tests using terrascan
    (note: the build and push of the docker image won't happen unless the commit message is "build")
 
  ## 3- Python
  * Used pycharm IDE for creating and editing.
  * Used fastapi to implement our cod
  * Used requests package to send requests to openSenseMap API.
  * Write unit test using pytest.
  * Lint the code using pylint 

  ## 4- ArgoCD
  * appling gitops concept.
    -	Installing argo project
    -	Open ports for argo project
    -	Authentication for argo project
    -	argo application manifest
    -	Running argocd

  ## 5- Terraform
*  * 1- VPC.tf:
     * This file will create a VPC using VPC module and provision some resources in this VPC like nat gateway, public subnet, and private subnet
*  * 2- eks-cluster.tf:
     * This file will use eks module to provision all eks cluster resources  like cluster name and instances type

* Note: there is also a file (terraform.tfvars) for assigning variables which will be needed in the two previous files

  ## 6- Kubernetes
  * Manifests for Kubernetes to deploy the app using them on Kubernetes with adding config to support high availability and volume persistence and exposing service to the public (using kind to test).
  * Create KIND config to run with Ingress-Nginx.
  * Create a Helm chart for the application.
  * Create Kustomize manifests for the application.
  * Configure the Kubernetes app manifest to use /readyz as a readiness probe.

  ## 7-Terrascan
  * Run Terrascan for Kubernetes manifest misconfigurations and vulnerabilities.
  * Reviewing some important vulnerabilities from actions and covering them.

  ## 8-Sonarqube
  * Run SonarQube for code quality, security, and static analysis. ( used Sonarcloud free account to run these analyses)

  ## 9- Grafana Cloud
  *Deploy Grafana agent to collect logs and metrics ( Created Grafana Cloud free account to Use Loki and Grafana)




  ## Documentation Video
  [Documentation Video](https://drive.google.com/file/d/1uzsoCL1jlrvrW7zh33-U50LaMx_dwRDS/view?usp=drive_link)
