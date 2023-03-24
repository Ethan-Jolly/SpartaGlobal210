import boto3
from pprint import pprint as pp
import json
import pandas as pd

s3_client = boto3.client('s3')  # low level
s3_resource = boto3.resource('s3')  # high level, object-orientated

bucket_list = s3_client.list_buckets()  # List of all buckets

bucket_name = 'data-eng-resources'
bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name)  # Listing all objects inside a particular bucket

bucket = s3_resource.Bucket(bucket_name)  # Creating an instance of the bucket
# objects = bucket.objects
# for object in objects.all():
#     print(object.key)

# Reading a json file from s3 bucket then using loads to convert from binary string to json
s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/chatbot-intent.json')
str_body = s3_object['Body'].read()
data = json.loads(str_body)
# pp(data)

# Reading a csv file from s3 bucket into a pandas dataframe
s3_object = s3_client.get_object(Bucket=bucket_name, Key='python/happiness-2019.csv')
df = pd.read_csv(s3_object['Body'])
# print(df.head())
# print(df.info())

dict_to_upload = {'name': 'paula', 'course': 'data', 'extra': '5'}


# with open('data210.json', 'w') as json_file:
#     json.dump(dict_to_upload, json_file)

# Uploading a file to the s3 bucket
# s3_client.upload_file(Filename='data210.json', Bucket=bucket_name, Key='Data210/ethan.json')

# Deleting a file from the s3 bucket
# s3_client.delete_object(Bucket=bucket_name, Key='Data210/ethan.json')

# Using put_object to upload the serialised python dictionary straight to the s3 bucket
# s3_client.put_object(Body=json.dumps(dict_to_upload), Bucket=bucket_name, Key='Data210/ethan.json')

# s3_object = s3_client.get_object(Bucket=bucket_name, Key='Data210/ethan.json')
# str_body = s3_object['Body'].read()
# data = json.loads(str_body)
# pp(data)

# df = pd.DataFrame([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])

# s3_object = s3_client.put_object(Body=df.to_csv(index=False), Bucket=bucket_name,
#                                             Key='Data210/ethan_csv.csv')

# print(type(df.to_csv(index=False)))

# s3_object = s3_client.get_object(Bucket=bucket_name, Key='Data210/ethan_csv.csv')
# df_s3 = pd.read_csv(s3_object['Body'])
# print(df_s3.head())

# Key='python/fish-market.csv'


def get_pandas_from_bucket(bucket_name, key_name):
    s3_object = s3_client.get_object(Bucket=bucket_name, Key=key_name)
    return pd.read_csv(s3_object['Body'])


def put_pandas_to_bucket(dataframe, bucket_name, key_name):
    s3_client.put_object(Body=dataframe.to_csv(index=False), Bucket=bucket_name, Key=key_name)


files = ['python/fish-market.csv', 'python/fish-market-mon.csv', 'python/fish-market-tues.csv']
dataframes = [get_pandas_from_bucket(bucket_name, file) for file in files]

df = pd.concat(dataframes)
# print(df)

fish_agg = df.groupby(['Species']).agg({'Weight': 'mean', 'Length1': 'mean', 'Length2': 'mean', 'Length3': 'mean', 'Height': 'mean', 'Width': 'mean'})

put_pandas_to_bucket(fish_agg, bucket_name, 'Data210/fish/ethan.csv')

# print(fish_agg)

print(get_pandas_from_bucket(bucket_name, 'Data210/fish/ethan.csv'))
