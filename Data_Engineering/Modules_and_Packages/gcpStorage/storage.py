from google.cloud import storage


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """    Downloads a blob from the bucket to local path.
        # bucket_name = "your-bucket-name"
        # source_blob_name = "storage-object-name"
        # destination_file_name = "local/path/to/file"    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)
    print("Blob {} downloaded to {}.".format(source_blob_name, destination_file_name))


def download_blob_content(bucket_name, source_blob_name):
    """ :param bucket_name: name of the gcs bucket
     :param source_blob_name: blob path
      :return: content of the image """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    print(blob.content_type)
    content = blob.download_as_string().decode('utf-8')
    return content
