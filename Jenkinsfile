pipeline {
	agent any
	stages {
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
