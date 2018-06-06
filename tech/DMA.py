# -*- coding: UTF-8 -*-
import talib as ta
import numpy as np
from util import StockUtil as su
from tech import StockTechIndicator


class DMA(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=10, time_period2=50, time_period3=6):
        dma = 0.0
        ama = 0.0
        max_time_period = max(time_period1, time_period2, time_period3)
        data = su.get_basic_data(stock_code, date, max_time_period + time_period3).sort_index(ascending=False)

        if data.shape[0] >= max_time_period + 1:
            data['MA1'] = data['CLOSE'].rolling(window=time_period1).mean()
            data['MA2'] = data['CLOSE'].rolling(window=time_period2).mean()
            data['DMA'] = data['MA1'] - data['MA2']
            data['AMA'] = data['DMA'].rolling(window=time_period3).mean()
            dma = round(data['DMA'].as_matrix()[-1], 3)
            ama = round(data['AMA'].as_matrix()[-1], 3)

        if np.isnan(dma) or np.isinf(dma) or np.isneginf(dma):
            dma = 0.0
        if np.isnan(ama) or np.isinf(ama) or np.isneginf(ama):
            ama = 0.0

        self.save_tech_data(stock_code, date, {'DMA': dma, 'AMA': ama})
        return dma, ama

if __name__ == "__main__":
    b = DMA()
    print b.calculate('chbtc', 'btc_cny', '5min', 1498653000)