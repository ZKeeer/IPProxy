# IPProxy
爬虫所需要的IP代理，抓取八个网站的代理IP检测/清洗/入库/更新，添加调用接口<br>
如何使用，查看demo.py<br>
数据库和新的数据需要主动调用Util.Refresh()函数更新<br>
调用Util.Get()可获取一条可用的代理，Util.Get()返回的代理：{'http': 'http://115.159.152.130:81', 'https': 'https://115.159.152.130:81'}，requests可以直接使用
