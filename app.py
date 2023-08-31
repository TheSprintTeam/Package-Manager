from flask import Flask, request, Response
from flask_socketio import SocketIO, join_room, leave_room
import json
import subprocess
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

PAYLOAD_FILE_PATH = 'payload.json'
clients = {}  # To store connected clients

TEST_PAYLOAD = {
            "technologies" : [
                "ansible",
                "rust",
                "python"
            ]
        }

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

@app.route('/sse/<client_id>', methods = ['GET'])
def sse(client_id):
    def event_stream():
        clients[client_id] = None  # Store the client's connection
        try:
            if clients.get(client_id) is not None:
                yield f"{json.dumps(TEST_PAYLOAD)}\n"
        finally:
            # Cleanup code when the client disconnects
            if client_id in clients:
                clients.pop(client_id)

    return Response(event_stream(), content_type='application/x-ndjson', headers={'Cache-Control': 'no-cache'})

@app.route('/close/<client_id>', methods =['POST'])
def close(client_id):
    client_connection = clients.get(client_id)
    if client_connection:
        client_connection.close()  # Close the client's connection
        clients.pop(client_id, None)
        return 'Connection closed'
    else:
        return 'Client not found', 404

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    print(f'Client joined room: {room}')

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    print(f'Client left room: {room}')

@app.route('/sendInstallEvent', methods = ["POST"])
def sendInstallEvent():
    data = request.json
    print("received event")
    room = data['room'] 
    message = data['message']
    # Process data and trigger event
    # Emit an event to the specified room
    socketio.emit('electron_event', {'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', allow_unsafe_werkzeug=True)