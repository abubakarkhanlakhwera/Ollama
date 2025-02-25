import requests as req
import json


url = 'http://localhost:11434/api/chat'

prompt = input('Enter a prompt: ')
payload = {
    'model': 'llama3.1',
    'messages': [{ 'role': 'user', 'content': f'You are a PHD professor in python programming and you have a great experience coding.{prompt}' }]
}

response = req.post(url, json=payload,stream=True)
lines = response.iter_lines(decode_unicode=True)

if response.status_code == 200:
    print('Streaming Response From Ollama')
    for line in lines:
        if line:
            try:
                json_data = json.loads(line)
                if 'message' in json_data and 'content' in json_data['message']:
                    print(json_data['message']['content'],end='')
            except json.JSONDecodeError:
                print('Error decoding JSON')
    print()
else:
    print('Error:', response.status_code)       