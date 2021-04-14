import json

import boto3

client = boto3.client('lambda', region_name='ap-southeast-1')

if __name__ == '__main__':
    # invoke doc
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda.html#Lambda.Client.invoke
    response = client.invoke(
        FunctionName='arn:aws:lambda:ap-southeast-1:609101512119:function:helloworld',
        # RequestResponse - Invoke the function synchronously
        # Event - Invoke the function asynchronously
        InvocationType='RequestResponse',
        LogType='Tail',
        Payload=json.dumps({}).encode(),
    )
    print(response)
    resp_payload = response['Payload'].read()
    print(resp_payload)

    # invoke async
    response = client.invoke(
        FunctionName='arn:aws:lambda:ap-southeast-1:609101512119:function:helloworld',
        # RequestResponse - Invoke the function synchronously
        # Event - Invoke the function asynchronously
        InvocationType='Event',
        LogType='Tail',
        Payload=json.dumps({}).encode(),
    )
    print(response)
    resp_payload = response['Payload'].read()
    print(resp_payload)

