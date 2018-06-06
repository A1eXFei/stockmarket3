# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class MACD(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, short=12, long=26, mid=9):
        dif = 0.0
        dea = 0.0
        macd = 0.0
        max_time_period = max(short, long, mid)
        data = su.get_basic_data(stock_code, date, max_time_period*3).sort_index(ascending=False)
        if data.shape[0] >= max_time_period*3:
            close = data['CLOSE'].values
            ewma_short = pd.ewma(close,span=short)
            ewma_long = pd.ewma(close,span=long)
            difs = (ewma_short-ewma_long)
            deas = pd.ewma(difs,span=mid)
            macds = (difs-deas)*2

            dif = round(difs[-1], 3)
            dea = round(deas[-1], 3)
            macd = round(macds[-1], 3)

        if np.isnan(dif) or np.isinf(dif) or np.isneginf(dif):
            dif = 0.0
        if np.isnan(dea) or np.isinf(dea) or np.isneginf(dea):
            dea = 0.0
        if np.isnan(macd) or np.isinf(macd) or np.isneginf(macd):
            macd = 0.0

        self.save_tech_data(stock_code, date, {'MACD_DIF': dif, 'MACD_DEA':dea, 'MACD':macd})
        return dif, dea, macd

if __name__ == "__main__":
    b = MACD()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)