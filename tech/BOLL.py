# -*- coding: UTF-8 -*-
import talib as ta
import numpy as np
from util import StockUtil as su
from tech import StockTechIndicator


class BOLL(StockTechIndicator):
    def __init__(self):
        StockTechIndicator.__init__(self)

    def calculate(self, stock_code, date, time_period=20, nbdev_up=2, nbdev_down=2):
        upper_brand = 0.0
        middle_brand = 0.0
        lower_brand = 0.0
        data = su.get_basic_data(stock_code, date,  time_period + 1).sort_index(ascending=False)

        if data.shape[0] >= time_period:
            upper_brands, middle_brands, lower_brands = ta.BBANDS(data['CLOSE'].as_matrix(), time_period, nbdev_up, nbdev_down)
            upper_brand = round(upper_brands[-1], 3)
            middle_brand = round(middle_brands[-1], 3)
            lower_brand = round(lower_brands[-1], 3)
        if np.isinf(upper_brand) or np.isnan(upper_brand) or np.isneginf(upper_brand):
            upper_brand = 0.0
        if np.isinf(middle_brand) or np.isnan(middle_brand) or np.isneginf(middle_brand):
            middle_brand = 0.0
        if np.isinf(lower_brand) or np.isnan(lower_brand) or np.isneginf(lower_brand):
            lower_brand = 0.0

        self.save_tech_data(stock_code, date, {'BOLL_UP': upper_brand, 'BOLL_LOW':lower_brand, 'BOLL_MID':middle_brand})
        return upper_brand, middle_brand, lower_brand

if __name__ == "__main__":
    b = BOLL()
    print b.calculate('chbtc', 'btc_cny', '5min', 1497449100)