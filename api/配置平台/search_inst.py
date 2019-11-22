from api.app_info import *


data = {
    "bk_obj_id": "test",
    "bk_supplier_account": "0",
    "page": {
        "start": 0,
        "limit": 10,
        "sort": "bk_inst_id"
    },
    "fields": "test",
    "condition": {
        "bk_weblogic": [
            {
                "field": "bk_inst_name",
                "operator": "$regex",
                "value": "qq"
            }
        ]
    }
}

response = requests.post(
    'http://dpaas.ce.bktencent.com/api/c/compapi/v2/cc/search_inst/',
    proxies=proxies,
    data=json.dumps(data),
    verify=False
)

print(response.json())