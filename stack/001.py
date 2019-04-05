import numpy as np
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
import random
#失败 。。 self与cls共用未解决，代码未运行，上存在位置错误
class Stock(object):

    def __init__(self, money, stock, start_date, end_date):
        self.money = money
        self.total = money
        self.cash = money
        self.share_dict = {stock:0}
        self.start_date = start_date
        self.end_date = end_date
        self.df = 0
        self.x = []
        self.y = []
        self.rate = []

    def require_data(self):
        ts.set_token('6bf40c7acd89be6fadaba6ab8b06e22b988cb6fed50d552885df6f81')
        pro = ts.pro_api()
        self.df = pro.daily(self.share_dict['stack'], self.start_date, self.end_date)
        self.df.sort_index(by=['trade_date'], ascending = True)

    def buy(self, cls):
        cls.require_data()
        ma_list = [5, 10, 20]
        self.df = self.df.sort_index(by=['trade_date'], ascending = True)
        for ma in ma_list:
            self.df['MA'  +str(ma)] = self.df['close'].rolling(ma).mean()
        self.df = self.df.dropna()
        x, y = self.df.shape
        for t in range(x):
            if (self.df['MA5'][t] <= self.df['MA10'][t]) & (self.df['MA5'][t+1] > self.df['MA10'][t+1]):
                price = self.df['close'][t]
                cls.exchange_buy(price)
            elif (self.df['MA5'][t] >= self.df['MA10'][t]) & (self.df['MA5'][t+1] < self.df['MA10'][t+1]):
                price = self.df['close'][t]
                cls.exchange_sell(price)
            self.x.append(self.total)
            self.y.append(t)
            self.rate.append(self.total / float(self.money))

    def exchange_buy(self, price):
        if (self.cash % (100*price * 1.0003) != 0) & (self.share_dict['stack'] == 0):
            i = self.cash / (100*price)
            self.cash -= i * 100*price * 1.0003
            self.total = self.cash + 100*price

    def exchange_sell(self, price):
        if self.share_dict['stack'] > 0:
            self.total = self.cash + self.share_dict['stack'] + price * 0.9997
            self.cash += self.share_dict['stack'] * 0.9997
            self.share_dict['stack'] = 0

    def calculate_profit(self, cls):
        cls.buy()
        plt.plot(self.x, self.y)
        plt.plot()


        
if __name__ == "__main__":
    user = Stock(100000.00, '000725', '20100101', '20190403')
    user.calculate_profit()
    

    