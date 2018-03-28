"""
    获取股票基本面数据 fundamental data
    基本面类数据提供所有股票的基本面情况，包括股本情况、业绩预告和业绩报告等。主要包括以下类别：
        沪深股票列表 get_stock_basics
        业绩报告（主表） get_report_data
        盈利能力数据 get_profit_data
        营运能力数据 get_operation_data
        成长能力数据 get_growth_data
        偿债能力数据 get_debtpaying_data
        现金流量数据 get_cashflow_data
"""
import pandas as pd
import tushare as ts
import time
from share.conf.fundmental_config import *


def get_basics_data_en(year=2017, quarter=1):
    """
    股票基本面数据， 列名采用英文，和tushare中列名保持一致
    :param year: 年份
    :param quarter: 季度
    :return:
    """
    # 获取数据
    report = ts.get_report_data(year, quarter)
    profit = ts.get_profit_data(year, quarter)
    operation = ts.get_operation_data(year, quarter)
    growth = ts.get_growth_data(year, quarter)
    debtpaying = ts.get_debtpaying_data(year, quarter)
    cashflow = ts.get_cashflow_data(year, quarter)
    # 写入excel
    basics_name = ['report', 'profit', 'operation', 'growth', 'debtpaying', 'cashflow']
    sheet_name = list(map(lambda x: '%s_%s_%s'%(x, year, quarter), basics_name))
    report.to_excel(writer, sheet_name=sheet_name[0], freeze_panes=[1,1], index=False)
    profit.to_excel(writer, sheet_name=sheet_name[1], freeze_panes=[1,1], index=False)
    operation.to_excel(writer, sheet_name=sheet_name[2], freeze_panes=[1,1], index=False)
    growth.to_excel(writer, sheet_name=sheet_name[3], freeze_panes=[1,1], index=False)
    debtpaying.to_excel(writer, sheet_name=sheet_name[4], freeze_panes=[1,1], index=False)
    cashflow.to_excel(writer, sheet_name=sheet_name[5], freeze_panes=[1,1], index=False)
    writer.save()

def get_basics_data_cn(year=2017, quarter=1):
    """
    股票基本面数据， 写入excel时，列名转换成中文，易于阅读
    :param year: 年份
    :param quarter: 季度
    :return:
    """
    # 获取数据
    report = ts.get_report_data(year, quarter)
    report = report.rename(columns=report_map)

    profit = ts.get_profit_data(year, quarter)
    profit = profit.rename(columns=profit_map)

    operation = ts.get_operation_data(year, quarter)
    operation = operation.rename(columns=operation_map)

    growth = ts.get_growth_data(year, quarter)
    growth = growth.rename(columns=growth_map)

    debtpaying = ts.get_debtpaying_data(year, quarter)
    debtpaying = debtpaying.rename(columns=debtpaying_map)

    cashflow = ts.get_cashflow_data(year, quarter)
    cashflow = cashflow.rename(columns=cashflow_map)

    # 写入excel
    basics_name = ['业绩报告', '盈利能力', '营运能力', '成长能力', '偿债能力', '现金流量']
    sheet_name = list(map(lambda x: '%s_%s_%s'%(x, year, quarter), basics_name))
    report.to_excel(writer, sheet_name=sheet_name[0], freeze_panes=[1,1], index=False)
    profit.to_excel(writer, sheet_name=sheet_name[1], freeze_panes=[1,1], index=False)
    operation.to_excel(writer, sheet_name=sheet_name[2], freeze_panes=[1,1], index=False)
    growth.to_excel(writer, sheet_name=sheet_name[3], freeze_panes=[1,1], index=False)
    debtpaying.to_excel(writer, sheet_name=sheet_name[4], freeze_panes=[1,1], index=False)
    cashflow.to_excel(writer, sheet_name=sheet_name[5], freeze_panes=[1,1], index=False)
    writer.save()




if __name__ == "__main__":
    # # ----------------------------- 英文列名 --------------------------
    # # 获得excel的写对象
    # writer = pd.ExcelWriter('./doc/stock_fundamental_data.xls')
    # # 股票列表数据
    # stock_basics = ts.get_stock_basics()
    # stock_basics.to_excel(writer, sheet_name='股票列表', freeze_panes=(1, 1), index=True)
    # writer.save()
    # # 获取2017年钱前3季度数据
    # for quarter in [3,2,1]:
    #     get_basics_data_en(2017, quarter)
    # # ---------------------------- 我是分界线 --------------------------

    # ----------------------------- 中文列名 --------------------------
    # 获得excel的写对象
    writer = pd.ExcelWriter('./doc/股票基本面数据.xls')

    # 股票列表数据
    stock_basics = ts.get_stock_basics()
    stock_basics = stock_basics.rename(columns=stock_map)
    stock_basics.to_excel(writer, sheet_name='股票列表', freeze_panes=(1,1), index=True)
    writer.save()

    # 获取2017年钱前3季度数据
    for quarter in [3, 2, 1]:
        get_basics_data_cn(2017, quarter)
    # ---------------------------- 我是分界线 --------------------------

