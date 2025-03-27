# DevOps_Hive
[![Dynamic DevOps Roadmap](https://devopshive.net/badges/dynamic-devops-roadmap.svg)](https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap)

## End-to-End Project: HiveBox
Almost everyone loves honey, and we at DevOps Hive love it too and appreciate the role that bees play for the planet! Because bees are essential to people and planet.
For that reason, in this roadmap our main hands-on project will be for the bees! We will utilize the technology and open source software to build an API to track the environmental sensor data from openSenseMap, a platform for open sensor data in which everyone can participate.

## Overview
DevOps_Hive is a comprehensive DevOps project integrating modern CI/CD, containerization, infrastructure as code (IaC), and monitoring tools. This repository demonstrates best practices for deploying and managing applications using GitHub Actions, Kubernetes, Terraform, and more.

## Goal
The goal of this project is to build a scalable RESTful API around openSenseMap but customized to help beekeeper with their chores. The API output should be in JSON. You will start with a basic implementation, then extend the whole system to handle thousands of requests per second. But always remember, every decision has a cost.

## Software Project Management
This project was built in the KANBAN agile methodology with jira.
The Kanban method is an approach to evolutionary and incremental systems and process change for organizations. A work-in-progress limited pull system is the central mechanism to uncover system operation (or process) complications and encourage collaboration to continuously improve the system.
Electronic Kanban boards are also available in ALM tools like Rally (CA Agile), Jira, Swift, Kanban, LeanKit, Kanban, etc. Stages could be configured in these tools, and the movement of tickets between stages could be viewed in these tools.
![KANBAN Agile](https://github.com/user-attachments/assets/8c54eb2b-42ef-4573-8154-81d3e90e3259)


## Features
- **FastAPI Application**: The project includes a Python FastAPI application.
- **CI/CD Pipeline**: Automates testing, building, and deployment using GitHub Actions and ArgoCD.
- **Containerization**: Utilizes Docker for containerized applications.
- **Infrastructure as Code (IaC)**: Manages cloud infrastructure with Terraform.
- **Kubernetes Orchestration**: Deploys applications using Kubernetes with Helm and Kustomize.
- **Security & Code Quality**: Uses SonarQube and Terrascan for security and code analysis.
- **Monitoring & Logging**: Integrated with Grafana Cloud for observability.

## Project Structure
```
.
├── .github/                 # GitHub Actions workflows
│   ├── workflows/           # CI/CD pipeline definitions
│   ├── ISSUE_TEMPLATE/      # GitHub issue templates
├── iac/                     # Infrastructure as Code (Terraform)
│   ├── modules/             # Reusable Terraform modules
│   ├── main.tf              # Main Terraform configuration
│   ├── variables.tf         # Terraform variables
│   ├── outputs.tf           # Terraform outputs
│   ├── provider.tf          # Cloud provider configuration
├── k8s/                     # Kubernetes manifests
│   ├── deployments/         # Deployment YAML files
│   ├── services/            # Service YAML files
│   ├── configmaps/          # Configuration files for Kubernetes
│   ├── secrets/             # Secure secrets management
├── .dockerignore            # Files to ignore in Docker builds
├── .gitignore               # Files to exclude from Git
├── Dockerfile               # Docker container definition
├── main.py                  # Main FastAPI application
├── requirements.txt         # Python dependencies
├── sonar-project.properties # SonarQube configuration
├── unit_tests.py            # Unit tests
├── README.md                # Project documentation
```

## Prerequisites
Ensure you have the following installed:
- Docker
- Kubernetes (Kind or Minikube)
- Helm & Kustomize
- Terraform
- Python (3.x) & Pip
- SonarQube (optional for code quality analysis)
- Grafana Cloud (for monitoring setup)

## Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/mabdelgowa/DevOps_Hive.git
   cd DevOps_Hive
   ```
2. **Set Up Virtual Environment** (optional but recommended)
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Application Locally**
   ```sh
   python main.py
   ```

## Running with Docker
1. **Build the Docker Image**
   ```sh
   docker build -t devops_hive .
   ```
2. **Run the Container**
   ```sh
   docker run -p 8000:8000 devops_hive
   ```

## Kubernetes Deployment
1. **Apply Kubernetes Manifests**
   ```sh
   kubectl apply -f k8s/
   ```
2. **Check Running Pods**
   ```sh
   kubectl get pods
   ```

## CI/CD with GitHub Actions & ArgoCD
- The project includes a GitHub Actions pipeline for automated testing and deployment.
- ArgoCD handles continuous delivery to a Kubernetes cluster.

## Security & Code Quality
- **SonarQube**: Run static code analysis using:
  ```sh
  sonar-scanner
  ```
- **Terrascan**: Scan Terraform code for security vulnerabilities:
  ```sh
  terrascan scan
  ```

## Monitoring with Grafana Cloud
- Configure Prometheus and Grafana for logging and monitoring.


## Contributing

We welcome contributions! Feel free to open issues or submit pull requests. For larger changes, please create a new issue to discuss the change before implementing.

---

## Documentation Video
  [Documentation Video](https://drive.google.com/file/d/1uzsoCL1jlrvrW7zh33-U50LaMx_dwRDS/view?usp=drive_link)
