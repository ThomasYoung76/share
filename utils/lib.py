"""
    封装通用方法
"""
__author__ = 'YangShiFu'
__date__ = '2017-11-19'

import xlrd
import pandas as pd

def load_data_from_excel(filename, sheet_name, encoding='gbk'):
    reader = xlrd.open_workbook(filename, encoding_override=encoding)
    df = pd.read_excel(reader, sheet_name=sheet_name, engine='xlrd')
    return df

