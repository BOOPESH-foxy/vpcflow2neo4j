import boto3
import botocore
from aws_client import aws_client

client = aws_client()
list_regions = []


def fetch_regions():
    
    try:
        r = client.describe_regions(
            AllRegions=True, 
            Filters=[{
                "Name":"opt-in-status",
                "Values":["opt-in-not-required","opted-in"
                    ]}])
        return sorted([x["RegionName"] for x in r["Regions"]])
    
    except Exception as e:
        print(":: Error ::",e)
        raise