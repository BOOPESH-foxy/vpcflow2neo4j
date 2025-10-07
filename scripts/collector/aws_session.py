import boto3

def boto3_session():
    return boto3.Session()

def ec2_resource():
    return boto3.resource('ec2')

def ec2_client():
    return boto3.client('ec2')