"""
    分析大盘历史数据
"""

import xlrd
import pandas as pd
import re
import time

workbook = xlrd.open_workbook('doc/大盘历史数据.xls')

df_sh = pd.read_excel(workbook, sheet_name='sh', engine='xlrd')


# 插入具体星期几
def get_week(str_date):
    res = re.findall(r'\d+(.*?)\d+', str_date)[0]
    return time.strptime(str_date, '%Y'+ res + '%m' + res + '%d').tm_wday

weekday = df_sh['date'].apply(get_week)
df_sh.insert(loc=df_sh.shape[1], column='week', value=weekday)

# 计算涨跌幅
df_sh.insert(loc=df_sh.shape[1], column='scope', value=((df_sh['close'] - df_sh['open'])*100/df_sh['close']))
print(df_sh.head(2))

df_low = df_sh[df_sh['scope'] <= -3]
print(df_low)

print(df_low['date'].groupby(df_low['week']).count())