from flask import Flask, request
import requests

app = Flask(__name__)

STORAGE_SERVICE_URL = 'http://storage:5001/store'

@app.route('/log', methods=['POST'])
def log_message():
    message = request.json.get('message')
    if message:
        response = requests.post(STORAGE_SERVICE_URL, json={'message': message})
        if response.status_code == 200:
            return {'status': 'success'}, 200
        return {'status': 'error', 'message': 'Failed to store message'}, 500
    return {'status': 'error', 'message': 'No message provided'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
