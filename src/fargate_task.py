import boto3
import os
import time
import json

RETRIES = 3 # Use an environment variable in Production

SQS_CLIENT = boto3.client('sqs')
QUEUE_URL = os.getenv('QUEUE_URL')

while RETRIES >= 0:
    sqs_messages = SQS_CLIENT.receive_message(
        QueueUrl=QUEUE_URL,
        MaxNumberOfMessages=10, # MAX allowed by SQS
        WaitTimeSeconds=20, 
        VisibilityTimeout=60) # 1 minutes
    if 'Messages' in sqs_messages:
        RETRIES = 3 # Reset retries
        messages = sqs_messages['Messages']
        for message in messages:
            print("SQS Message: {}".format(message['Body']))
            time.sleep(3) # Sleep to simulate some processing
            # Delete SQS message after processing it
            SQS_CLIENT.delete_message(
                QueueUrl=QUEUE_URL,
                ReceiptHandle=message['ReceiptHandle'])
    else:
        if RETRIES <= 0:
            print('Shutting down container.')
            break
        RETRIES = RETRIES - 1
        print('SQS Queue is empty. Retrying.')