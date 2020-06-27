import boto3
import json

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='muralia-fargateScaling')
queue.purge() # Start with an empty queue

for msg_id in range(1500):
    data = {"id": msg_id}
    queue.send_message(MessageBody=json.dumps(data))
