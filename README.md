# IPProxy
爬虫所需要的IP代理，抓取八个网站的代理IP检测/清洗/入库/更新，添加调用接口<br>
<hr /><br>
<h3>如何使用</h3>
查看demo.py<br><br>
Util.Refresh()：数据库和新的数据需要主动调用此函数更新<br><br>
Util.Get()：调用可获取一条可用的代理，Util.Get()返回的代理：<br>
{'http': 'http://115.159.152.130:81', 'https': 'https://115.159.152.130:81'}<br>
requests可以直接使用：requests.get(url,proxies=Util.Get(),headers={})
