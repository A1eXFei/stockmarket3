# -*- coding: UTF-8 -*-
import talib as ta
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class ROC(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=14, time_period2=6):
        roc = 0.0
        maroc = 0.0
        data = su.get_basic_data(stock_code, date, time_period1 * 2).sort_index(ascending=False)

        if data.shape[0] >= time_period1:
            rocs = ta.ROC(data['CLOSE'].as_matrix(), time_period1)
            roc = round(rocs[-1], 3)
            maroc = round(rocs[-6:].sum()/float(time_period2), 3)

        if np.isnan(roc) or np.isinf(roc) or np.isneginf(roc):
            roc = 0.0
        if np.isnan(maroc) or np.isinf(maroc) or np.isneginf(maroc):
            maroc = 0.0
        self.save_tech_data(stock_code, date, {'ROC': roc, 'MAROC':maroc})
        return roc, maroc


if __name__ == "__main__":
    b = ROC()
    print b.calculate('chbtc', 'btc_cny', '5min', 1498653000)