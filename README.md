# IPProxy
爬虫所需要的IP代理，抓取八个网站的代理IP检测/清洗/入库/更新，添加调用接口<br>
<hr /><br>
<h3>如何使用</h3>
查看<a href="https://github.com/ZKeeer/IPProxy/blob/master/demo.py">demo.py</a><br><br>
Util.Refresh()：数据库和新的数据需要主动调用此函数更新<br><br>
Util.Get()：调用可获取一条可用的代理，Util.Get()返回的代理：<br>
{'http': 'http://115.159.152.130:81', 'https': 'https://115.159.152.130:81'}<br>
requests可以直接使用：requests.get(url,proxies=Util.Get(),headers={})
<hr /><br>
<strong>Config.py 部分：</strong><br>

如果你还有代理网站可以添加，请添加在Url_Regular字典中。<br>
代理IP网址和对应的正则式，正则式一定要IP和Port分开获取，例如[(192.168.1.1, 80), (192.168.1.1, 90),]<br>
只抓取首页，想要抓取首页以后页面的可以将链接和正则式贴上来，例如，将某网站的1、2、……页的链接和对应的正则式分别添加到Url_Regular字典中。<br>

添加正则式之前请先在 <a href="http://tool.chinaz.com/regex">站长工具-正则表达式在线测试</a> 测试通过后添加<br>
<hr /><br>
<h4>数据来源：</h4>
<pre>http://www.kuaidaili.com/free/
http://www.66ip.cn/
http://www.xicidaili.com/nn/
http://www.ip3366.net/free/
http://www.proxy360.cn/Region/China
http://www.mimiip.com/
http://www.data5u.com/free/index.shtml
http://www.ip181.com/
http://www.kxdaili.com/</pre>
<hr /><br>
逻辑结构：<br>
<img src="https://github.com/ZKeeer/IPProxy/blob/master/%E9%80%BB%E8%BE%91%E5%9B%BE.png">
<hr /><br>
<strong>欢迎issue和pull，代码渣渣，大神轻喷</strong>
