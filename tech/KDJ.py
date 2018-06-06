# -*- coding: UTF-8 -*-
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class KDJ(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=9, time_period2=3, time_period3=3):
        kdj_k = 0.0
        kdj_d = 0.0
        kdj_j = 0.0
        data = su.get_basic_data(stock_code, date, max(time_period1, time_period2, time_period3) * 5)

        if data.shape[0] > time_period1:
            data['LOW_N'] = data['LOW'].rolling(window=time_period1).min()
            data['LOW_N'].fillna(value=data['LOW'].expanding().min(), inplace=True)
            data['HIGH_N'] = data['HIGH'].rolling(window=time_period1).max()
            data['HIGH_N'].fillna(value=data['HIGH'].expanding().max(), inplace=True)
            data['RSV'] = (data['CLOSE'] - data['LOW_N']) / (data['HIGH_N'] - data['LOW_N']) * 100
            data.sort_index(ascending=False, inplace=True)

            data['KDJ_K'] = data['RSV'].ewm(com=(time_period2 - 1)).mean()
            data['KDJ_D'] = data['KDJ_K'].ewm(com=(time_period2 - 1)).mean()
            data['KDJ_J'] = 3 * data['KDJ_K'] - 2 * data['KDJ_D']
            kdj_k = round(data['KDJ_K'].as_matrix()[-1], 3)
            kdj_d = round(data['KDJ_D'].as_matrix()[-1], 3)
            kdj_j = round(data['KDJ_J'].as_matrix()[-1], 3)

        if np.isnan(kdj_d) or np.isinf(kdj_d) or np.isneginf(kdj_d):
            kdj_d = 0.0
        if np.isnan(kdj_j) or np.isinf(kdj_j) or np.isneginf(kdj_j):
            kdj_j = 0.0
        if np.isnan(kdj_k) or np.isinf(kdj_k) or np.isneginf(kdj_k):
            kdj_k = 0.0
        self.save_tech_data(stock_code, date, {'KDJ_K': kdj_k, 'KDJ_D':kdj_d, 'KDJ_J':kdj_j})
        return kdj_k, kdj_d, kdj_j

if __name__ == "__main__":
    b = KDJ()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)