import socket
from flask import Flask, jsonify
import os
app = Flask(__name__)

SERVICE_MODE = os.getenv('SERVICE_MODE', 'app')

@app.route('/')
def home():
    env = os.getenv('APP_DEBUG')
    sock=socket.gethostname()

    return jsonify({
        'message': 'Welcome to the Home Page!',
        'service_mode': SERVICE_MODE,
        'environment': env,
        'hello from' : sock
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy'
    }), 200
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
