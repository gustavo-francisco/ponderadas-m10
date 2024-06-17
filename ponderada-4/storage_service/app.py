from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/store', methods=['POST'])
def store_message():
    message = request.json.get('message')
    if message:
        with open('logs.txt', 'a') as f:
            f.write(f"{datetime.datetime.now()} - {message}\n")
        return {'status': 'success'}, 200
    return {'status': 'error', 'message': 'No message provided'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
