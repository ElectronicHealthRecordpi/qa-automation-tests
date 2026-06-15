pipeline {
    agent any

    parameters {
        string(name: 'BASE_URL', defaultValue: 'http://localhost:5173', description: 'URL base de la aplicación')
    }

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        stage('Install Playwright browsers') {
            steps {
                sh '''
                    . venv/bin/activate
                    playwright install chromium
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests \\
                        --html=reports/report.html \\
                        --base-url=${BASE_URL} \\
                        --browser=chromium
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/*.xml'
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'report.html',
                        reportName: 'Test Report'
                    ])
                    archiveArtifacts artifacts: 'reports/screenshots/*.png', allowEmptyArchive: true
                }
            }
        }
    }
}