import os

import boto3

# install aws_cli

os.system("pip3 install awscli --upgrade --user")

# configure aws_cli

user_id = 'scantist'
user_name = 'XXX'
user_password = 'XXX'

os.system("export AWS_ACCESS_KEY_ID=%s" % user_name)
os.system("export AWS_SECRET_ACCESS_KEY=%s" % user_password)
os.system("export AWS_DEFAULT_OUTPUT=%s" % 'json')

# configure s3
DB_url = 'XXX'
DB_user_name = 'XXX'
DB_user_password = 'XXX'

os.system("aws configure set default.s3.max_concurrent_requests %d" % 20)
os.system("aws configure set default.s3.max_queue_size %d" % 1000)
os.system("aws configure set default.s3.multipart_threshold %s" % '64MB')
os.system("aws configure set default.s3.multipart_chunksize %s" % '16MB')
os.system("aws configure set default.s3.max_bandwidth %s" % '50MB/s')
os.system("aws configure set default.s3.use_accelerate_endpoint %s" % 'false')
os.system("aws configure set default.s3.addressing_style %s" % 'path')

# download data from AWS cloud
bucket_name = 'scantist-engine-resource'
# Retrieve a bucket's ACL
s3_resource = boto3.resource('s3')
# s3_client = boto3.client('s3')
bucket = s3_resource.Bucket(bucket_name)
all_objects = bucket.objects.filter(Prefix='jars')
for object in all_objects:
    key_value = object.key
    file_path = str(key_value)
    file_content = file_path.split('/')
    library_info = file_content[-1]
    library_name = "_".join(library_info.split('-')[:-1])
    library_version = library_info.split('-')[-1]
    print(file_path + "\t\tlibrary_name:\t%s \t\t library_verison:\t%s" % (library_name, library_version))
    bucket.download_file(key_value, '/home/wufeng/Downloads/AWS/' + library_info)
