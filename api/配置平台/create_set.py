from api.app_info import *


data = {
    'bk_app_code': bk_app_code,
    'bk_app_secret': bk_app_secret,
    'bk_username': bk_username,
    'bk_biz_id': 4,
    'data': {
        "bk_parent_id": 4,
        "bk_set_name": "test-set",
    }
}

response = requests.post(
    'http://dpaas.ce.bktencent.com/api/c/compapi/v2/cc/create_set/',
    proxies = proxies,
    data=json.dumps(data),
    verify=False
)

print(response.json())