import boto3,json
iam=boto3.client('iam')
response=iam.get_policy(
    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'
)
#print(response['Policy']['CreateDate'])
#print(response['Policy'].keys())
print(response['Policy'])
print(response)