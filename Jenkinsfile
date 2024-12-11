pipeline {
    agent any
    environment {
        AZURE_CLIENT_ID = credentials('azure-client-id')
        AZURE_CLIENT_SECRET = credentials('azure-client-secret')
        AZURE_TENANT_ID = credentials('azure-tenant-id')
        RESOURCE_GROUP = "js_resource_group"
        FUNCTION_APP_NAME = "js-cicd-assignment-3"
    }
    stages {
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
