from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
import json

# Credentials
storage_account_name = "mlframeworkledger"
container_name = "testsparkv1-2022-12-28t08-49-36-356z"
storage_account_key = "vOqPQ7a9mlZGeG4wXbCncuOVp9TbOP9Vcv+xaepMmu7aHxuxjduXbFi05+bwC0iwhJElNBw/yJ/W+AStFUF3NQ=="
connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"

# Data File path and Output file name
df_path = "https://mlframeworkledger.blob.core.windows.net/testsparkv1-2022-12-28t08-49-36-356z/testdata.parquet"
file_name = "bitanTest/testUpload.json"

# Making a Blob client to connect to our Blob
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

# Making a container client to connect to our container
container_client = blob_service_client.get_container_client(container_name)

# List of files in the container
blob_list = list()
for blob_i in container_client.list_blobs():
    blob_list.append(blob_i.name)

# Generate Shared Access Signature token to read the file
for blob_i in blob_list:
    sas_i = generate_blob_sas(account_name=storage_account_name,
                                container_name=container_name,
                                blob_name=blob_i,
                                account_key=storage_account_key,
                                permission=BlobSasPermissions(read=True),
                                expiry= datetime.utcnow() + timedelta(hours=1))

    sas_url = f'https://{storage_account_name}.blob.core.windows.net/{container_name}/{blob_i}?{sas_i}'

data = {"msg": "Test Blob Upload"}
data = json.dumps(data)
blob_client.upload_blob(data)