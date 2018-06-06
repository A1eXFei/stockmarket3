# -*- coding: UTF-8 -*-
import logging
import tushare as ts
import pandas as pd
from logging.config import fileConfig
from util import DatabaseUtil as dbu
from util import StockUtil as su


fileConfig("logging_config.ini")
logger = logging.getLogger(__name__)


class StockBasicData(object):
    def __init__(self):
        pass

    def download_stock_list(self):
        stock_list = ts.get_stock_basics()
        stock_list[['esp']] = stock_list[['esp']].astype(float, raise_on_error='ignore')
        dbu.save_pd_data('sdtb_stock_list_tmp', stock_list)
        dbu.call('prc_check_stock_list')


    def download_basic_data_fq(self, stock_code, start_date, end_date):
        # print 'Getting basic fq data'
        try:
            data = ts.get_h_data(stock_code, start=start_date, end=end_date, index=False)
            if data is not None:
                data = data.sort_index(ascending=True)[1:]
                data['code'] = pd.Series(stock_code, index=data.index)
            # print data
            return data
        except Exception, e:
            logger.error(e.message)
            return None


    def download_basic_data(self, stock_code, start_date, end_date):
        data = su.get_hist_data(stock_code, start_date, end_date)

        if data is None:
            logger.warn("No basic data is downloaded from 163 for stock code " + stock_code + ", try from tushare now...")
            print("No basic data is downloaded from 163 for stock code " + stock_code + ", try from tushare now...")
            data = ts.get_hist_data(stock_code, start_date, end_date)
            if not 'turnover' in data.columns:
                logger.warn("Tushare data without turnover data")
                data.insert(loc=2,column="turnover",value=0)

        if data is not None:
            data = data.sort_index(ascending=True)[1:]
            data['code'] = pd.Series(stock_code, index=data.index)
        return data


    def get_stock_list(self, end_date):
        sql = "SELECT CODE, LASTUPDATEDDATE FROM pdtb_stock_list where LASTUPDATEDDATE < '" + end_date + "' and TIMETOMARKET <> '0000-00-00' ORDER BY CODE"
        return dbu.get_data(sql)


    def save_data(self, basic_data, basic_data_fq=None):
        try:
            tech_data = pd.DataFrame(index=basic_data.index, columns=['code'], data=basic_data['code'])
            dbu.save_pd_data('pdtb_stock_basic_data', basic_data)
            dbu.save_pd_data('pdtb_stock_tech_data', tech_data)

            if basic_data_fq is not None:
                dbu.save_pd_data('pdtb_stock_basic_data_fq', basic_data_fq)
        except Exception as e:
            logger.error(e.message)


    def update_end_date(self, stock_code, basic_data):
        last_updated_date = basic_data[-1:].index.values[0]
        sql = 'UPDATE pdtb_stock_list SET LASTUPDATEDDATE = \'' + last_updated_date + '\' WHERE CODE = \'' + stock_code + '\''
        dbu.update(sql)

    def is_working_day(self, date):
        sql = "SELECT fn_is_holiday('" + date + "')"
        flag = dbu.get_data(sql)[0][0]
        if flag == 'W':
            return True
        else:
            return False
