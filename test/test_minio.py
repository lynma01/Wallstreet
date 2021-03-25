import boto3
from botocore.client import Config


s3 = boto3.resource('s3',
                    endpoint_url='http://localhost:9000',
                    aws_access_key_id='minio-admin',
                    aws_secret_access_key='minio-secret-key-CHANGE-ME',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

for bucket in s3.buckets.all():
    print(bucket.name)