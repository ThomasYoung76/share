import tushare as ts
import pandas as pd
from conf.mv_conf import *




def get_movie_info(lang='cn'):
    realtime_df = ts.realtime_boxoffice()   # 实时票房
    day_df = ts.day_boxoffice()     # 每日票房
    month_df = ts.month_boxoffice()     # 每月票房，默认上一月
    day_cinema_df = ts.day_cinema()        #取上一日全国影院票房排行数据
    if not lang or lang == 'cn':
        realtime_df = realtime_df.rename(columns=realtime_map)
        day_df = day_df.rename(columns=day_map)
        month_df = month_df.rename(columns=month_map)
        day_cinema_df = day_cinema_df.rename(columns=day_cinema_map)
    return {'realtime': realtime_df, 'day': day_df, 'month': month_df, 'cinema': day_cinema_df}

if __name__ == '__main__':
    writer = pd.ExcelWriter('./doc/电影票房信息.xls')
    info = get_movie_info()
    info['realtime'].to_excel(writer, sheet_name='实时票房', freeze_panes=(1, 0), index=False)
    info['day'].to_excel(writer, sheet_name='每日票房', freeze_panes=(1, 0), index=False)
    info['month'].to_excel(writer, sheet_name='每月票房', freeze_panes=(1, 0), index=False)
    info['cinema'].to_excel(writer, sheet_name='影院票房', freeze_panes=(1, 0), index=False)
    writer.save()

