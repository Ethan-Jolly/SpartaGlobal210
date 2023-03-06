from google.cloud import storage


"""
Uploading files to Google Cloud Storage
"""


def upload_blob(bucket_name, source_file_name, blob_name):
    """Upload a file from local to the bucket.
    bucket_name = "your-bucket-name"
    source_file_name = "local/path/to/file"
    destination_blob_name = "storage-object-name"
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.upload_from_filename(source_file_name)


def upload_data_to_gcs(bucket_name, string_data, blob_name):
    """

    :param bucket_name: bucket name in google cloud
    :param string_data: data in a string
    :param blob_name: "storage-object-name"
    :return: None , the data will be stored to bucket as "text/plain"
    """
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        bucket.blob(blob_name).upload_from_string(string_data)
        return bucket.blob(blob_name).public_url

    except Exception as e:
        print(e)
    return None


def upload_blob_string(bucket_name, string_data, blob_name, content_type='image/jpg'):
    """Uploads file directly from data to the bucket by specifying its Type.
    bucket_name = "your-bucket-name"
    string_data = "local/path/to/file"
    blob_name = "storage-object-name"
    content_type = the data will be stored to bucket as content_type and default is  image/jpg
    other options : image/jpeg , application/pdf , text/plain
    """

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        blob.upload_from_string(string_data, content_type=content_type)

        print("File uploaded to {}.".format(blob_name))
    except Exception as e:
        print(e)

    return None


def upload_jpg_img_to_gcs(bucket_name, data, blob_name):
    """

    :param bucket_name: buncket name in Google cloud Storage
    :param data:
    :param blob_name:storage-object-name"
    :return: public_url if works otherwise None
    """

    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        bucket.blob(blob_name).upload_from_string(
            data, content_type="image/jpeg")
        return bucket.blob(blob_name).public_url

    except Exception as e:
        print(e)

    return None


"""
Downloading files from Google Cloud Storage
"""


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """
    Downloads a blob from the bucket to local path.
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Blob {} downloaded to {}.".format(
            source_blob_name, destination_file_name
        )
    )


def download_blob_content(bucket_name, source_blob_name):
    """
    :param bucket_name: name of the gcs bucket
    :param source_blob_name: blob path
    :return: content of the image
    """
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    # print(blob.content_type)
    content = blob.download_as_string().decode('utf-8')

    return content


"""
Some extra needed functionalities
"""


def create_folder(bucket_name, destination_folder_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_folder_name)

    blob.upload_from_string('')

    print('Created {} .'.format(
        destination_folder_name))


def rename_blob(bucket_name, blob_name, new_name):
    """Renames a blob."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"
    # new_name = "new-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    new_blob = bucket.rename_blob(blob, new_name)

    print("Blob {} has been renamed to {}".format(blob.name, new_blob.name))


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print("Blob {} deleted.".format(blob_name))


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    for blob in blobs:
        print(blob.name)


def list_blobs_with_prefix(bucket_name, prefix, delimiter="None"):
    """Lists all the blobs in the bucket that begin with the prefix.

    This can be used to list all blobs in a "folder", e.g. "public/".

    The delimiter argument can be used to restrict the results to only the
    "files" in the given "folder". Without the delimiter, the entire tree under
    the prefix is returned. For example, given these blobs:

        a/1.txt
        a/b/2.txt

    If you just specify prefix = 'a', you'll get back:

        a/1.txt
        a/b/2.txt

    However, if you specify prefix='a' and delimiter='/', you'll get back:

        a/1.txt

    Additionally, the same request will return blobs.prefixes populated with:

        a/b/
    """

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(
        bucket_name, prefix=prefix, delimiter=delimiter
    )

    print("Blobs:")
    for blob in blobs:
        print(blob.name)

    if delimiter:
        print("Prefixes:")
        for prefix in blobs.prefixes:
            print(prefix)

