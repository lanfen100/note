import requests
import json

bk_app_code = 'new85'
bk_app_secret = '6c1456ff-7daf-4e82-a8ce-8bd48c6750bd'

data = {
    "bk_app_code": bk_app_code,
    "bk_app_secret": bk_app_secret,
    "bk_username": 'bkdoc',
    "bk_supplier_account": "1",
    "fields": [
        "bk_biz_id",
        "bk_biz_name"
    ],
    "condition": {
        "bk_biz_name": "esb-test"
    },
    "page": {
        "start": 0,
        "limit": 10,
        "sort": ""
    }
}
response = requests.session().post(
    'http://dpaas.ce.bktencent.com/api/c/compapi/v2/cc/search_business/',
    data=json.dumps(data),
)

print(response.json())