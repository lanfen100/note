from api.app_info import *


data = {
    'bk_app_code': bk_app_code,
    'bk_app_secret': bk_app_secret,
    'bk_username': bk_username,
}

response = requests.get(
    'http://dpaas.ce.bktencent.com/api/c/compapi/v2/bk_login/get_all_users/',
    proxies = proxies,
    data=json.dumps(data),
    verify=False
)

print(response.json())