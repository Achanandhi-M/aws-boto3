import boto3

client = boto3.client('s3')

bucket_name=input('Enter your Bucket Name: ')

response=client.create_bucket(
    Bucket= bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1',
    },
)
print(response)