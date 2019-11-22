import requests
import json

bk_app_code = 'new85'
bk_app_secret = '6c1456ff-7daf-4e82-a8ce-8bd48c6750bd'


data = {
    "bk_app_code": bk_app_code,
    "bk_app_secret": bk_app_secret,
    "bk_username": "admin",
    "data": {
        "bk_biz_name": "cc_app_test",
        "bk_biz_maintainer": "admin",
        "bk_biz_productor": "admin",
        "bk_biz_developer": "admin",
        "bk_biz_tester": "admin",
        "time_zone": "Asia/Shanghai",
        "language": '1',
        'bk_supplier_id': 1,
    }
}


response = requests.session().post(
    'http://paas-test.o.qcloud.com/api/c/compapi/v2/cc/create_business/',
    data=json.dumps(data),
    verify=False
)


print(response.json())