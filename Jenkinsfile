pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Cloning the GitHub repository with credentials
                git(
                    branch: 'main',
                    url: 'https://github.com/jagjeetsinghsandhu22129/cicd_lab_2.git',
                    credentialsId: 'cicd' // Ensure this is the ID of your Jenkins credentials for GitHub
                )
            }
        }
        stage('Build') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r HttpTrigger/requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'python -m unittest discover -s tests'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying to Azure...'
                    sh '''
                        az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID
                        az functionapp deployment source config-zip \
                        --resource-group $RESOURCE_GROUP \
                        --name $FUNCTION_APP_NAME \
                        --src-path HttpTrigger
                    '''
                }
            }
        }
    }
}
