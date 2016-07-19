#!/usr/bin/python
import sys
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id=sys.argv[1],
    aws_secret_access_key=sys.argv[2]
)

bucketList = open(sys.argv[3], 'w')

for bucket in s3.buckets.all():
        bucketList.write(bucket.name + "\n")
