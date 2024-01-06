import boto3

client=boto3.client('s3')

response=client.get_bucket_acl(
    Bucket='my-demo-boto3-bucket'
)

print(response)