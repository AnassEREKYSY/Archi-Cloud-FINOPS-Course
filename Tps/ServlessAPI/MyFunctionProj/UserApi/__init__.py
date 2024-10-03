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
