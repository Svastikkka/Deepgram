import os
import requests
import json
API_KEY = os.getenv('DEEPGRAM_API_KEY')
URL = 'https://api.deepgram.com/v1/listen'
audio_file = 'harvard/harvard.wav'
with open(audio_file, 'rb') as audio:
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

print(transcript)
with open('transcript.txt', 'w') as file:
    file.write(transcript)
