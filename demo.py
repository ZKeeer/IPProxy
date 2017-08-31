import sqlite3
import GetIP
import Config
import ProxiesDataBase
import Util


def main():
    # 初始化数据库和数据表
    ProxiesDataBase.InitDB()
    # 刷新数据库，添加新数据
    Util.Refresh()
    # 获取一个代理使用
    proxies = Util.Get()
    print(proxies)

    # 查询数据库多少条数据
    conn = sqlite3.connect(Config.DBName)
    cu = conn.cursor()
    print(cu.execute("""SELECT * FROM {};""".format(Config.TabelName)).fetchall().__len__())
    cu.close()
    conn.close()


if __name__ == '__main__':
    main()
