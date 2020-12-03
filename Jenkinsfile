pipeline {

    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building..'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }

        stage('Deploy to staging') {
            when {
                branch 'staging'
            }
            steps {
                # ADD STEPS HERE
            }
        }

        stage('Deploy to production') {
            when {
                branch 'master'
            }
            steps {
                # ADD STEPS HERE
            }
        }
    }
}