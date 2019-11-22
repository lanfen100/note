import requests

proxy = '127.0.0.1:12639'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

res = requests.get('http://mp.weixin.qq.com/s?__biz=MjM5NTcxMTE2Nw==&amp;mid=2653118788&amp;idx=1&amp;sn=1c6d41bc92b2b48199ff94f51cde7bb6&amp;chksm=bd2390948a5419825a5d063fc5fad23a0c916cfd6dc6087f5c079de647485075eb72f9e9714a&amp;scene=27#wechat_redirect',proxies=proxies)

print(res.text)