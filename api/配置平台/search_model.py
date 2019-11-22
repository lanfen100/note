from api.app_info import *

data = {
    "bk_app_code": "n1013",
    "bk_app_secret": 'cf53bdb8-d6cf-4840-8bc4-c28a6042272e',
    "bk_username": 'bkdoc',
    "fields": [
        "bk_module_name"
    ],
    "condition": {
        "bk_module_name": "belong"
    },
    "page": {
        "start": 0,
        "limit": 10
    }
}

response = requests.post(
    'http://dpaas.ce.bktencent.com/api/c/compapi/v2/cc/search_module/',
    data=json.dumps(data)
)

print(response.json())