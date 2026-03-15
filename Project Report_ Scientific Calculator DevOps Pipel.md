<div align="center">
  <br><br><br><br>
  <h1>Scientific Calculator DevOps Pipeline</h1>
  <br>
  <p style="font-size: 1.2em;">
    <b>Abstract:</b> This project demonstrates a complete end-to-end CI/CD lifecycle for a Python-based scientific calculator. 
    By integrating Jenkins for orchestration, Docker for containerization, and Ansible for automated deployment, 
    the pipeline ensures that every code change is rigorously tested and seamlessly delivered to a production-ready environment.
  </p>
</div>

<br><br><br><br><br><br><br><br><br><br>

<div align="right">
  <h3>Project By:</h3>
  <b>Name:</b> [Your Name]<br>
  <b>Roll Number:</b> [Your Roll Number]
</div>

<div style="page-break-after: always;"></div>

---

## Table of Contents
1. [Introduction to DevOps](#1-basic-ideas-the-what-and-why-of-devops)
2. [Tech Stack & Tools](#2-tools-used-in-this-project)
3. [Phase 1: Source Control (Git)](#phase-1-source-control-with-git)
4. [Phase 2: CI Orchestration (Jenkins)](#phase-2-jenkins-orchestration)
5. [Phase 3: Pipeline as Code (Jenkinsfile)](#phase-3-jenkinsfile-configuration)
6. [Phase 4: Containerization (Docker)](#phase-4-containerization-with-docker)
7. [Phase 5: Automated Deployment (Ansible)](#phase-5-deployment-with-ansible)
8. [Conclusion & Future Scope](#conclusion--future-scope)

---

## 1. Basic Ideas: The What and Why of DevOps

**What is DevOps?**  
DevOps is a set of practices that combines software development (**Dev**) and IT operations (**Ops**). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality.

**Why DevOps?**  
* **Speed:** Deliver features and fixes faster.  
* **Reliability:** Ensure the quality of application updates and infrastructure changes via automated testing.  
* **Scalability:** Manage infrastructure and development processes at scale.  
* **Collaboration:** Build more effective teams under a model that emphasizes ownership and accountability.

---

## 2. Tools Used in This Project

| Category | Tool | Purpose |  
| :--- | :--- | :--- |  
| **Source Control** | **Git / GitHub** | Versioning code and hosting the remote repository. |  
| **CI/CD Orchestration** | **Jenkins** | Automating the build, test, and deployment stages. |  
| **Containerization** | **Docker** | Packaging the application into a portable, lightweight image. |  
| **Artifact Repository** | **Docker Hub** | Securely storing and sharing built Docker images. |  
| **Config Management** | **Ansible** | Automating the deployment and container management on the host. |  
| **Programming Language**| **Python** | Logic for the scientific calculator and unit testing. |

---

## 3. Step-by-Step Instructions to Reproduce

### Phase 1: Source Control with Git  
**What is Git?** Git is a distributed version control system that tracks changes in source code during software development.

**Key Commands Used:**  
1. `git init`: Initializes the local repository.
2. `git add .`: Stages changes for commit.
3. `git commit -m "..."`: Saves the snapshot of the project.
4. `git push -u origin main`: Uploads local changes to the GitHub remote.

> **[SPACE FOR SCREENSHOT: Terminal showing Git init and initial commit]**  
>  
>  
>  
> **[SPACE FOR SCREENSHOT: Git push success in terminal showing remote upload]**  
>  
>

---

### Phase 2: Jenkins Orchestration  
**Intro:** Jenkins serves as the "brain" of the operation, triggering builds automatically upon every code change.

**Setup & Configuration:**  
1. **Expose Jenkins with ngrok:** Run `ngrok http 8080` to get a public URL for your local Jenkins.  
   ![a73dc0b45abbbfe8c602493bbab3ed76.png](../_resources/a73dc0b45abbbfe8c602493bbab3ed76.png)

2. **GitHub Webhook:** In GitHub Settings > Webhooks, add your ngrok URL followed by `/github-webhook/`.  
   ![4d59cc355f9538e59b99daf6ce0b8b73.png](../_resources/4d59cc355f9538e59b99daf6ce0b8b73.png)
  
3. **Docker Hub Credentials:** Credentials are stored securely using Jenkins' Secret Manager with the ID `DockerHubCred`.  
   ![36f80f37a309fdcd3ef07c73f0746743.png](../_resources/36f80f37a309fdcd3ef07c73f0746743.png)
  
4. **Mail Notification:** Configured via SMTP to notify the developer of the build status.  
   ![a25266c1487778dc565a4eeda1579aab.png](../_resources/a25266c1487778dc565a4eeda1579aab.png)  

---

### Phase 3: Jenkinsfile Configuration  
The `Jenkinsfile` implements a declarative pipeline, ensuring the build process is repeatable and version-controlled.

```groovy
pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = 'kartikeyblaze'
        IMAGE_NAME = 'scientific-calculator'
        IMAGE_TAG = "${env.BUILD_ID}"
        DOCKER_CREDENTIALS_ID = 'DockerHubCred'
        EMAIL = 'kartikeyblaze@gmail.com'
    }
    // ... stages for Checkout, Unit Testing, Build, Push, and Deploy
}
```

**Pipeline Logic:**  
* **Unit Testing:** Runs `python3 -m unittest` to ensure mathematical functions (add, sqrt, ln, etc.) work as expected.
* **Security:** Uses `withCredentials` to mask sensitive Docker Hub passwords in the logs.
* **Ansible Integration:** The `ansiblePlaybook` step bridges the gap between CI (building) and CD (deploying).

> **[SPACE FOR SCREENSHOT: Jenkins Dashboard showing the Pipeline Job execution]**  
>  ![1090ef77ab8edae58e89999c398d492b.png](../_resources/1090ef77ab8edae58e89999c398d492b.png)
>  ![0237410c4bd85112a3d8f5443eaf54c6.png](../_resources/0237410c4bd85112a3d8f5443eaf54c6.png)

---

### Phase 4: Containerization with Docker  
**Intro:** Docker ensures that the calculator app runs consistently regardless of the underlying OS, eliminating "it works on my machine" issues.

**Dockerfile Breakdown:**  
* `FROM python:3.9-slim`: Provides a minimal, secure Python environment.
* `WORKDIR /app`: Organizes the application files.
* `CMD ["python", "Calculator.py"]`: Defines the entry point for the application.

> **[SPACE FOR SCREENSHOT: Terminal showing Docker Build and Image Creation]**  
>  ![3869fea25d49c9c05b7ba72416c49747.png](../_resources/3869fea25d49c9c05b7ba72416c49747.png)
>  ![1c32920d1544676481eaf8d5496a1e41.png](../_resources/1c32920d1544676481eaf8d5496a1e41.png)

---

### Phase 5: Deployment with Ansible  
**Intro:** Ansible provides "Infrastructure as Code" by automating the final deployment steps, reducing manual error.

**Playbook Features:**  
* **Idempotency:** The playbook checks if the `calculator` container already exists and removes it before starting a fresh one.
* **Local Connection:** Uses `connection: local` to deploy directly to the host without requiring complex SSH setups.

> **[SPACE FOR SCREENSHOT: Terminal showing successful Ansible Playbook execution]**  
>  ![4c94221f659b28b642a3fabce46214c9.png](../_resources/4c94221f659b28b642a3fabce46214c9.png)
>  
> **[SPACE FOR SCREENSHOT: Terminal showing 'docker ps' with the active container]**  
>  ![0876768eca0e7ebd8beaba50b4007a86.png](../_resources/0876768eca0e7ebd8beaba50b4007a86.png)

---

## EMAIL NOTIFICATIONS
![9bdf0e28f27b43ed5907ab4b9d1c8926.png](../_resources/9bdf0e28f27b43ed5907ab4b9d1c8926.png)
![d27361801a62e0b2c41f39decaacaf02.png](../_resources/d27361801a62e0b2c41f39decaacaf02.png)

---

## Conclusion & Future Scope
This project successfully implemented a standard DevOps lifecycle. The automated pipeline reduces human intervention, minimizes deployment errors, and ensures that only code passing all unit tests reaches production.

**Future Enhancements:**
* **Kubernetes Integration:** Scaling the container using K8s for high availability.
* **Monitoring:** Adding Prometheus and Grafana to track application performance.
* **Static Analysis:** Integrating tools like SonarQube for code security scanning.
