# -*- coding: UTF-8 -*-
import os
import sys
import pandas as pd
import logging
from logging.config import fileConfig

try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

reload(sys)
sys.setdefaultencoding('gbk')

fileConfig("logging_config.ini")
logger = logging.getLogger(__name__)


class StockFundamentalData():
    def __init__(self, stock_code, export_dir):
        self.dir = export_dir + os.sep + stock_code
        # 主要财务指标
        self.url_zycwzb = "http://quotes.money.163.com/service/zycwzb_" + stock_code + ".html?type=report"
        # 主要财务指标 - 盈利能力
        self.url_ylnl = self.url_zycwzb + "&part=ylnl"
        # 主要财务指标 - 偿还能力
        self.url_chnl = self.url_zycwzb + "part=chnl"
        # 主要财务指标 - 成长能力
        self.url_cznl = self.url_zycwzb + "part=cznl"
        # 主要财务指标 - 营运能力
        self.url_yynl = self.url_zycwzb + "part=yynl"
        # 财务报表摘要
        self.url_cwbbzy = "http://quotes.money.163.com/service/cwbbzy_" + stock_code + ".html"
        # 资产负债表
        self.url_zcfzb = "http://quotes.money.163.com/service/zcfzb_" + stock_code + ".html"
        # 利润表
        self.url_lrb = "http://quotes.money.163.com/service/lrb_" + stock_code + ".html"
        # 现金流量表
        self.url_xjllb = "http://quotes.money.163.com/service/xjllb_" + stock_code + ".html"

    def download_fundamental_data(self):
        try:
            if not os.path.exists(self.dir):
                logger.debug("Make dir because there is no existing dir")
                os.makedirs(self.dir)

            for attr in dir(self):
                if attr[:3] == "url":
                    filename = self.dir + os.sep + attr[4:] + ".csv"
                    data = self.__get_data__(getattr(self, attr))
                    data.to_csv(filename)
        except Exception, e:
            logger.error(e.message)

    def __get_data__(self, url):
        data = pd.read_csv(url).T
        data.columns = data.iloc[0]
        return data[1:-1]