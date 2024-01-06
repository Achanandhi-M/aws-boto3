import boto3

client=boto3.client('s3')

response_list_buckets=client.list_buckets()

print("Available buckets in your AWS Account")

for bucket in response_list_buckets['Buckets']:
    print(bucket['Name'])

bucket_to_delete=input("Enter the bucket name which you want to delete?:")

def my_delete_bucket(bucket_to_delete) :
    response=client.delete_bucket(
    Bucket=bucket_to_delete
)
response= my_delete_bucket(bucket_to_delete)
print(response)

