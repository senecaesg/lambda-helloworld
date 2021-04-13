import requests

def handler(event, context):
    print(event, context)
    resp = requests.get('https://api.ipify.org?format=json')
    print('Hello World!', resp.json())
    return 'Hello World!', resp.json()

