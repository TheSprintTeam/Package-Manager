from flask import Flask, request, Response
import json
import subprocess
import os

app = Flask(__name__)

PAYLOAD_FILE_PATH = 'payload.json'
clients = {}  # To store connected clients

@app.route('/', methods=['POST'])
def index():
    # Get the JSON payload from the request
    payload = request.json
    # Check if the file exists
    if os.path.exists(PAYLOAD_FILE_PATH):
        # Clear the contents of the file
        with open(PAYLOAD_FILE_PATH, 'w') as f:
            f.truncate(0)

    # Write the payload to the file
    with open(PAYLOAD_FILE_PATH, 'w') as f:
        json.dump(payload, f)
    
    subprocess.run(["python","inventoryFetcher.py"])

    return 'install finished'

@app.route('/sse/<client_id>')
def sse(data):
    def event_stream():
        client_id  = data["id"] 

        clients[client_id] = None  # Store the client's connection
        try:
            if clients.get(client_id) is not None:
                yield f"{json.dumps(data)}\n"
        finally:
            # Cleanup code when the client disconnects
            if client_id in clients:
                clients.pop(client_id)

    return Response(event_stream(), content_type='application/x-ndjson', headers={'Cache-Control': 'no-cache'})

@app.route('/close/<client_id>')
def close(client_id):
    client_connection = clients.get(client_id)
    if client_connection:
        client_connection.close()  # Close the client's connection
        clients.pop(client_id, None)
        return 'Connection closed'
    else:
        return 'Client not found', 404