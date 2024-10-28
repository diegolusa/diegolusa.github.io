
#  I need a SQS consumer

import boto3
from time import sleep

session = boto3.Session(profile_name='141684974138_AdministratorAccess', region_name='us-east-1')
sqs = session.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='sqs-demo-queue')

while 1:
    for message in queue.receive_messages(MaxNumberOfMessages=2,AttributeNames=['All'],MessageAttributeNames=['age']):
        print(message.body)
        print(message.message_attributes)
        message.delete()
    sleep(10)
        
