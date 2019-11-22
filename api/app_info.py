import requests
import json

proxy = '127.0.0.1:12639'

proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy
}

bk_app_code = 'lxwtest'
bk_app_secret = 'bf826f0e-6029-4f20-8d26-c98a84f550e2'
bk_username = 'bkdoc'
