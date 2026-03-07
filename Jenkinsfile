pipeline {
    agent any

    environment {
        DOCKER_HUB_USER = 'kartikeyblaze'
        IMAGE_NAME = 'scientific-calculator'
        IMAGE_TAG = "${env.BUILD_ID}"
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        EMAIL = 'kartikeyblaze@gmail.com'
    }

    triggers { 
      githubPush() 
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Testing') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_CREDENTIALS_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin'
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:${IMAGE_TAG}"
                        sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Run Ansible Playbook') {
            steps {
                ansiblePlaybook(
                    playbook: 'deploy.yml',
                    inventory: 'inventory'
                )
            }
        }
    }

    post {
        always {
            script {
                def status = currentBuild.result ?: 'SUCCESS'
                mail to: EMAIL,
                     subject: "Build ${status}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                     body: "Build ${status} for ${env.JOB_NAME} #${env.BUILD_NUMBER}.\nView more: ${env.BUILD_URL}"
            }
        }
    }
}
