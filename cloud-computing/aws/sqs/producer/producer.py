

# I need a SQS producer to send messages to SQS queue.

import boto3

session = boto3.Session(profile_name='141684974138_AdministratorAccess')
sqs = session.resource('sqs',region_name='us-east-1')

queue = sqs.get_queue_by_name(QueueName='sqs-demo-queue')

message = {
    'code':"CD001",
    'message':"Hello World"
}

#https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-java-send-message-with-attributes.html
response = queue.send_message(MessageBody=str(message),MessageAttributes={
    'age':{ 
        'DataType':'Number',       
        'StringValue':'30'
    }
})

print(response.get('MessageId'))