import os
import boto3
import botocore

def aws_session():
    return boto3.Session
