# -*- coding: UTF-8 -*-
import talib as ta
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class WR(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=14, time_period2=6):
        wr_14 = 0.0
        wr_6 = 0.0
        data = su.get_basic_data(stock_code, date, time_period1 + 1).sort_index(ascending=False)

        if data.shape[0] >= time_period1 + 1:
            wr_14 = round(ta.WILLR(data['HIGH'].as_matrix(), data['LOW'].as_matrix(), data['CLOSE'].as_matrix(), time_period1)[-1] * -1, 3)
            wr_6 = round(ta.WILLR(data['HIGH'].as_matrix(), data['LOW'].as_matrix(), data['CLOSE'].as_matrix(), time_period2)[-1] * -1, 3)
        if np.isnan(wr_14) or np.isinf(wr_14) or np.isneginf(wr_14):
            wr_14 = 0.0
        if np.isnan(wr_6) or np.isinf(wr_6) or np.isneginf(wr_6):
            wr_6 = 0.0
        self.save_tech_data(stock_code, date, {'WR_14': wr_14, 'WR_6':wr_6})
        return wr_14, wr_6


if __name__ == "__main__":
    b = WR()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)