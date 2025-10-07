import boto3
import botocore
from aws_client import aws_client

vpc_client = aws_client()
vpc_id_list = []

def fetch_vpc_ids():
    print(f"! Fetching VPC id's")
    try:

        response_vpc = vpc_client.describe_vpcs(
        )
        len_of_list = len(response_vpc)
        for _ in range(len_of_list):
            vpc_data = response_vpc["Vpcs"][_]
            vpc_id = vpc_data["VpcId"]
            vpc_id_list.append(vpc_id)
    
        return vpc_id_list
        
    except Exception as e:
        print(":: Error ::",e)
        raise


def describe_eni_and_subnet():
    vpc_id_list = fetch_vpc_ids()
    response_vpc_description = vpc_client.describe_flow_logs()
    print(response_vpc_description)
    

