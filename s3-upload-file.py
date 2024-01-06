import boto3

s3=boto3.client('s3')

response=s3.upload_file('/home/user/test.txt','my-demo-s3-lambda-buck','test')

print(response)