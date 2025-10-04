import boto3
import botocore
from aws_client import aws_client

client = aws_client()
list_regions = []


def fetch_regions():
    
    try:
        response_region = client.describe_regions()
        regions_data = response_region["Regions"]
        region_count = len(regions_data)

        for _ in range(region_count):
            region_data = regions_data[_]
            region_name = region_data['RegionName']
            list_regions.append(region_name)    

        print(list_regions)
        return list_regions
    
    
    except Exception as e:
        print(":: Error ::",e)
        raise
    