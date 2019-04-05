import tushare as ts
import pandas as pd
import numpy as np
import time 
class ReData(object):
    def __init__(self):
        self.pro = ts.pro_api(token='6bf40c7acd89be6fadaba6ab8b06e22b988cb6fed50d552885df6f81')

    def storage(self):
        df = self.pro.stock_basic()
        a = df.loc[:, 'ts_code']
        for i in a:
            data = self.pro.daily(ts_code = i, start_date = '20100101', end_date = '20190402')
            name = i[0:6]
            data.to_csv('./data/'+ name + '.csv')
            time.sleep(0.1)


if __name__ == "__main__":
    hdata = ReData()
    hdata.storage()

