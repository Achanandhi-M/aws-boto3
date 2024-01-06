import boto3

# Create an IAM client
iam = boto3.client('iam')

# List IAM users
response = iam.list_users()

# Print user information
print("IAM Users:")
for user in response['Users']:
    print(f"Username: {user['UserName']}, UserID: {user['UserId']}, ARN: {user['Arn']}")
