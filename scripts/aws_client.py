import os
from dotenv import load_dotenv
import boto3
import botocore

load_dotenv()
REGION = os.getenv('REGION')

def aws_resources():
    return boto3.client()

def aws_client():
    return boto3.resource('',region_name = REGION)
    