pipeline {
    agent any

    environment {
        BASE_URL = credentials('BASE_URL')
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
                    playwright install --with-deps chromium
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest tests \\
                        --html=reports/report.html --self-contained-html \\
                        --base-url=${BASE_URL} \\
                        --headed=false \\
                        --browser=chromium
                '''
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'reports/*.xml'
                }
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test Report'
            ])
            archiveArtifacts artifacts: 'reports/screenshots/*.png'
        }
    }
}