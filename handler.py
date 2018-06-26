import json
import boto3
import base64
import uuid
import decimal
import time

import api
from urllib import parse
from io import BytesIO
from PIL import Image
from voluptuous import Schema, Required, Length, All, Invalid, Any, Optional
from boto3.dynamodb.conditions import Attr, Key

pictures = boto3.resource('dynamodb', region_name='us-east-1').Table('jPictures')
s3 = boto3.resource('s3')

pictureSchema = Schema({
    Optional('description'): All(str),
    Required('base64'): All([str]),
})

postSchema = Schema({
    Required('images'): All([pictureSchema]),
    Optional('tags'): All([str]),
    Optional('title'): All(str)
})

searchSchema = Schema({
    Required('q'): All(str, Length(min=3, max=64)),
    Optional('l'): All(str)
})


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError


def add_cors(d):
    d['headers'] = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': True
    }

    return d


class InvalidImageFormat(Exception):
    def __init__(self, message, errors):
        super().__init__(message)

        self.errors = errors


class InvalidImageResolution(Exception):
    def __init__(self, message):
        super().__init__(message)


class MissingParameters(Exception):
    def __init__(self, message):
        super().__init__(message)


def new_postv1(event, context):
    response = dict()

    try:
        picture = json.loads(event['body'])
        pictureSchema(picture)
        image_stream = BytesIO(base64.b64decode(picture['image']))

        image = Image.open(image_stream)

        width, height = image.size

        if width < 512 or height < 512:
            raise InvalidImageResolution('Dimension cant be less then 512 pixels')

        if width > 7680 or height > 7680:
            raise InvalidImageResolution('Dimension cant be more then 7680 pixels')

        new_image = BytesIO()
        image.save(new_image, format='PNG')
        new_image.seek(0)

        filename = str(uuid.uuid4()) + '.png'

        image_object = s3.Object('judge-my-pics-images', filename)
        image_object.put(Body=new_image, ACL='public-read')

        picture['filename'] = filename
        picture['createdAt'] = int(time.time())

        del picture['image']

        pictures.put_item(Item=picture)

        response['statusCode'] = 200
        response['body'] = {
            'success': True
        }

    except json.JSONDecodeError:
        response['statusCode'] = 400
        response['body'] = {
            'error': 'Invalid json'
        }
    except Invalid as e:
        response['statusCode'] = 400
        response['body'] = {
            'error': str(e)
        }

    except InvalidImageFormat:
        response['statusCode'] = 400
        response['body'] = {
            'error': 'Image is wrong format'
        }

    except InvalidImageResolution as e:
        response['statusCode'] = 400
        response['body'] = {
            'error': str(e)
        }

    except ValueError:
        response['statusCode'] = 400
        response['body'] = {
            'error': 'Invalid base64 format'
        }

    except Exception as e:
        print(e)

    response['body'] = json.dumps(response['body'])
    response = add_cors(response)

    return response


def search(event, context):
    response = dict()

    try:
        params = searchSchema(event['queryStringParameters'])
        q = params['q']

        data = pictures.scan(
            FilterExpression=Attr('title').contains(q),
            Limit=2,
        )

        del data['ResponseMetadata']

        response['statusCode'] = 200
        response['body'] = {
            'data': data
        }

    except Invalid as e:
        response['statusCode'] = 400
        response['body'] = {
            'error': str(e)
        }
    except Exception as e:
        response['statusCode'] = 500
        response['body'] = {
            'error': str(e)
        }

    response['body'] = json.dumps(response['body'], default=decimal_default)
    response = add_cors(response)

    return response


def get(evnet, context):
    response = dict()

    data = pictures.scan()

    del data['ResponseMetadata']

    response['statusCode'] = 200
    response['body'] = {
        'data': data
    }

    response['body'] = json.dumps(response['body'], default=decimal_default)
    response = add_cors(response)

    return response


def test(event, context):
    response = {
        'statusCode': 200,
        'body': json.dumps(event)
    }

    return add_cors(response)


def get_lastest(eevent, context):
    response = dict()

    try:
        pictures.query(KeyConditionExpression=Key('postedAt').lt())

    except Exception as err:
        response['statusCode'] = 500
        response['body'] = {
            'error': str(err)
        }


def new_post(event, context):
    try:
        body = json.loads(event['body'])

        return api.process_response(api.new_post(body, event['requestContext']['identity']['cognitoIdentityId']))
    except Exception as e:
        return api.process_response(None, exception=e)
