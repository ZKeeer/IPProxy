from random import choice
from re import findall
from threading import Thread
from traceback import print_exc

from requests import get

import Config
import ProxiesDataBase

d = {}


def GetPageContent(tar_url):
    url_content = ""
    try:
        url_content = get(tar_url,
                          headers={
                              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                              'Accept-Encoding': 'gzip, deflate, compress',
                              'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
                              'Cache-Control': 'no-cache',
                              'Connection': 'keep-alive',
                              'Upgrade-Insecure-Requests': "1",
                              'User-Agent': choice(Config.UserAgents)
                          }).text
    except BaseException as e:
        print_exc()
        print('\n\n\n')
    finally:
        return url_content


def GetIP():
    ip_list = []
    for tar_url in Config.Url_Regular.keys():
        url_content = GetPageContent(tar_url)
        regular = Config.Url_Regular.get(tar_url, "")
        tmp_ip_list = findall(regular, url_content)
        for item in tmp_ip_list:
            ip_list.append("{}:{}".format(item[0], item[1]))
            # print(tar_url, "\niplist_len: ", ip_list.__len__())

    thread_list = []
    for item in ip_list:
        thread_list.append(Thread(target=VertifyIp, args=(item.split(':')[0], item.split(':')[1])))
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()

    while d.__len__():
        ProxiesDataBase.AddItem(d.popitem()[0])


def RefreshDB():
    ip_list = ProxiesDataBase.GetItems()
    thread_list = []

    for item in ip_list:
        thread_list.append(Thread(target=VertifyIp, args=[item.split(':')[0], item.split(':')[1]]))
    for item in thread_list:
        item.start()
    for item in thread_list:
        item.join()

    ProxiesDataBase.ClearItems()
    while d.__len__():
        ProxiesDataBase.AddItem(d.popitem()[0])


def VertifyIp(ip, port):
    proxies = {"http": "http://{}:{}".format(ip, port), "https": "https://{}:{}".format(ip, port)}
    try:
        url_content = get(Config.TestUrl,
                          proxies=proxies,
                          timeout=Config.TestTimeOut,
                          headers={
                              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                              'Accept-Encoding': 'gzip, deflate, compress',
                              'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ru;q=0.4',
                              'Cache-Control': 'max-age=0',
                              'Connection': 'keep-alive',
                              'User-Agent': choice(Config.UserAgents)
                          })

        if int(url_content.status_code) == int(200) and "新闻" in url_content.text:
            d.update({"{}:{}".format(ip, port): 0})
    except BaseException as e:
        pass
