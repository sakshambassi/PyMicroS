from flask import Flask, request, jsonify
from service.bigram_service import bigram_service
from service.word_count_service import word_count_service

import logging

logging.getLogger().setLevel(logging.INFO)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def home():
    return "Welcome!"

@app.route('/analyze-text', methods=['POST'])
def analyze_text():
    data = request.get_json()
    service = data.get('service')
    text = data.get('text')
    if not service:
        return jsonify({'error': 'No service specified'}), 400

    if not text:
        return jsonify({'error': 'No text specified'}), 400

    if service == 'bigram':
        result = bigram_service(text)
    elif service == 'word-count':
        result = word_count_service(text)
    else:
        return jsonify({'error': 'Invalid service specified'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)