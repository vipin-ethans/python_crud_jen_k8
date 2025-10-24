pipeline {
  agent any

  environment {
    IMAGE_NAME = "vipinde/devops-python"
    KUBE_DEPLOY_PATH = "k8s"
  }

  stage('Clean Workspace') {
  steps {
    deleteDir() // Jenkins workspace clean karega
  }
}

  stages {
    stage('Clone Repo') {
      steps {
        sh 'git clone https://github.com/vipin-ethans/python_crud_jen_k8.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $IMAGE_NAME:latest .'
      }
    }

    stage('Push Image') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
          sh 'docker push $IMAGE_NAME:latest'
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        sh 'kubectl apply -f $KUBE_DEPLOY_PATH/deployment.yaml'
        sh 'kubectl apply -f $KUBE_DEPLOY_PATH/service.yaml'
      }
    }

    stage('Verify Deployment') {
      steps {
        sh 'kubectl rollout status deployment/devops-python'
      }
    }
  }

  post {
    success {
      echo '✅ Kubernetes deployment successful!'
    }
    failure {
      echo '❌ Deployment failed!'
    }
  }
}

