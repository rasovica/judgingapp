import string
import json
import boto3

from Crypto.Random import random

pictures = boto3.resource('dynamodb', region_name='us-east-1').Table('postsTable')


def get_post_id():
    # :TODO Check if exists
    allowed_chars = string.ascii_letters+string.digits

    return ''.join([random.choice(allowed_chars) for _ in range(8)])


def new_post(data, user):
    post = dict()

    post_id = get_post_id()

    post['post_id'] = post_id
    post['owner_id'] = user

    if 'title' in data:
        post['title'] = data['title']

    pictures.put_item(Item=post)

    return {
        'statusCode': 200,
        'body': {
            'success': True,
            'data': {
                'post_id': post_id
            }
        }
    }


def process_response(response, exception=None):
    if not response or not isinstance(response, dict) or 'statusCode' not in response or 'body' not in response or exception:
        response = dict()
        response['statusCode'] = 500
        if not exception:
            response['body'] = {
                'success': False,
                'error': 'Internal server error'
            }
        if isinstance(exception, json.JSONDecodeError):
            response['body'] = {
                'success': False,
                'error': 'Json decode error'
            }
        else:
            response['body'] = {
                'success': False,
                'error': str(exception)
            }

    if isinstance('body' in response and response['body'], dict):
        response['body'] = json.dumps(response['body'])

    response['headers'] = {
        'Access-Control-Allow-Origin': '*'
    }

    return response


def add_image_to_post():
    pass