import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
import os
import json
from datetime import datetime

# Initialize the BlobServiceClient
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')  # Set your connection string in local.settings.json
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Received an HTTP request.')

    # Get request details
    request_body = req.get_json()
    log_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'data': request_body
    }

    # Store the log entry in a blob
    try:
        container_name = 'logs'
        blob_name = f"log_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.json"
        
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        blob_client.upload_blob(json.dumps(log_entry), overwrite=True)

        return func.HttpResponse("Log entry stored successfully.", status_code=200)
    except Exception as e:
        logging.error(f"Error storing log: {str(e)}")
        return func.HttpResponse("Error storing log.", status_code=500)
