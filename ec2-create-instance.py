import boto3

ec2=boto3.client('ec2')

response=ec2.run_instances(
    ImageId='',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='myKey',
    TagSpecifications=[
    {
      'ResourceType': 'instance',
      'Tags': [
        {
          'Key': 'Name',
          'Value': 'Myboto3-instance'
        }
      ]
    }
  ]
)

instance=response['Instances'][0]
print(instance['InstanceId'])