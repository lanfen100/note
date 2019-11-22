from api.app_info import *


data = {
    'bk_app_code': bk_app_code,
    'bk_app_secret': bk_app_secret,
    'bk_username': bk_username,
    "bk_obj_asst_id": "bk_switch_belong_bk_host",
    "bk_inst_id": 1,
    "bk_asst_inst_id": 2,

}

response = requests.post(
    'http://dpaas.ce.bktencent.com:80/api/c/compapi/v2/cc/add_instance_association/',
    proxies=proxies,
    data=json.dumps(data),
    verify=False
)

print(response.json())