# -*- coding: UTF-8 -*-
import talib as ta
import numpy as np
from util import StockUtil as su
from tech import StockTechIndicator


class CCI(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period=14):
        cci = 0.0
        data = su.get_basic_data(stock_code, date, time_period + 1).sort_index(ascending=False)

        if data.shape[0] >= time_period + 1:
            cci = round(ta.CCI(data['HIGH'].as_matrix(), data['LOW'].as_matrix(), data['CLOSE'].as_matrix(), time_period)[-1], 3)
        if np.isnan(cci) or np.isinf(cci) or np.isneginf(cci):
            cci = 0.0
        self.save_tech_data(stock_code, date, {'CCI':cci})
        return cci


if __name__ == "__main__":
    b = CCI()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)