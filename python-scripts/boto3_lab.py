import boto3
import json


s3_client = boto3.client('s3')                          #initialize boto3 client
ec2_client = boto3.client('ec2')


# response = s3_client.list_buckets()                 #list bucket function
# print(json.dumps(response, default=str))
# print(response)
response = ec2_client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print(f"Instance Id: {instance['InstanceId']} - State: {instance['State']['Name']}")


# import boto3
# import json

# # Initialize boto3 client
# s3_client = boto3.client('s3')
# ec2_client = boto3.client('ec2')

# # List buckets function
# #response = s3_client.list_buckets()

# # print(json.dumps(response, default=str))

# # List all buckets from response
# # for buc in response["Buckets"]:
# #     print(buc["Name"])

# # List all instances
# response = ec2_client.describe_instances(
#     Filters=[
#         {
#             'Name': 'instance-state-name',
#             'Values': ['running']
#         }
#     ]
# )
# # print(json.dumps(response, default=str))

# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         print(f"Instance Id: {instance['InstanceId']} - State: {instance['State']['Name']}")
#         # print(f"Instance Id: {instance['InstanceId']} - State: {instance['State']}")