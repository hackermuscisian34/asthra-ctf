from flask import Flask, request, jsonify
import os
import base64
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to the Secret Vault</h1>
    <p>Can you find the hidden treasure?</p>
    <p>Hint: Sometimes the most valuable things are hidden in plain sight.</p>
    """

@app.route('/ping', methods=['POST'])
def ping():
    try:
        data = request.get_json()
        if not data or 'host' not in data:
            return jsonify({'error': 'No host provided'}), 400
        
        # Intentionally vulnerable command injection
        result = subprocess.check_output(f"ping -c 1 {data['host']}", shell=True)
        return jsonify({'result': result.decode()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decode', methods=['POST'])
def decode():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided'}), 400
        
        # Base64 decode endpoint that might reveal information
        decoded = base64.b64decode(data['message'])
        return jsonify({'decoded': decoded.decode()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)