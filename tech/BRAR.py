# -*- coding: UTF-8 -*-
import numpy as np
from util import StockUtil as su
from tech import StockTechIndicator


class BRAR(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period=26):
        ar = 0.0
        br = 0.0
        data = su.get_basic_data(stock_code, date, time_period + 1).sort_index(ascending=False)

        if data.shape[0] >= time_period + 1:
            ar = round((data['HIGH'][1:] - data['OPEN'][1:]).sum() / (data['OPEN'][1:] - data['LOW'][1:]).sum() * 100, 3)
            data['P_CLOSE'] = data['CLOSE'].shift(1)
            data['BR_U'] = data['HIGH'][1:] - data['P_CLOSE'][1:]
            data['BR_D'] = data['P_CLOSE'][1:] - data['LOW'][1:]
            br = round(data[data['BR_U'] > 0]['BR_U'].sum() / data[data['BR_D'] > 0]['BR_D'].sum() *100, 3)
        if np.isnan(ar) or np.isinf(ar) or np.isneginf(ar):
            ar = 0.0
        if np.isnan(br) or np.isinf(br) or np.isneginf(br):
            br = 0.0
        self.save_tech_data(stock_code, date, {'BRAR_BR': br,'BRAR_AR':ar})
        return br, ar

if __name__ == "__main__":
    b = BRAR()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)