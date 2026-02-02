pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
    }

    environment {
        PYTHON_PATH = 'C:\\Python\\python.exe'
        REPORT_NAME = 'report.html'
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat """
                %PYTHON_PATH% -m pytest --html=%REPORT_NAME% --self-contained-html
                """
            }
        }
    }

    post {

        success {
            echo '✅ Tests passed successfully'
        }

        failure {
            echo '❌ Tests failed'

            // -------- EMAIL NOTIFICATION --------
            emailext(
                subject: "❌ Jenkins Build Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    <p>Build <b>FAILED</b></p>
                    <p><b>Job:</b> ${env.JOB_NAME}</p>
                    <p><b>Build Number:</b> ${env.BUILD_NUMBER}</p>
                    <p><b>Build URL:</b> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                """,
                mimeType: 'text/html',
                to: '12014dipsnh@gmail.com'
            )

            // -------- SLACK NOTIFICATION (OPTIONAL) --------
            slackSend(
                color: 'danger',
                message: "❌ Jenkins build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER} \n${env.BUILD_URL}"
            )
        }

        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
