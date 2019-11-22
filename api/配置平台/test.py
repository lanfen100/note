from api.app_info import *


data = {
    'bk_app_code': bk_app_code,
    'bk_app_secret': bk_app_secret,
    'bk_username': bk_username,
}

response = requests.get(
    'http://dpaas.ce.bktencent.com:80/api/c/self-service-api/lxwtest/gateway_test/',
    proxies=proxies,
    params=data,
    verify=False
)

print(response.json())