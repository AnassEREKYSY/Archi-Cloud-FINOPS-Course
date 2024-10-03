## Tps


## Setting Up Azure Functions
1. login to Azure : 
    ```bash
    az login

2. Create a ressource group :
    ```bash
    az group create --name MyResourceGroup --location eastus

3. Create an Azure Function App :
    ```bash
    az functionapp create \
    --resource-group MyResourceGroup \
    --consumption-plan-location eastus \
    --runtime python \
    --runtime-version 3.10 \
    --functions-version 4 \
    --name MyFunctionAppAnass \
    --storage-account mystorageaccountanass \
    --os-type Linux

## Creating the Azure Function : 

1. Initialize a New Function Project:
    ```bash
    func init MyFunctionProj --python

2. Navigate to the Project Directory:
    ```bash
    cd MyFunctionProj

3. Create a New Function:
    ```bash
    func new --name LogHttpRequest --template "HTTP trigger" --authlevel "anonymous"

4. Modify the Function Code
    Open __init__.py in the LogHttpRequest directory and modify it to log HTTP requests:
    ```python
    import logging
    import azure.functions as func
    from google.cloud import storage

    def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    # Extract data from the request
    log_data = f"{req.headers['X-Forwarded-For']} - {req.method} - {req.url}\n"
    
    # Store log in Azure Blob Storage
    client = storage.Client()
    bucket = client.get_bucket('YOUR_BUCKET_NAME')
    blob = bucket.blob('logs.txt')
    blob.upload_from_string(log_data, content_type='text/plain')
    
    return func.HttpResponse("Logged request!", status_code=200)

## Deploying the Azure Function :

1. Deploy the Azure Function: From the MyFunctionProj directory, run :
    ```bash
    func azure functionapp publish MyFunctionAppAnass

2. Note the Function URL: After deployment, you will receive the URL for your function. Copy this URL for testing.

## Setting Up Azure Storage for Logging :

1. Create an Azure Storage Account: If you haven’t already created a storage account, run:
    ```bash
    az storage account create --name mystorageaccountanass --resource-group MyResourceGroup --location eastus --sku Standard_LRS

2. Create a Blob Container:
    ```bash
    az storage container create --name logs --account-name mystorageaccountanass

## Creating the Log Sender : 

1. Create a new Python script (e.g., log_sender.py) with the following code:
    ```python
    import json
    import time
    import random
    import requests

    # Cloud function endpoint
    CLOUD_FUNCTION_ENDPOINT = "YOUR_FUNCTION_URL"

    def send_log_to_cloud_function(log):
        response = requests.post(CLOUD_FUNCTION_ENDPOINT, json=log)
        if response.status_code == 200:
            print(f"Sent log: {log}")
        else:
            print(f"Failed to send log: {log}. Status code: {response.status_code}")

    def simulate_log_stream():
        sample_logs = [
            {"level": "INFO", "message": "User logged in", "user_id": 1},
            {"level": "DEBUG", "message": "Query executed", "user_id": 3},
        ]
        error_logs = [
            {"level": "ERROR", "message": "Failed to connect to database", "user_id": 2},
            {"level": "ERROR", "message": "Permission denied", "user_id": 4},
        ]
        while True:
            if random.random() < 0.1:
                log = random.choice(error_logs)
            else:
                log = random.choice(sample_logs)
            send_log_to_cloud_function(log)
            time.sleep(random.uniform(0.5, 3))

    if __name__ == "__main__":
        simulate_log_stream()

## Running the Log Sender :

1. Run the Log Sender Script: 
    ```bash
    python log_sender.py

2. Verify Logs in Azure Storage: Check your Azure Blob Storage to see if the logs are being stored correctly.


## Serverless API with Azure Functions and Cosmos DB

1. run this commande : 
    ```bash
    pip install azure-functions azure-cosmos

2. Open the _init_.py file to edit it : 
    ```python
    import json
    import azure.functions as func
    from azure.cosmos import CosmosClient, PartitionKey

    # Initialize Cosmos client
    endpoint = "YOUR_COSMOS_DB_ENDPOINT"
    key = "YOUR_COSMOS_DB_KEY"
    client = CosmosClient(endpoint, key)
    database_name = "UserData"
    container_name = "users"
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    def main(req: func.HttpRequest) -> func.HttpResponse:
        logging.info('Processing a request.')

        if req.method == "GET":
            # Retrieve all users
            users = list(container.read_all_items())
            return func.HttpResponse(json.dumps(users), status_code=200)

        elif req.method == "POST":
            # Create a new user
            user_data = req.get_json()
            container.create_item(user_data)
            return func.HttpResponse("User created.", status_code=201)

        elif req.method == "PUT":
            # Update a user
            user_data = req.get_json()
            container.upsert_item(user_data)
            return func.HttpResponse("User updated.", status_code=200)

        elif req.method == "DELETE":
            # Delete a user
            user_id = req.params.get('id')
            container.delete_item(item=user_id, partition_key=user_id)
            return func.HttpResponse("User deleted.", status_code=204)

        else:
            return func.HttpResponse("Unsupported method", status_code=405)

3. Edit requirements.txt to include the necessary libraries:
    ```bash
    azure-functions
    azure-cosmos

4. Deploy the Azure Function: From the MyFunctionProj directory, run: 
    ```bash 
    func azure functionapp publish MyFunctionAppAnass

5. Test the API : 
    ```bash 
    curl -X POST "https://myfunctionappanass.azurewebsites.net/api/userapi" -H "Content-Type: application/json" -d "{\"id\": \"1\", \"name\": \"John Doe\"}"

    curl -X GET https://myfunctionappanass.azurewebsites.net/api/userapi

    curl -X DELETE https://myfunctionappanass.azurewebsites.net/api/userapi?id=1

## Install Azure Functions Tools on Linux OS :

1. Create a Linux VM
2. SSH into the Linux VM :
    ```bash 
    ssh <username>@<ip_address>   // ssh azureuser@4.178.137.34
3. Install Azure Functions Core Tools
    ```bash 
    # Update and upgrade the system
    sudo apt-get update -y
    sudo apt-get upgrade -y

    # Install Microsoft packages
    wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
    sudo dpkg -i packages-microsoft-prod.deb
    sudo apt-get update

    # Install required packages
    sudo apt-get install apt-transport-https -y
    sudo apt-get install dotnet-sdk-2.1 -y
    sudo apt-get install azure-functions-core-tools -y

4. Test Azure Functions Core Tools Installation
    ```bash 
    func --version
5. Create the Azure Functions Project :
    ```bash 
    func init MyFunctionProj --dotnet
6. Create the Azure Function :
    ```bash 
    cd MyFunctionProj
    func new
7. Run the Function App :
    ```bash 
    func start
8.  Invoke the Function :
    ```bash 
    curl -X POST "http://localhost:7071/api/UserApi" -H "Content-Type: application/json" -d '{"id": "1", "name": "John Doe"}'








