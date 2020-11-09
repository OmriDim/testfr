pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                git 'https://github.com/OmriDim/testfr.git'
            }
        }
        stage('bye') {
            steps {
                sh 'python3 func.py 3 4 '
            }
        }
    }
}

