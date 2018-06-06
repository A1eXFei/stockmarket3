# -*- coding: UTF-8 -*-
import talib as ta
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class RSI(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=6, time_period2=14, time_period3=24):
        rsi_6 = 0.0
        rsi_14 = 0.0
        rsi_24 = 0.0
        data = su.get_basic_data(stock_code, date, time_period3 + 1).sort_index(ascending=False)
        if data.shape[0] >= time_period3 + 1:
            rsi_6 = round(ta.RSI(data['CLOSE'].as_matrix(), time_period1)[-1], 3)
            rsi_14 = round(ta.RSI(data['CLOSE'].as_matrix(), time_period2)[-1], 3)
            rsi_24 = round(ta.RSI(data['CLOSE'].as_matrix(), time_period3)[-1], 3)
        if np.isnan(rsi_6) or np.isinf(rsi_6) or np.isneginf(rsi_6):
            rsi_6 = 0.0
        if np.isnan(rsi_14) or np.isinf(rsi_14) or np.isneginf(rsi_14):
            rsi_14 = 0.0
        if np.isnan(rsi_24) or np.isinf(rsi_24) or np.isneginf(rsi_24):
            rsi_24 = 0.0
        self.save_tech_data(stock_code, date, {'RSI_6': rsi_6, 'RSI_14':rsi_14, 'RSI_24':rsi_24})
        return rsi_6, rsi_14, rsi_24


if __name__ == "__main__":
    b = RSI()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)