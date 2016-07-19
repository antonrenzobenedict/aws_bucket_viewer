#!/usr/bin/python
import sys
import boto3

s3 = boto3.resource(
    's3',
    aws_access_key_id=sys.argv[1],
    aws_secret_access_key=sys.argv[2]
)

#for bucket in s3.buckets.all():
 #      print bucket.name

bucket = s3.Bucket('3kricegenome')
for obj in bucket.objects.all():
    print(obj.key)


