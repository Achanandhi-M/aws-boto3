import boto3

client=boto3.client('s3')

#Display bucket

response=client.list_buckets()
print("Available buckets in your AWS Account")

for bucket in response['Buckets']:
    print(bucket['Name'])

delete_objects_in_bucket=input("Please provide the name of the bucket from which you'd like to delete objects: ")

# display objects
s3 = boto3.resource('s3')
bucket = s3.Bucket(delete_objects_in_bucket)
print("Available objects in your Bucket")
for obj in bucket.objects.all():
    print(obj.key)

# Delete objects
objects_to_delete=input("Enter the object name to delete: ")
response = client.delete_object(
    Bucket=delete_objects_in_bucket ,
    Key=obj.key
)
