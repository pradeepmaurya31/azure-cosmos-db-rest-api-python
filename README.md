# azure-cosmos-db-rest-api-python
azure cosmos db rest api communication using python requests module

1. use this url for basic test https://<paste here cosmos db account name>.documents.azure.com:443/dbs
- method = "get"
- resource_type = "dbs"
- resouce_link = ""

2. After final prepartion should be like below
- date = Fri, 03 Jan 2025 15:54:24 GMT
- url = https://test_db.documents.azure.com:443/                      # I added "test_db" as a test account you will see yours 
- master_key = type=master&ver=1.0&sig=7p63oNQ3gppWVz8cUEAoVQy4bA1am%2Bk%2BYzN3PbbTK0E%3D

Note- 
1. for this get resquest, partion_key not required, otherwise you need to pass header it in stringified array format.
2. if anywhere you missed like resource_type or resource_link not added correctly it will return 401, unauthorization error.
3. During master key prepartion all these parameter need to pass into lower case only including date
