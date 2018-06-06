# -*- coding: UTF-8 -*-
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class MA(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=5, time_period2=10, time_period3=20):
        ma_1 = 0.0
        ma_2 = 0.0
        ma_3 = 0.0

        max_time_period = max(time_period1, time_period2, time_period3)
        data = su.get_basic_data(stock_code, date, max_time_period + 1).sort_index(ascending=False)

        if data.shape[0] >= max_time_period + 1:
            data['MA1'] = data['CLOSE'].rolling(window=time_period1).mean()
            data['MA2'] = data['CLOSE'].rolling(window=time_period2).mean()
            data['MA3'] = data['CLOSE'].rolling(window=time_period3).mean()

            ma_1 = round(data['MA1'].as_matrix()[-1], 3)
            ma_2 = round(data['MA2'].as_matrix()[-1], 3)
            ma_3 = round(data['MA3'].as_matrix()[-1], 3)

        if np.isnan(ma_1) or np.isinf(ma_1) or np.isneginf(ma_1):
            ma_1 = 0.0
        if np.isnan(ma_2) or np.isinf(ma_2) or np.isneginf(ma_2):
            ma_2 = 0.0
        if np.isnan(ma_3) or np.isinf(ma_3) or np.isneginf(ma_3):
            ma_3 = 0.0
        self.save_tech_data(stock_code, date, {'MA_5': ma_1, 'MA_10':ma_2, 'MA_20':ma_3})
        return ma_1, ma_2, ma_3

if __name__ == "__main__":
    b = MA()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)