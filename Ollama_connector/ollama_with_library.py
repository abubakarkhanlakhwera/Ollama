from ollama import Client

client = Client()
prompt = input('Enter a prompt: ')
response = client.generate(
    model='llama3.1',
    prompt=f'You are a PHD professor in python programming and you have a great experience coding. {prompt}',
    stream=True
)

for part in response:
    print(part.response, end='')