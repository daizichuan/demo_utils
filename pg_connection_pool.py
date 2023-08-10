import sys

import psycopg2.extras
from dbutils.pooled_db import PooledDB
import threading


class PgConnectionPool:
    _instance_lock = threading.Lock()

    def __init__(self):
        self.init_pool()

    # 单例模式
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with PgConnectionPool._instance_lock:
                if not hasattr(cls, '_instance'):
                    PgConnectionPool._instance = object.__new__(cls)
                return PgConnectionPool._instance

    def get_pool_conn(self):
        if not self._pool:
            self.init_pool()
        return self._pool.connection()

    def init_pool(self):
        try:
            pool = PooledDB(
                creator=psycopg2,  # 使用连接数据库的模块 psycopg2
                maxconnections=6,  # 连接池允许的最大连接数，0 和 None 表示不限制连接数
                mincached=1,  # 初始化时，链接池中至少创建的空闲的链接，0 表示不创建
                maxcached=0,  # 链接池中最多闲置的链接，0 和 None 不限制
                blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
                maxusage=None,  # 一个链接最多被重复使用的次数，None 表示无限制
                setsession=[],  # 开始会话前执行的命令列表
                host='',
                port='5432',
                user='',
                password='',
                database='',
                client_encoding='utf-8',  # 解决字符集问题
            )
            self._pool = pool
        except:
            print('connect postgresql error')
            self.close_pool()

    def close_pool(self):
        if self._pool != None:
            self._pool.close()

    def select_sql(self, sql):
        try:
            conn = self.get_pool_conn()
            cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)  # 设置返回格式为字典
            cursor.execute(sql)
            result = cursor.fetchall()
        except Exception as e:
            print('execute sql {0} is error'.format(sql))
            sys.exit('ERROR: load data from database error caused {0}'.format(str(e)))
        finally:
            cursor.close()
            conn.close()
        return result

    def insert_sql(self, sql):
        try:
            conn = self.get_pool_conn()
            cursor = conn.cursor()
            cursor.execute(sql)
            result = True
        except Exception as e:
            print('ERROR: execute  {0} causes error'.format(sql))
            sys.exit('ERROR: update data from database error caused {0}'.format(str(e)))
        finally:
            cursor.close()
            conn.commit()
            conn.close()
        return result

    def update_sql(self, sql):
        try:
            conn = self.get_pool_conn()
            cursor = conn.cursor()
            cursor.execute(sql)
            result = True
        except Exception as e:
            print('ERROR: execute  {0} causes error'.format(sql))
            sys.exit('ERROR: update data from database error caused {0}'.format(str(e)))
        finally:
            cursor.close()
            conn.commit()
            conn.close()
        return result


if __name__ == '__main__':
    pg_conn_pool = PgConnectionPool()
    for _ in range(10):
        sp_organization_sql = 'SELECT name,code,short_name,type,id from sp_organization ORDER BY created_time desc limit 1;'
        print(pg_conn_pool.select_sql(sp_organization_sql))
