from flask import Flask, request, jsonify, render_template_string
import os
import requests

app = Flask(__name__)

API_KEY = os.getenv('DEEPGRAM_API_KEY')
URL = 'https://api.deepgram.com/v1/listen'

@app.route('/')
def upload_form():
    return render_template_string('''
        <!doctype html>
        <title>Upload Audio File</title>
        <h1>Upload Audio File for Transcription</h1>
        <form method="post" action="/transcribe" enctype="multipart/form-data">
            <input type="file" name="file" accept="audio/*">
            <input type="submit" value="Upload">
        </form>
    ''')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    audio = file.read()
    
    response = requests.post(
        URL,
        headers={
            'Authorization': f'Token {API_KEY}',
            'Content-Type': 'audio/wav'
        },
        data=audio
    )

    response_json = response.json()
    transcript = response_json.get('results', {}).get('channels', [{}])[0].get('alternatives', [{}])[0].get('transcript', '')

    return jsonify({'transcript': transcript})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=30080)
