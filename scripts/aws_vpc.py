import boto3
import botocore
from aws_client import aws_client

vpc_client = aws_client()

def check_vpc_existence(name='default'):

    print(f"! checking vpc {name}")
    try:
        if(name=='default'):
            response_default_vpc = vpc_client.describe_vpcs(
                Filters = [{
                    "Name":"isDefault",
                    "Values":["true"]
                }]
            )
            vpc_data = response_default_vpc["Vpcs"][0]
            vpc_id = vpc_data["VpcId"]
            return vpc_id
        else:
            response_vpc = vpc_client.describe_vpcs(
                Filters = [{
                    "Name":"tag:Name",
                    "Values":[name]
                }]
            )
            print(response_vpc)
            return id
        
    except Exception as e:
        print(":: Error ::",e)
        raise



check_vpc_existence()