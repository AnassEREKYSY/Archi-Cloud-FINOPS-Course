import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient

# Initialize the BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string('YOUR_AZURE_STORAGE_CONNECTION_STRING')
container_name = 'logs'

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Extract data from the request
    log_data = req.get_json(silent=True)

    # Create a blob client
    blob_client = blob_service_client.get_blob_client(container=container_name, blob='logs.txt')

    # Write data to a blob in Azure Blob Storage
    blob_client.upload_blob(f"{log_data['user']} - {log_data['action']}\n", blob_type="AppendBlob", overwrite=True)

    return func.HttpResponse("Logged request!", status_code=200)
