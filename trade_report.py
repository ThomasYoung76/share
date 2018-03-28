"""
    股票交易行情实时报表
"""
import numpy as np
import pandas as pd
import matplotlib as plt
import tushare as ts
from datetime import datetime
import xlrd
from share.conf.trade_config import *

now = datetime.now()

print("当前时间：%s" % str(datetime.now()))

def get_stock_data(filename, sheet_name='实时行情', is_update=False):
    """
    默认从excel中获取股票数据，如果is_update为True，则从网上获取数据，并更新到excel中
    :param filename: excel文件名
    :param sheet_name: 页签
    :param is_update: 是否从网上获取数据并更新excel
    :return: DataFrame
    """
    if is_update:
        writer = pd.ExcelWriter(filename)
        df_today = ts.get_today_all()
        df_today = df_today.rename(columns=today_map)
        df_today.to_excel(writer, sheet_name=sheet_name, freeze_panes=(1, 1), index=False)
        writer.save()
    else:
        content = xlrd.open_workbook(filename=filename, encoding_override='gbk')
        df_today = pd.read_excel(content, sheet_name=sheet_name, engine='xlrd')
    return df_today

df_today = get_stock_data(filename='./doc/交易数据.xls', sheet_name='实时行情', is_update=True)

# df_tick_sh = []
#
# for co in df_today['code'].tail(10):
#     df_tick = ts.get_realtime_quotes(co)
#     df_tick_sh.append(df_tick)

