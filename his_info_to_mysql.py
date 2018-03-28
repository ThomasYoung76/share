"""
    获取股票历史数据保存到mysql中
    如上证, 深证, 沪深300, 上证50
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tushare as ts
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR

config = {
    'host': '10.1.77.84',
    'port': 3306,
    'user': 'yang',
    'password': '123',
    'db': 'stock',
    'charset': 'utf8'
}


def py_conn(*args, **kwargs):
    """
    连接mysql
    :param args:
    :param kwargs: 连接mysql的配置
    :return: 返回connect对象和cursor对象
    """
    # 连接mysql
    try:
        conn = pymysql.Connection(*args, **kwargs)
    except:
        print("Connect failed")
        import traceback
        print(traceback.print_exc())
        sys.exit(1)
    # 创建游标
    cursor = conn.cursor()
    return {'conn': conn, 'cursor': cursor}


def hist_data_to_sql(code, engine):
    """
    将股票近三年的历史数据存入mysql
    :param code: str or list 股票代码
    :param engine:
    :return:
    """
    # 获取股票近三年的历史数据
    if isinstance(code, str):
        df_his = ts.get_hist_data(code)
        # 存入数据库
        df_his.to_sql('%s_his' % code, engine, if_exists='append', index=True, index_label='date', dtype={'date': VARCHAR(50)})
    elif isinstance(code, list):
        for co in code:
            df_his = ts.get_hist_data(co)
            #  - replace: If table exists, drop it,   - append: If table exists, insert data.
            df_his.to_sql('%s_his' % co, engine, if_exists='append', index=True, index_label='date', dtype={'date': VARCHAR(50)})  #  - replace: If table exists, drop it,
    else:
        raise TypeError('type of code should be str or list')

def get_engine():
    """
    创建mysql的连接对象, 获得SQLAlchemy 连接对象
    :return:
    """
    try:
        engine = create_engine('mysql+pymysql://yang:123@10.1.77.84/stock?charset=utf8')
    except:
        print("Connect mysql error.")
        sys.exit(1)
    return engine



if __name__ == "__main__":
    # 获取上证, 深证, 沪深300, 上证50
    code_list = ['sh', 'sz', 'hs300', 'sz50', 'sh600000', 'sh600111']
    hist_data_to_sql(code_list, get_engine())

