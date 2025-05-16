from flask import Flask, request, render_template, jsonify
import subprocess
import re

app = Flask(__name__)

ALLOWED_SCAN_TYPES = {
    "-A",
    "-sS",
    "-F",
    "-O",
    "-Pn",
    "--top-ports 10"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()
    target = data.get('target')
    scan_type = data.get('scanType', '-A')

    if not target or not re.match(r'^[a-zA-Z0-9\.\-]+$', target):
        return jsonify({'error': 'Invalid target'}), 400

    if scan_type not in ALLOWED_SCAN_TYPES:
        return jsonify({'error': 'Invalid scanType'}), 400

    scan_args = scan_type.split()

    try:
        result = subprocess.check_output(
            ['nmap'] + scan_args + [target],
            stderr=subprocess.STDOUT,
            text=True
        )
        return jsonify({'output': result})
    except subprocess.CalledProcessError as e:
        return jsonify({'error': e.output}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
