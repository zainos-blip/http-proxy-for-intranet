from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

def load_proxy_logs():
    try:
        with open('http_logs.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

@app.template_filter('safe_json')
def safe_json(value):
    if value is None:
        return '{}'
    try:
        return json.dumps(value, indent=2)
    except TypeError:
        return '{}'

@app.route('/')
def index():
    logs = load_proxy_logs()
    return render_template('index.html', logs=logs)

@app.route('/api/logs')
def get_logs():
    logs = load_proxy_logs()
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True, port=5000)