# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from util import StockUtil as su
from tech import StockTechIndicator


class BBI(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=3, time_period2=6, time_period3=12, time_period4=24):
        bbi = 0.0
        max_time_period = max(time_period1, time_period2, time_period3, time_period4)
        data = su.get_basic_data(stock_code, date, max_time_period + 1).sort_index(ascending=False)

        if data.shape[0] >= max_time_period + 1:
            data['MA1'] = data['CLOSE'].rolling(window=time_period1).mean()
            data['MA2'] = data['CLOSE'].rolling(window=time_period2).mean()
            data['MA3'] = data['CLOSE'].rolling(window=time_period3).mean()
            data['MA4'] = data['CLOSE'].rolling(window=time_period4).mean()
            data['BBI'] = (data['MA1'] + data['MA2'] + data['MA3'] + data['MA4'])/ 4

            bbi = round(data['BBI'].as_matrix()[-1], 3)
        if np.isnan(bbi) or np.isinf(bbi) or np.isneginf(bbi):
            bbi = 0.0
        self.save_tech_data(stock_code, date, {'BBI':bbi})
        return bbi


if __name__ == "__main__":
    b = BBI()
    #print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)