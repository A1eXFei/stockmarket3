from tech.BBI import BBI
from tech.BIAS import BIAS
from tech.BOLL import BOLL
from tech.BRAR import BRAR
from tech.CCI import CCI
from tech.DMA import DMA
from tech.KDJ import KDJ
from tech.MA import MA
from tech.MACD import MACD
from tech.MTM import MTM
from tech.PSY import PSY
from tech.ROC import ROC
from tech.RSI import RSI
from tech.VR import VR
from tech.WR import WR

class StockTechCalculator(object):
    def __init__(self, stock_code, date):
        self.__stock_code = stock_code
        self.__date = date

    def calculate_indicator(self):
        bbi = BBI()
        bias = BIAS()
        boll = BOLL()
        brar = BRAR()
        cci = CCI()
        dma = DMA()
        kdj = KDJ()
        ma = MA()
        macd = MACD()
        mtm = MTM()
        psy = PSY()
        roc = ROC()
        rsi = RSI()
        vr = VR()
        wr = WR()

        bbi.calculate(self.__stock_code, self.__date)
        bias.calculate(self.__stock_code, self.__date)
        boll.calculate(self.__stock_code, self.__date)
        brar.calculate(self.__stock_code, self.__date)
        cci.calculate(self.__stock_code, self.__date)
        dma.calculate(self.__stock_code, self.__date)
        kdj.calculate(self.__stock_code, self.__date)
        ma.calculate(self.__stock_code, self.__date)
        macd.calculate(self.__stock_code, self.__date)
        mtm.calculate(self.__stock_code, self.__date)
        psy.calculate(self.__stock_code, self.__date)
        roc.calculate(self.__stock_code, self.__date)
        rsi.calculate(self.__stock_code, self.__date)
        vr.calculate(self.__stock_code, self.__date)
        wr.calculate(self.__stock_code, self.__date)
