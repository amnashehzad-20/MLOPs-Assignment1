pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "amnashehzad25678/mlops-app"
        DOCKER_CREDENTIALS_ID = "docker-hub-credentials"
        ADMIN_EMAIL = "shehzad.amna270@gmail.com"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'master', url: 'https://github.com/amnashehzad-20/MLOPs-Assignment1.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:latest ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry([credentialsId: DOCKER_CREDENTIALS_ID, url: '']) {
                        bat "docker push ${DOCKER_IMAGE}:latest"
                    }
                }
            }
        }

    
    }

    post {
        success {
            mail to: "${ADMIN_EMAIL}",
                 subject: "Deployment Successful",
                 body: "The application has been successfully deployed via Jenkins."
        }
        failure {
            mail to: "${ADMIN_EMAIL}",
                 subject: "Deployment Failed",
                 body: "The deployment via Jenkins has failed. Please check the logs."
        }
    }
}