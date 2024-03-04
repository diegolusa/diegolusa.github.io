#I need a code to write dynamodb items to a table

import boto3
import json
from decimal import Decimal

session = boto3.Session(profile_name='141684974138_AdministratorAccess', region_name='us-east-1')
dynamodb = session.resource('dynamodb')

table = dynamodb.Table('users')

# https://youtu.be/yNOVamgIXGQ


def add_new(key='diego.lusa@compasso.com.br'):
    table.put_item(
        Item={
            'user_id':key,
            'FirstName': 'Diego',
            'LastName': 'Lusa',
            'age': 34,
        }
    )

def update_rec(key='diego.lusa@compasso.com.br'):
    #se o atributo do set não existir, será criado
    table.update_item(
        Key={
            "user_id": 'diego.lusa@compasso.com.br'
        },
        UpdateExpression='SET NewFirstName = :new_name REMOVE FirstName',
        
        ExpressionAttributeValues={
            ":new_name": "DIEGO123"
            
        }
    )

def get_rec(key='diego.lusa@compasso.com.br'):
    response = table.get_item(
        Key={
            'user_id': key
        }
    )
    print(response['Item'])

get_rec()