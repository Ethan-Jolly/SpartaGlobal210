from google.cloud import storage
from google.oauth2.service_account import Credentials


class AccessGCPStorage:
    def __init__(self, key_path, bucket_name='ejspartabucket'):
        self.key_path = key_path
        self.credentials = Credentials.from_service_account_file(self.key_path)
        self.client = storage.Client(credentials=self.credentials)
        self.bucket = self.client.get_bucket(bucket_name)

    def download_file(self, file_on_cloud, local_file):
        blob = self.bucket.blob(file_on_cloud)
        blob.download_to_filename(local_file)

    def read_file(self, cloud_file):
        blob = self.bucket.blob(cloud_file)
        text = blob.download_as_string().decode('utf-8')
        return text

    def upload_file(self, file_on_cloud, local_file):
        blob = self.bucket.blob(file_on_cloud)
        blob.upload_from_filename(local_file)


def main():
    access_gcp = AccessGCPStorage('keys/gcp_storage_key.json')
    access_gcp.upload_file('GCPBucketTest', 'GCPBucketTest.txt')
    access_gcp.download_file('GCPBucketTest', 'GCPBucketTest')

    print(access_gcp.read_file('GCPBucketTest'))


if __name__ == '__main__':
    main()
