pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Cloning the GitHub repository
                git(
                    branch: 'main',
                    url: 'https://github.com/jagjeetsinghsandhu22129/cicd-assignment-3-azure-function-deployment.git',
                    credentialsId: 'cicd'  // Replace 'cicd' with the correct GitHub credential ID
                )
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    // For Python, use bat for Windows to run the command
                    bat 'python -m pip install -r HttpTrigger/requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    // For Python tests, use bat for Windows
                    bat 'python -m unittest discover -s tests'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    // Azure CLI deployment using PowerShell commands
                    bat """
                        az login --service-principal -u %AZURE_CLIENT_ID% -p %AZURE_CLIENT_SECRET% --tenant %AZURE_TENANT_ID%
                        az functionapp deployment source config-zip ^
                        --resource-group %RESOURCE_GROUP% ^
                        --name %FUNCTION_APP_NAME% ^
                        --src-path HttpTrigger
                    """
                }
            }
        }
    }
}
