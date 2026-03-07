# Scientific Calculator CI/CD Project

A complete DevOps pipeline for a Scientific Calculator application, featuring automated unit testing, containerization with Docker, CI/CD with Jenkins (GitSCM Polling & Webhooks), and deployment via Ansible.

## 🚀 Features
- **Scientific Calculator**: Supports basic arithmetic (+, -, *, /) and advanced functions (sqrt, factorial, natural log, power).
- **Unit Testing**: Automated test suite using Python's `unittest` framework.
- **Dockerization**: Containerized environment for consistent execution.
- **Jenkins Pipeline**:
    - **GitSCM Polling**: Automated checks for code changes every minute.
    - **Webhook Integration**: Real-time build triggers via GitHub and ngrok.
    - **Docker Hub**: Automated build, tagging, and pushing of images.
    - **Email Notifications**: Real-time status updates (Success/Failure) for developers.
- **Ansible Deployment**: Playbook to pull and run the latest image from Docker Hub.

---

## 🛠️ Technologies Used
- **Language**: Python 3.9
- **CI/CD**: Jenkins
- **Containerization**: Docker
- **Automation**: Ansible
- **Tunneling**: ngrok (for Webhooks)
- **Version Control**: Git & GitHub

---

## 📋 Prerequisites
- Python 3.x installed locally.
- Docker and Docker Compose installed.
- Jenkins server running with the following plugins:
    - Docker Pipeline
    - Email Extension
    - GitHub Integration
- Ansible installed.
- ngrok account for webhook tunneling.

---

## ⚙️ Setup Instructions

### 1. Local Development & Testing
To run the calculator and tests locally:
```bash
# Run the calculator
python3 Calculator.py

# Run unit tests
python3 -m unittest test_calculator.py
```

### 2. Docker Execution
Build and run the container manually:
```bash
docker build -t scientific-calculator .
docker run -it scientific-calculator
```

### 3. Jenkins Pipeline Configuration
1.  **ngrok & Webhook**:
    - Run `ngrok http 8080` (or your Jenkins port).
    - Copy the `https` URL provided by ngrok.
    - In GitHub Repo Settings -> Webhooks, add: `https://<your-ngrok-url>/github-webhook/`.
2.  **Credentials**:
    - Add Docker Hub credentials in Jenkins (ID: `docker-hub-credentials`).
3.  **Pipeline**:
    - Create a "Pipeline" project in Jenkins.
    - Set "Definition" to "Pipeline script from SCM".
    - Configure the Git repository and the `Jenkinsfile` path.
    - Enable "GitHub hook trigger for GITScm polling".

### 4. Ansible Deployment
To deploy the latest containerized version:
```bash
ansible-playbook deploy.yml
```

---

## 📧 Notifications
The Jenkins pipeline is configured to send email alerts to the development team. 
- **Success**: Notifies that the build passed and the image is pushed.
- **Failure**: Provides the build number and URL for rapid debugging.

## 🤝 Contributing
1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.
