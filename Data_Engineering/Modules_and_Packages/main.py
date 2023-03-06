from gcpStorage.utils import list_blobs
from gcpStorage.storage import *
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../keys/gcp_storage_key.json"
bucket_name = 'ejspartabucket'

list_blobs(bucket_name=bucket_name)
download_blob(bucket_name, 'GCPBucketTest.txt', 'GCPBucketTest.txt')
print(download_blob_content(bucket_name, 'GCPBucketTest.txt'))


# from summation import add_three (Can limit imports to only objects or functions which you need)

# Module is just a python file (A .py file)
