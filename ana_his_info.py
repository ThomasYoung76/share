"""
    利用pandas分析mysql的stock数据库中的表数据
"""
from his_info_to_mysql import *
import matplotlib.finance as mpf
from matplotlib.pylab import date2num
import datetime
import pandas as pd
import tushare as ts

# 绘图设置中文格式
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

def drawK(code):
    """
    画日K线图
    :param code: 股票代码
    :return:
    """
    sql = 'select * from %s_his'% code
    df = pd.read_sql(sql, get_engine(), index_col='date')

    # 对tushare获取到的数据转换成candlestick_ohlc()方法可读取的格式
    data_list = []
    for dates, row in df.iterrows():
        # 将时间转换为数字
        date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
        t = date2num(date_time)
        open, high, close, low = row[:4]
        datas = (t, open, high, low, close)
        data_list.append(datas)

    # 创建画布
    fig, ax = plt.subplots(figsize=(12,6))

    ax.xaxis_date()
    plt.xticks(rotation=45)
    plt.yticks()
    plt.title("%s"%code)
    plt.xlabel("时间")
    plt.ylabel("股价（元）")
    mpf.candlestick_ohlc(ax,data_list,width=1.5,colorup='red',colordown='green')
    plt.grid()
    plt.show()

def hist_to_excel(code, writer):
    """
    大盘历史数据写入excel
    :param code: 代码
    :param writer: excel的writter
    :return:
    """
    # sql = 'select * from %s_his' % code
    # df = pd.read_sql(sql, get_engine(), index_col='date')
    df = ts.get_hist_data(code)
    df.to_excel(writer, sheet_name=code, freeze_panes=(1, 1), index=True)
    writer.save()


if __name__ == "__main__":
    # 股票代码
    code = 'sh'
    # drawK(code)   # 画K线图
    writer = pd.ExcelWriter('./doc/大盘历史数据.xls')
    for code in ['sh', 'sz', 'hs300', 'sz50', 'sh600111']:
        hist_to_excel(code, writer)



