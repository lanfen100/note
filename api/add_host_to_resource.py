import requests
import json

bk_app_code = 'new85'
bk_app_secret = 'f8f3719b-1ed1-4d10-a136-9d85fb6dce50'

data = {
    "bk_app_code": bk_app_code,
    "bk_app_secret": bk_app_secret,
    "bk_username": 'admin',
    "bk_supplier_id": 1,
    "host_info": {
        "0": {
            "bk_host_innerip": "10.0.0.1",
            "bk_cloud_id": 0,
            "import_from": "3"
        }
    }
}

response = requests.session().post(
    'https://paasce-b.o.qcloud.com/api/c/compapi/v2/cc/add_host_to_resource/',
    data=json.dumps(data),
    verify=False
)

print(response.json())