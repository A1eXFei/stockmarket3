# -*- coding: UTF-8 -*-
import numpy as np
from util import StockUtil as su
from tech import StockTechIndicator

class BIAS(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=6, time_period2=12, time_period3=24):
        bias1 = 0.0
        bias2 = 0.0
        bias3 = 0.0
        max_time_period = max(time_period1, time_period2, time_period3)
        #print max_time_period
        data = su.get_basic_data(stock_code, date, max_time_period + 1).sort_index(ascending=False)

        if data.shape[0] >= max_time_period + 1:
            data['MA1'] = data['CLOSE'].rolling(window=time_period1).mean()
            data['MA2'] = data['CLOSE'].rolling(window=time_period2).mean()
            data['MA3'] = data['CLOSE'].rolling(window=time_period3).mean()
            close = data['CLOSE'].as_matrix()[-1]
            data['BIAS1'] = (close - data['MA1']) * 100 / data['MA1']
            data['BIAS2'] = (close - data['MA2']) * 100 / data['MA2']
            data['BIAS3'] = (close - data['MA3']) * 100 / data['MA3']

            bias1 = round(data['BIAS1'].as_matrix()[-1], 3)
            bias2 = round(data['BIAS2'].as_matrix()[-1], 3)
            bias3 = round(data['BIAS3'].as_matrix()[-1], 3)
        #print data
        #print data
        if np.isinf(bias1) or np.isnan(bias1) or np.isneginf(bias1):
            bias1 = 0.0
        if np.isinf(bias2) or np.isnan(bias2) or np.isneginf(bias2):
            bias2 = 0.0
        if np.isinf(bias3) or np.isnan(bias3) or np.isneginf(bias3):
            bias3 = 0.0
        self.save_tech_data(stock_code, date, {'BIAS_6': bias1, 'BIAS_12':bias2, 'BIAS_24':bias3})
        return bias1, bias2, bias3

if __name__ == "__main__":
    b = BIAS()
    print b.calculate('chbtc', 'btc_cny', '5min', 1498653000)