# -*- coding: UTF-8 -*-
import logging
import ConfigParser
import multiprocessing as mp
from datetime import *
from logging.config import fileConfig
from util import DateUtil as du
from basic import StockBasicData
from StockTechCalculator import StockTechCalculator
from fundamental import StockFundamentalData
from StockExporter import StockExporter
from StockCleaner import StockCleaner

EXP_DIR = "D:\\StockData\\"
config_file = ConfigParser.SafeConfigParser()
config_file.read("../ss_config.ini")
EXP_DIR = config_file.get('export', 'dir')

fileConfig("logging_config.ini")
logger = logging.getLogger(__name__)


def create_process(stock_code, start_date, end_date):
    logger.info("Start to process stock code: " + stock_code + " from " + start_date + " to " + end_date)
    sbd = StockBasicData()
    basic_data = sbd.download_basic_data(stock_code, start_date, end_date)
    basic_data_fq = sbd.download_basic_data_fq(stock_code, start_date, end_date)
    if (basic_data is not None) and (basic_data.shape[0] > 0):
        sbd.save_data(basic_data, basic_data_fq)
        sbd.update_end_date(stock_code, basic_data)
        logger.info("Basic data is downloaded and saved into database, is going to calculate tech indicator")
        for each in basic_data.itertuples():
            business_date = str(each.Index)
            logger.info("Calculate " + stock_code + " tech indicator for " + business_date)
            stc = StockTechCalculator(stock_code, business_date)
            stc.calculate_indicator()
        logger.info("All tech indicators are calculated")
        sfd = StockFundamentalData(stock_code, EXP_DIR)
        sfd.download_fundamental_data()
        se = StockExporter(EXP_DIR, stock_code, start_date, end_date)
        se.export()
        sc = StockCleaner(stock_code, end_date)
        sc.clean()
    else:
        logger.warn("No data found for stock code: " + stock_code)

if __name__ == '__main__':
    try:
        logger.info("Downloading full stock list....")

        sbd = StockBasicData()
        sbd.download_stock_list()
        logger.info("Download completed")

        now = datetime.now()
        today = du.convertDateToString(now, '%Y-%m-%d')
        #today = "1999-12-31"
        logger.debug("Today is: " + today)
        stock_list = sbd.get_stock_list(today)

        pool = mp.Pool(processes=1)
        #for stock in stock_list[:5]:
        for stock in stock_list:
            stock_code = stock[0]
            last_updated_date = du.convertDateToString(stock[1], '%Y-%m-%d')
            pool.apply_async(create_process, (stock_code, last_updated_date, today))

        pool.close()
        pool.join()
        logger.info("All stocks information is downloaded")
    except Exception, e:
        logger.error(e.message)
