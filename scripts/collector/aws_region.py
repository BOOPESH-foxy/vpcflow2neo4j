import boto3
import botocore
from aws_session import aws_session

client = aws_session()
list_regions = []

def fetch_regions():
    
    try:
        response_region = client.describe_regions(
            AllRegions=True, 
            Filters=[{
                "Name":"opt-in-status",
                "Values":["opt-in-not-required","opted-in"
                    ]}])
        return sorted([_["RegionName"] for _ in response_region["Regions"]])
    
    except Exception as e:
        print(":: Error ::",e)
        raise