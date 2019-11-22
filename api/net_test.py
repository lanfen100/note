import requests

res = requests.session().get('https://baidu.com')

print(res.status_code)