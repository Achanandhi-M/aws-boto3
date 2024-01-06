import boto3

ec2 = boto3.client('ec2')

# Describe VPCs to get default VPC ID
vpcs = ec2.describe_vpcs()['Vpcs']

default_vpc = [vpc for vpc in vpcs if vpc['IsDefault']][0]

# Delete subnets, route tables etc associated with default VPC

# Delete default VPC
response = ec2.delete_vpc(VpcId=default_vpc['VpcId'])
print(vpcs)
print(vpcs[0]['VpcId'])
print(vpcs[0]['OwnerId'])
print(vpcs[0]['CidrBlock'])

response = ec2.delete_vpc(VpcId=default_vpc['VpcId'])
print(response)