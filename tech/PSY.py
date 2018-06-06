# -*- coding: UTF-8 -*-
import numpy as np
from util import StockUtil as su
from tech import StockTechIndicator


class PSY(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period1=12, time_period2=6):
        psy_12 = 0.0
        psy_6 = 0.0
        data = su.get_basic_data(stock_code, date, time_period1 + 1).sort_index(ascending=False)
        if data.shape[0] >= time_period1:
            count = 0.0
            data['P_CLOSE'] = data['CLOSE'].shift(1)
            data['DIFF'] = data['CLOSE']-data['P_CLOSE']
            data['DIFF'].fillna(0, inplace=True)
            #print data
            for each in data[1:].itertuples():
                if each.DIFF > 0:
                    count += 1.0
            psy_12 = round((count / time_period1 * 100), 3)

            count = 0.0
            for each in data[-6:].itertuples():
                if each.DIFF > 0:
                    count += 1.0
            psy_6 = round((count / time_period2 * 100), 3)
        #print data
        if np.isnan(psy_12) or np.isinf(psy_12) or np.isneginf(psy_12):
            psy_12 = 0.0
        if np.isnan(psy_6) or np.isinf(psy_6) or np.isneginf(psy_6):
            psy_6 = 0.0
        self.save_tech_data(stock_code, date, {'PSY_12': psy_12, 'PSY_6':psy_6})
        return psy_12, psy_6


if __name__ == "__main__":
    b = PSY()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)