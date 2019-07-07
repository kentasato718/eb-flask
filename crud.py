import boto3

db = boto3.resource('dynamodb', region_name='ap-northeast-1')
table = db.Table('signuptable')

# get item
response = table.get_item(Key={'email': 'kenta@test.com'})

print(response['Item'])

# put item
table.put_item(
    Item={
        'email': 'sato@test.com',
        'first_name': 'Eri',
        'last_name': 'Sato',
        'age': 37
    }
)

# Update item
table.update_item(
    Key={'email': 'sato@test.com'},
    UpdateExpression='SET age = :val',
    ExpressionAttributeValues={':val': 38}
)

# delete item
table.delete_item(Key={'email': 'kenta@test.com'})