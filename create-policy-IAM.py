import boto3,json
iam=boto3.client('iam')
my_managed_policy={
    "Version":"2012-10-17",
    "Statement": [
        {
       "Effect": "Allow",
       "Action": [
       "ec2:Describe*",
       "ec2:CreateSecurityGroup",
       "ec2:TerminateInstances",
       "ec2:RunInstances",
       "ec2:DeleteSecurityGroup",
       "ec2:AuthorizeSecurityGroupIngress",
       "ec2:CreateTags",
       "ec2:DescribeKeyPairs",
       "ec2:ImportKeyPair",
        "ec2:DescribeNetworkInterfaces",
        "ec2:CreateNetworkInterface",
        "ec2:DeleteNetworkInterface",
        "ec2:AttachNetworkInterface",
        "ec2:DetachNetworkInterface",
        "ec2:DescribeImages",
        "ec2:CopyImage",
        "ec2:CreateImage",
        "ec2:DescribeInstances",
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:RebootInstances",
        "ec2:ModifyInstanceAttribute",
        "ec2:CreateSnapshot",
        "ec2:DescribeSnapshots",
        "ec2:DeleteSnapshot"     
                  
       ],
       "Resource": "*" #The "Resource" field is empty, which means this policy will apply to all Lambda functions. You may want to specify an ARN here to limit the scope.

},
{
    "Effect": "Allow",
    "Action":[
        "ec2:DescribeVpcs",
        "ec2:CreateDefaultVpc",
        "ec2:DeleteVpc",
        "ec2:DeleteSubnet",
        "ec2:DeleteRouteTable",
        "ec2:DeleteSecurityGroup",
        "ec2:DetachInternetGateway",
        "ec2:DeleteInternetGateway"

    ],
    "Resource": "*"
}
    ]
}
response=iam.create_policy(
    PolicyName='Your-policy-name',
    PolicyDocument=json.dumps(my_managed_policy)
)
policy_arn=response['Policy']['Arn']

# Attach the policy to the User 

iam.attach_user_policy(
    UserName='your User name',
    PolicyArn=policy_arn
)
policies = iam.list_attached_user_policies(UserName='your user name')
print(policies)
