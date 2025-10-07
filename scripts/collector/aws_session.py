import os
import boto3
from dotenv import load_dotenv


def ec2_resource():
    return boto3.resource('ec2')

def aws_session():
    return boto3.client('ec2')