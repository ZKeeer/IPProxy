import random

import ProxiesDataBase
import GetIP
import re

def Refresh():
    GetIP.RefreshDB()
    GetIP.GetIP()

def Get():
    proxies_dict = {}
    result = ProxiesDataBase.GetItems()
    if result:
        tmp = random.choice(result)
        proxies_dict['http'] = 'http://{}'.format(tmp)
        proxies_dict['https'] = 'https://{}'.format(tmp)
    return proxies_dict

