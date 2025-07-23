pipeline {
    agent any
    stages {
        stage('Setup python') {
            steps {
            sh "python3 -m venv venv"
            sh '''
            source venv/bin/activate
            pip3 install -r requirements.txt
            '''
            }
        }
        stage('Configure') {
            steps {
            sh "config.py"
            }
        }
        stage('Test') {
            steps {
            sh "test.py"
            }
        }
    }
}
