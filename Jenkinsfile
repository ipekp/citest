pipeline {
    agent any
    stages {
        stage('Setup python') {
            steps {
                script {
                    sh "python3 -m venv venv"
                    sh '''
                    . venv/bin/activate
                    pip3 install -r requirements.txt
                    '''
                }
            }
        }
        stage('Configure') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python3 config.py
                    '''
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh '''
                    . venv/bin/activate
                    python3 test.py
                    '''
                }
            }
        }

    }
}
