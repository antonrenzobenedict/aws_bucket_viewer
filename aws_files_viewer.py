#!/usr/bin/python
import sys
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id=sys.argv[1],
    aws_secret_access_key=sys.argv[2]
)

bucket = s3.Bucket(sys.argv[3])

fileList = open(sys.argv[4], 'w')

fileList.write(sys.argv[3] + "\n")
for obj in bucket.objects.all():
        fileList.write(obj.key + "\n")
