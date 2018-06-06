# -*- coding: UTF-8 -*-
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class MTM(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=12, time_period2=6):
        max_time_period = max(time_period1, time_period2)
        mtm = 0.0
        mamtm = 0.0
        data = su.get_basic_data(stock_code, date, max_time_period * 2).sort_index(ascending=False)

        if data.shape[0] >= max_time_period * 2:
            data['N_CLOSE'] = data['CLOSE'].shift(time_period1)
            data['MTM'] = data['CLOSE'] - data['N_CLOSE']
            mtm = round(data['MTM'].as_matrix()[-1], 3)
            mamtm = round(data['MTM'].as_matrix()[-6:].sum() / float(time_period2), 3)

        if np.isnan(mtm) or np.isinf(mtm) or np.isneginf(mtm):
            mtm = 0.0
        if np.isnan(mamtm) or np.isinf(mamtm) or np.isneginf(mamtm):
            mamtm = 0.0

        self.save_tech_data(stock_code, date, {'MTM': mtm, 'MAMTM': mamtm})
        return mtm, mamtm

if __name__ == "__main__":
    b = MTM()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)