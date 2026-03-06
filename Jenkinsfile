pipeline {
    agent any

    stages {
        stage('Checkout') { // verilen git reposundan kod çekilir
            steps {
                git 'https://github.com/ibrahimaltun/ml-pipeline-w-CI.git'
            }
        }

        stage('Install Dependencies') { // ortam hazırlanır, bağımlılıklar yüklenir
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Data Preparation') { // kod yürütülür, veri hazırlama
            steps {
                sh './venv/bin/python scripts/data_prep.py'
            }
        }

        stage('Model Training') { // kod yüürtme, model eğitimi
            steps {
                sh './venv/bin/python scripts/train.py'
            }
        }

        stage('Evaluation') { // kod yürütme, sonuçları değerlendirme
            steps {
                sh './venv/bin/python scripts/evaluate.py'
            }
        }

        stage('Deploy') { // model dosyasını bir servise deploy etme
            steps {
                sh './venv/bin/python scripts/deploy.py'
            }
        }
    }

    post {
        always { // çıktıların saklanacağı dizin
            archiveArtifacts artifacts: '**/results/*', fingerprint: true
        }
    }
}
