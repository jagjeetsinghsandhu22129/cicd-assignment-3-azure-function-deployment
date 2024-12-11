# cicd-assignment-3-azure-function-deployment

# Jenkins CI/CD Pipeline for Azure Functions (Python)

## Overview
This project demonstrates the CI/CD pipeline to build, test, and deploy an Azure Function using Jenkins.

### Directory Structure
- **HttpTrigger**: Contains the Azure Function code.
- **tests**: Includes unit test cases for the function.
- **Jenkinsfile**: Defines the Jenkins pipeline.

## Prerequisites
1. Jenkins installed and configured.
2. Azure CLI installed on the Jenkins server.
3. Python installed on the Jenkins server.
4. Azure Function App created in Azure.

## Steps to Run
1. Clone the repository.
2. Configure Jenkins with GitHub integration.
3. Add the Azure service principal credentials in Jenkins.
4. Push changes to GitHub to trigger the Jenkins pipeline.

## Test Cases
The pipeline includes the following test cases:
- Validates HTTP response status.
- Checks the response body.

## Deployment
The pipeline deploys the Azure Function to an existing Function App in Azure.
