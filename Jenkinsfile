pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ibrahimaltun/ml-pipeline-w-CI.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Data Preparation') {
            steps {
                sh './venv/bin/python scripts/data_prep.py'
            }
        }

        stage('Model Training') {
            steps {
                sh './venv/bin/python scripts/train.py'
            }
        }

        stage('Evaluation') {
            steps {
                sh './venv/bin/python scripts/evaluate.py'
            }
        }

        stage('Deploy') {
             steps {
                 sh './venv/bin/python scripts/deploy.py'
             }
         }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/results/*', fingerprint: true
        }
    }
}
