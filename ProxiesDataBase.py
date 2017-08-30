# table IPPORT
# ip_port TEXT NOT NULL
import random
import sqlite3
from threading import Thread
import traceback
import Config
import GetIP


def InitDB():
    db_conn = sqlite3.connect(Config.DBName)
    try:
        db_conn.execute(
            """CREATE TABLE IF NOT EXISTS {} (IP_PORT TEXT NOT NULL PRIMARY KEY);""".format(Config.TabelName))
        db_conn.commit()
        return True
    except BaseException as e:
        db_conn.rollback()
        return False
    finally:
        db_conn.close()


def AddItem(ip_port):
    db_conn = sqlite3.connect(Config.DBName)
    db_cursor = db_conn.cursor()

    try:
        db_conn.execute("""INSERT INTO {} VALUES ('{}');""".format(Config.TabelName, ip_port))
        db_conn.commit()
    except BaseException as e:
        db_conn.rollback()
        traceback.print_exc()
    db_conn.close()


def DelItem(item):
    db_conn = sqlite3.connect(Config.DBName)

    try:
        db_conn.execute("""DELETE FROM {} WHERE IP_PORT = '{}';""".format(Config.TabelName, item))
        db_conn.commit()
    except BaseException as e:
        db_conn.rollback()
        traceback.print_exc()
    finally:
        db_conn.close()


def ClearItems():
    db_conn = sqlite3.connect(Config.DBName)
    try:
        db_conn.execute("""DELETE FROM {};""".format(Config.TabelName))
        db_conn.commit()
    except BaseException as e:
        db_conn.rollback()
        traceback.print_exc()
    finally:
        db_conn.close()


def GetItems():
    ip_list = []
    db_conn = sqlite3.connect(Config.DBName)
    db_cur = db_conn.cursor()
    try:
        tmp = db_cur.execute("""SELECT * FROM {};""".format(Config.TabelName)).fetchall()
        for item in tmp:
            ip_list.append(item[0])
    except BaseException as e:
        traceback.print_exc()
    finally:
        db_conn.close()
        return ip_list



