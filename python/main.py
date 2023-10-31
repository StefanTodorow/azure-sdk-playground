from azure.storage.blob.baseblobservice import BaseBlobService
import os

account_name = os.environ.get("ACCOUNT_NAME")
account_key = os.environ.get("ACCOUNT_KEY")

print(account_name)
print(account_key)

blob_service = BaseBlobService(account_name =account_name, account_key=account_key)

print(blob_service)

containers = blob_service.list_containers()
for container in containers:
    print(container.name)
    blobs = blob_service.list_blobs(container.name)
    for blob in blobs:
        print(f'-> {blob.name}')