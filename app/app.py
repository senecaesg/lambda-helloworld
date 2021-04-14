import json

import requests

def handler(event, context):
    print(event, context)
    resp = requests.get('https://api.ipify.org?format=json')
    print('Hello World!', resp.json())
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hello World: {resp.json()["ip"]}', 'input': event})
    }
    return response

