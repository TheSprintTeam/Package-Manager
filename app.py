from flask import Flask, request
import subprocess
import os
import json

PAYLOAD_FILE_PATH = 'payload.json'

app = Flask(__name__)

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

    return 'Payload received and saved.'

if __name__ == '__main__':
        app.run(host='0.0.0.0')