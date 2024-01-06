import boto3

client = boto3.client('ec2')
subnets = [
  'subnet-SubnetID',
  'subnet-SubnetID',
  'subnet-SubnetID'
]

for subnet in subnets:
  client.delete_subnet(SubnetId=subnet)


response = client.detach_internet_gateway(InternetGatewayId='igw-igID', VpcId='vpc-VPC-ID')  

gateways = [
  'igw-igID'
]
for gateway in gateways:
  client.delete_internet_gateway(InternetGatewayId=gateway)

response = client.detach_internet_gateway(InternetGatewayId='igw-igID', VpcId='vpc-VPC-ID')

response = client.detach_route_table(
  RouteTableId='rtb-rtb-ID',
)


vpc_id = 'vpc-VPC-ID'
client.delete_vpc(VpcId=vpc_id)

tables = [
  'rtb-rtID'
]

for table in tables:
  client.delete_route_table(RouteTableId=table)