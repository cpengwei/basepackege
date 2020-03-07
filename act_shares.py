# encoding:utf-8

import tushare as ts
import pandas as pd
import os

token = '7d63c3c1b2cd76782246c6498af99f737b8c28003102fe211adb9f46'
ts.set_token(token)
tp = ts.pro_api()


def add_shares_type(code):
    tmp_code = str(code).strip()
    if tmp_code[0] == '6':
        new_code = '{}.SH'.format(tmp_code)
        return new_code
    elif tmp_code[0] in ['0', '3']:
        new_code = '{}.SZ'.format(tmp_code)
        return new_code
    else:
        print('这个代码[{}]不是沪深股票代码！'.format(code))


def get_basic(trade_date, num=300):
    # 调用基础API获取沪深300的成分股
    shares_item300 = ts.get_hs300s()
    shares_items = shares_item300.head(num)
    data = []
    # 获取沪深300成分股的指标
    for item in shares_items.index:
        code = add_shares_type(shares_items.loc[item, 'code'])
        basic_data = tp.query('daily_basic', ts_code=code, trade_date=trade_date,
                              fields='trade_date,ts_code,close,pb,pe,dv_ratio')
        basic_data['name'] = shares_items.loc[item, 'name']
        data.append(basic_data)
    datas = pd.concat(data).sort_values(by='pb')  # 按市净率升幂排序
    datas.index = pd.Series([n for n in range(int(len(datas.index)))])  # 重置行索引
    return datas


def to_csv(data, outpath):
    # 修改列名并写入csv文件
    column = {'name': '名称', 'ts_code': '代码', 'close': '收盘价', 'pb': '市净率', 'pe': '市盈率',
              'dv_ratio': '股息率', 'trade_date': '交易日期'}  # 市净率=总市值/净资产,市盈率=总市值/净利润
    shares = data.rename(columns=column, copy=False).reindex(columns=column.values())  # 列名替换并重新排序
    # 写入csv
    print(shares)
    shares.to_csv(outpath, index=0, encoding='utf_8_sig')  # index=0表示不写入行索引


if __name__ == '__main__':
    outpath = os.path.join(os.getcwd(),'shares.csv')
    data = get_basic('20200306')
    to_csv(data, outpath)
