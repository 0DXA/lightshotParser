import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import string
import random
import time
"""Сори за говнокод"""

class Parser(object):
    cnt = 0
    def get(self, url, proxy):
        ua = UserAgent()
        self.cnt += 1
        print(self.cnt, url, proxy)
        proxyDict = {
            "http": "http://%s" %proxy,
            "https": "https://%s" %proxy,
        }
        headers = {'User-Agent': str(ua.random)}
        response = requests.get("https://prnt.sc/%s"%url, headers=headers, proxies=proxyDict,verify=False)
        soup = BeautifulSoup(response.text, 'lxml')
        try:
            imgur = soup.find("img", id="screenshot-image")["src"]
            req = requests.get(imgur,headers=headers,proxies=proxyDict,verify=False)
            with open("img/%s.png" % url, "wb") as code:
                code.write(req.content)
            return "OK"
        except TypeError:
            return None



def randanl():
    anl = (string.digits + string.ascii_lowercase)
    s = ""
    for i in range(6):
        s +=(anl[random.randint(0,len(anl)-1)])
    return s

def get_proxy(lst):
    return lst[random.randint(0, len(proxies) - 1)]

def find_aver(lst):
    return sum(lst) / len(lst)

if __name__ == "__main__":
    with open("http_proxies(1).txt") as f:
        proxies = f.read().split('\n')
    p = Parser()
    proxy = get_proxy(proxies)
    aver = []
    while True:
        link = randanl()
        if p.cnt==150:
            proxy = get_proxy(proxies)
            p.cnt = 0
            aver = []
        if link[0] != "0":
            try:
                time0 = time.time()
                resp = p.get(link, proxy)
                if resp == None:
                    proxy = get_proxy(proxies)
                    p.cnt = 0
                    aver = []
                timedelta = (time.time()-time0)
                aver.append(int(timedelta))
                faver = find_aver(aver)
                print(resp, int(timedelta), "с.",faver)
                if (faver>8) or ((timedelta-faver)>20):
                    proxy = get_proxy(proxies)
                    p.cnt = 0
                    aver = []

            except requests.exceptions.ProxyError:
                proxy = get_proxy()
                p.cnt = 0
                aver = []
            except requests.exceptions.MissingSchema:
                continue
            except requests.exceptions.ConnectionError as e:
                print(e)
                proxy = get_proxy(proxies)
                p.cnt = 0
                aver = []
            except Exception as e:
                print(type(e),e)



