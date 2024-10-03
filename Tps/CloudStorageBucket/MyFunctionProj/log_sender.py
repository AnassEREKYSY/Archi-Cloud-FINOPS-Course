import json
import time
import random
import requests

# Cloud function endpoint
CLOUD_FUNCTION_ENDPOINT = "https://myfunctionappanass.azurewebsites.net/api/LogHttpRequest"

# Sample log messages
sample_logs = [
    {"level": "INFO", "user": "John Doe", "action": "logged in"},
    {"level": "DEBUG", "user": "Jane Smith", "action": "executed query"},
]
error_logs = [
    {"level": "ERROR", "user": "Alice Brown", "action": "failed to connect"},
    {"level": "ERROR", "user": "Bob White", "action": "permission denied"},
]

def send_log_to_cloud_function(log):
    response = requests.post(CLOUD_FUNCTION_ENDPOINT, json=log)
    if response.status_code == 200:
        print(f"Sent log: {log}")
    else:
        print(f"Failed to send log: {log}. Status code: {response.status_code}")

def simulate_log_stream():
    while True:
        log = random.choice(sample_logs if random.random() < 0.9 else error_logs)
        send_log_to_cloud_function(log)
        time.sleep(random.uniform(0.5, 3))

if __name__ == "__main__":
    simulate_log_stream()
