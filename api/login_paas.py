import requests
import random
import http.cookiejar as cookielib


class LoginPaaS():

    def __init__(self):
        self.headers = {
            'Referer': 'https://paasce-b.o.qcloud.com/login',
            'Host': 'paasce-b.o.qcloud.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        self.login_url = 'https://paasce-b.o.qcloud.com'
        self.post_url =  'https://paasce-b.o.qcloud.com/login/?c_url=/'
        self.logined_url = 'https://paasce-b.o.qcloud.com'
        self.session = requests.Session()

    def get_bklogin_csrftoken(self):
        self.session.cookies = cookielib.LWPCookieJar(filename='cookies.txt')
        r = self.session.get(self.login_url, headers=self.headers, verify=False)
        csrf_token = dict(r.cookies)
        print(csrf_token)
        print(r.headers)
        return csrf_token

    def login(self, username, password):
        csrf = self.get_bklogin_csrftoken()
        post_data = {
            'csrfmiddlewaretoken': csrf,
            'username': username,
            'password': password,
            'next': None,
            'app_id': None
        }
        r = requests.post(self.post_url, data=post_data, headers=self.headers, verify=False)
        print(r.status_code)


if __name__ == '__main__':
    l = LoginPaaS()
    l.get_bklogin_csrftoken()
    #l.login('admin', 'Paas@123')