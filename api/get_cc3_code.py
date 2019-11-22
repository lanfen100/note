import requests

bk_token = 'wEJZPj3lTvKSqjEqAK7hQThpOwAxvGpxXR1TtorPAXY'
bk_app_code = 'new85'
bk_app_secret = 'f8f3719b-1ed1-4d10-a136-9d85fb6dce50'

cookie = {
    "bk_token": bk_token,
    #"qcloud_from": 'qcloud.baidu.seo-1566196069312',
    "blueking_language": 'zh-cn'
}

response = requests.get('https://cmdbce-b.o.qcloud.com/', cookies=cookie ,verify=False)

print(response.headers)
print(response.headers['Set-Cookie'])