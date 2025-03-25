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
This project was built in the KANBAN agile methodology with jira.
The Kanban method is an approach to evolutionary and incremental systems and process change for organizations. A work-in-progress limited pull system is the central mechanism to uncover system operation (or process) complications and encourage collaboration to continuously improve the system.
Electronic Kanban boards are also available in ALM tools like Rally (CA Agile), Jira, Swift, Kanban, LeanKit, Kanban, etc. Stages could be configured in these tools, and the movement of tickets between stages could be viewed in these tools.
![KANBAN Agile](https://github.com/user-attachments/assets/8c54eb2b-42ef-4573-8154-81d3e90e3259)


### Tech Stack
- **Python**: FastAPI for the API.
- **Docker**: Containerization for deployment (optional for running locally).
- **GitHub Actions**: CI/CD for automated builds, tests, and deployment.
- **ArgoCD**: GitOps continuous delivery.
- **Terraform**: Infrastructure as Code (IaC) for cloud resource provisioning (AWS).
  
### Key Features
- Scalable API that interacts with openSenseMap data.
- Integration of Docker and Kubernetes for deployment.
- CI/CD pipeline via GitHub Actions.
- Infrastructure automation using Terraform for AWS EKS clusters.

---

## Project Structure

```
├── Dockerfile
├── main.py
├── requirements.txt
├── terraform
│   ├── eks-cluster.tf
│   └── vpc.tf
├── .github
│   └── workflows
├── k8s
├── test
├── sonar-project.properties
└── README.md
```

---

## Setup & Installation

### 1. Clone the repository
To get started, clone the repository to your local machine:

```bash
git clone https://github.com/mabdelgowa/DevOps_Hive.git
cd DevOps_Hive
```

### 2. Set up a virtual environment (optional but recommended)
Create and activate a virtual environment to keep your dependencies isolated:

```bash
# For Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# For Windows:
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install dependencies
Install the required Python dependencies using `pip`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file includes FastAPI, Uvicorn, and other necessary packages for the project.

### 4. Run the FastAPI app locally
To start the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

- This will start the FastAPI application on `http://localhost:8000`.
- You can access the API docs at `http://localhost:8000/docs`.

### 5. Access the API
Once the app is running, you can interact with the API by visiting the following endpoints:

- **Main API endpoint**: `http://localhost:8000/`
- **Swagger UI for API documentation**: `http://localhost:8000/docs`
- **ReDoc UI for API documentation**: `http://localhost:8000/redoc`

---

## Usage

Once the FastAPI server is running locally, you can use the available endpoints to interact with the system. For example, you can make GET or POST requests to the API for data from openSenseMap.

---

## Contributing

We welcome contributions! Feel free to open issues or submit pull requests. For larger changes, please create a new issue to discuss the change before implementing.

---

## Documentation Video
  [Documentation Video](https://drive.google.com/file/d/1uzsoCL1jlrvrW7zh33-U50LaMx_dwRDS/view?usp=drive_link)
