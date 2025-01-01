import os
import requests
import hmac
import hashlib
import base64
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import quote

load_dotenv()

azure_master_key = os.environ.get("azure_key")      # you can select here primary key
azure_cosmos_db_url = os.environ.get("azure_url")  # https://<paste here cosmos db account name>.documents.azure.com:443


def prepare_auth_token(method,azure_master_key, resource_type, resource_link, date):
    key_type = "master"
    token_version = "1.0"
    payload = f"{method.lower()}\n{resource_type.lower()}\n{resource_link}\n{date.lower()}\n\n"

    # Decode the key from base64
    key_bytes = base64.b64decode(azure_master_key)

    # Create HMACSHA256 hash object
    hmac_sha256 = hmac.new(key_bytes, payload.encode('utf-8'), hashlib.sha256)

    # Compute the hash of the payload
    hash_payload = hmac_sha256.digest()

    # Convert hash to base64
    signature = base64.b64encode(hash_payload).decode('utf-8')

    # URL encode the authorization string
    auth_set = f"type={key_type}&ver={token_version}&sig={quote(signature)}"

    return auth_set

method = "get"
resource_type = "dbs"
resource_link = "dbs/testdb"     # here just i want to verify about db
date = datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT")


master_auth_token = prepare_auth_token(method, azure_master_key, resource_type, resource_link, date)

headers = {
    "Authorization": master_auth_token,
    "x-ms-date": date,
    "Accept": "application/json",
    "x-ms-partitionkey": '["partition_key"]',     # you need to pass here your partion key
    "x-ms-version":"2018-12-31"

}

res = requests.get(url = azure_cosmos_db_url, headers=headers)

print(res.status_code)
print(res.json())