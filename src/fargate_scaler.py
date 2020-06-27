import boto3
import json
import os

FARGATE_CLUSTER_ARN = os.getenv('FARGATE_CLUSTER_ARN')
FARGATE_TASK_DEFINITION = os.getenv('FARGATE_TASK_DEFINITION')
FARGATE_PLATFORM_VERSION = os.getenv('FARGATE_PLATFORM_VERSION')
FARGATE_SUBNETS = os.getenv('FARGATE_SUBNETS')
FARGATE_SECURITYGROUP = os.getenv('FARGATE_SECURITYGROUP')

client = boto3.client('ecs', region_name='us-east-1')

# Map SQS queue threshold to the number of additional tasks to run
desired_task_count_map = {
  "1": 1,
  "100": 1,
  "250": 1,
  "500": 2,
  "1000": 5,
}

def run_fargate_task(count):
    print("INFO: In run task. count: {}".format(count))
    subnets = FARGATE_SUBNETS.split(',')
    response = client.run_task(
        cluster=FARGATE_CLUSTER_ARN,
        launchType = 'FARGATE',
        taskDefinition=FARGATE_TASK_DEFINITION,
        count=count,
        platformVersion=FARGATE_PLATFORM_VERSION,
        networkConfiguration={
            'awsvpcConfiguration': {
                'assignPublicIp': 'ENABLED',
                'subnets': subnets,
                'securityGroups': [FARGATE_SECURITYGROUP]
            }
        },
    )

def get_task_count():
    response = client.list_tasks(cluster=FARGATE_CLUSTER_ARN)
    return len(response['taskArns'])

def handle_alarm(event, context):
    sns_message = json.loads(event['Records'][0]['Sns']['Message'])
    alarm_name = sns_message['AlarmName']
    sqs_threshold = alarm_name.split("#")[1]
    print("INFO: Alarm received: {}. Threshold: {}".format(alarm_name, sqs_threshold))
    run_fargate_task(desired_task_count_map[sqs_threshold])
