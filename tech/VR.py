# -*- coding: UTF-8 -*-
import numpy as np
from tech import StockTechIndicator
from util import StockUtil as su


class VR(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period=24):
        vr = 0.0
        data = su.get_basic_data(stock_code, date, time_period + 1).sort_index(ascending=False)

        if data.shape[0] >= time_period:
            p_volume = 0.0
            n_volume = 0.0
            data['P_CLOSE'] = data['CLOSE'].shift(1)
            data['DIFF'] = data['CLOSE']-data['P_CLOSE']
            data['DIFF'].fillna(0, inplace=True)

            for each in data[1:].itertuples():
                if each.DIFF >= 0:
                    p_volume += each.VOLUME
                else:
                    n_volume += each.VOLUME
            vr = round(p_volume / n_volume * 100, 3)
        if np.isnan(vr) or np.isinf(vr) or np.isneginf(vr):
            vr = 0.0
        self.save_tech_data(stock_code, date, {'VR': vr})
        return vr


if __name__ == "__main__":
    b = VR()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)